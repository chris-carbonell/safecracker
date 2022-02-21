# Dependencies

# general
import logging

# Classes

class PasswordGenerator:
    """
    generator of passwords

    ...

    Attributes
    ----------
    dictionary_filename : str
        path to dictionary file (e.g., rockyou.txt)

    Methods
    -------
    get_password()
        generate passwords
    """

    def __init__(self, dictionary_filename = None, encoding = "CP1252"):

        # get dictionary
        if dictionary_filename:
            self.dictionary_filename = dictionary_filename
        else:
            self.dictionary_filename = "safecracker/tools/dictionaries/rockyou.txt"  # default to rockyou

        self.encoding = encoding

        # calculate number of passwords in generator for tqdm
        self.pw_len = sum(1 for i in open(self.dictionary_filename, "rb"))

    def get_password(self):
        for line in open(self.dictionary_filename, encoding=self.encoding, errors="ignore"):
            yield line.strip()
