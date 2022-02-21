# Dependencies

# general
import itertools
import logging
import string

# Classes

class PasswordGenerator:
    """
    generator of passwords

    ...

    Attributes
    ----------
    max_len : int
        maximum length of potential passwords

    Methods
    -------
    get_password()
        generate passwords
    """

    def __init__(self, *args, **kwargs):

        # get max_len
        self.max_len = kwargs['max_len'] if "max_len" in kwargs else 14

        # get possible characters
        if len(args) == 0:
            # by default, bring everything in
            self.possible_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        else:
            # otherwise, just bring in whatever was specified
            self.possible_chars = ""
            self.possible_chars += string.ascii_uppercase if "-u" in args else ""
            self.possible_chars += string.ascii_lowercase if "-l" in args else ""
            self.possible_chars += string.digits if "-d" in args else ""
            self.possible_chars += string.punctuation if "-p" in args else ""

        # calculate number of passwords in generator for tqdm
        self.pw_len = 0
        for n in range(1, self.max_len + 1):
            self.pw_len += len(self.possible_chars) ** n

    def get_password(self):
        for n in range(1, self.max_len + 1):
            for chars in itertools.product(self.possible_chars, repeat=n):
                yield "".join(chars)
