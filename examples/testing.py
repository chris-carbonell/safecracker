# Dependencies

# general
from datetime import datetime
import inspect
import logging
import os
import time

# Funcs

def test(safe, safecracker, del_files = [], **kwargs):

    # Constants

    output_ts = datetime.now().strftime('%Y-%m-%d %H%M%S')
    output_filename = f"{output_ts} cracked_password.txt"

    # time
    time_start = time.time()

    # get calling script details
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename_calling = os.path.basename(module.__file__)

    # logging
    logging.basicConfig(
        filename=f"{output_ts} {filename_calling}.log", 
        encoding="utf-8", 
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
        )

    # attempt to crack safe
    safecracker.crack(safe, **kwargs)

    # output
    if safe.open:
        print(f"password found: {safe.password}")

        # save
        with open(output_filename, "w") as f:
            f.write(f"filename: {safe.filename}\n")
            f.write(f"password: {safe.password}\n")
    else:
        print("password not found")

    print(f"execution time (s): {round(time.time()-time_start, 2)}")

    # cleanup
    for file_path in del_files:
        if os.path.exists(file_path):
            os.remove(file_path)
