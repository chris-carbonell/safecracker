# safecracker
from safecracker import safecracker as sc
from safecracker.safe import zip as safe
from safecracker.tools import mask, dictionary
from examples import testing

# get safe
safe = safe.Safe("examples/safe/easy.zip")

# get safecracker
pwg_mask1 = mask.PasswordGenerator("-d", max_len=1)  # just one digit
pwg_mask2 = mask.PasswordGenerator("-d", max_len=2)  # just two digits
pwg_mask3 = mask.PasswordGenerator("-d", max_len=3)  # just three digits
pwg_dict = dictionary.PasswordGenerator()
safecracker = sc.Safecracker(PasswordGenerator=[pwg_mask1, pwg_mask2, pwg_mask3, pwg_dict])

# crack
testing.test(safe, safecracker, ["hello world.txt"])