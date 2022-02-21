# safecracker
from safecracker import safecracker as sc
from safecracker.safe import zip as safe
from safecracker.tools import mask as sct
from examples import testing

# get safe
safe = safe.Safe("examples/safe/easy.zip")

# get safecracker
pwg = sct.PasswordGenerator("-d", max_len=3)  # just digits
safecracker = sc.Safecracker(PasswordGenerator=pwg)

# crack
testing.test(safe, safecracker, ["hello world.txt"], num_threads=2)