# Dependencies

# general
from datetime import datetime
from itertools import chain, islice
import logging
import string
import sys
from tqdm import tqdm

# threading
import concurrent.futures.thread
from concurrent.futures import ThreadPoolExecutor, as_completed, wait

# safecracker
from safecracker.tools import dictionary as sct

# Classes

class Safecracker:
    """
    safecracker

    ...

    Attributes
    ----------
    Safe : Safe
        safe to crack
    PasswordGenerator : PasswordGenerator
        generator of passwords to try

    Methods
    -------
    """
    
    def __init__(self, **kwargs):

        # get passwords
        self.ls_pw_gen = []
        if "PasswordGenerator" in kwargs:
            if isinstance(kwargs['PasswordGenerator'], list):
                self.ls_pw_gen = kwargs['PasswordGenerator']
            else:
                # assume just one generator passed
                self.ls_pw_gen = [kwargs['PasswordGenerator']]
        else:
            self.ls_pw_gen = [sct.PasswordGenerator()]  # default to rockyou

    def crack(self, Safe, **kwargs):
        for pw_gen in self.ls_pw_gen:
            if not Safe.open:
                self.crack_one_gen(Safe, pw_gen, **kwargs)

    def crack_one_gen(self, Safe, PasswordGenerator, **kwargs):

        # setup quitting
        bool_attempt = True

        # Funcs

        def attempt_or_quit(Safe, pw):
            if bool_attempt:
                return Safe.attempt(pw)

        def chunks(iterable, size=1000):
            iterator = iter(iterable)
            for first in iterator:
                yield chain([first], islice(iterator, size - 1))

        # get count of total passwords to try for tqdm
        if PasswordGenerator.pw_len:
            pw_len = PasswordGenerator.pw_len  # calculated by the PasswordGenerator itself
        elif "pw_len" in kwargs:
            pw_len = kwargs['pw_len']  # manually provided
        else:
            pw_len = len(list(PasswordGenerator.get_password()))  # calculated here as a last resort

        # get threading config
        if "num_threads" in kwargs:
            
            # get num_threads
            try:
                num_threads = int(kwargs['num_threads'])
            except:
                logging.warning("defaulting num_threads")
                num_threads = 2  # default to 2

            # if 1 then just run without threading
            if num_threads == 1:
                bool_threading = False
            else:
                bool_threading = True
                
        else:
            bool_threading = False  # default to no threading

        # crack
        
        # with threading
        if bool_threading:

            logging.debug(f"threading activated with {num_threads}")

            # get chunk size
            if "chunk_size" in kwargs:
                chunk_size = int(kwargs['chunk_size'])
            else:
                chunk_size = 1000  # default to 1000

            with tqdm(total=pw_len, unit=" attempts") as progress:

                with ThreadPoolExecutor(max_workers=num_threads) as executor:

                    # get chunks
                    # chunk generator to minimize the size of the pool bc smaller pools are easier to cancel
                    gen_chunk = chunks(PasswordGenerator.get_password(), chunk_size)
                    
                    # loop over chunks
                    for chunk in gen_chunk:
                    
                        # create futures
                        futures = []
                        for pw in chunk:
                            future = executor.submit(attempt_or_quit, Safe=Safe, pw=pw)
                            future.add_done_callback(lambda p: progress.update())
                            futures.append(future)

                        # check if the safe is open
                        for future in as_completed(futures):

                            # check
                            if Safe.open:
                                
                                bool_attempt = False

                                done, not_done = wait(futures, timeout=0)
                                for future in not_done:
                                    _ = future.cancel()  # cancel
                                _ = concurrent.futures.wait(not_done, timeout=None)  # wait for remainder

                                break  # break out of as_completed
                            
                        if not bool_attempt:
                            break  # break out of chunk loop

        # no threading
        else:
            logging.debug("no threading activated")
            for pw in tqdm(PasswordGenerator.get_password(), total=pw_len, unit=" attempts"):

                # attempt
                attempt_or_quit(Safe, pw)

                # check
                if Safe.open:
                    bool_attempt = False
                    break