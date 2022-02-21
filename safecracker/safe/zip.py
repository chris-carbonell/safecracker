# Dependencies

# general
import logging
import zipfile

# Classes

class Safe:
    """
    password-protected safe

    ...

    Attributes
    ----------
    filename : str
        filename

    Methods
    -------
    attempt(password)
        attempt a password
    """

    def __init__(self, filename):
        self.filename = filename
        self.open = False
        self.password = None

    def attempt(self, password):

        logging.debug(f"attempting: {password}")

        password_byte = password.encode()

        zip_file = zipfile.ZipFile(self.filename, 'r')

        try:
            zip_file.extractall(pwd=password_byte)
        except:
            pass  # no password found
        else:
            self.password = password
            self.open = True
        finally:
            zip_file.close()

        return self.open