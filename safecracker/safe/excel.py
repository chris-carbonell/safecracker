# Dependencies

# general
import logging
import os

# excel
import win32com.client

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
        self.filename = os.path.abspath(filename)  # needs to be full path
        self.open = False
        self.password = None
        self.xlApp = win32com.client.Dispatch("Excel.Application")

    def attempt(self, password):

        logging.debug(f"attempting: {password}")

        try:
            xlwb = self.xlApp.Workbooks.Open(self.filename, False, True, None, password)
        except:
            pass  # no password found
        else:
            self.password = password
            self.open = True
            self.xlApp.Quit()

        return self.open
