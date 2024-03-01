import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
 import OLIVIA
elif bit == '32bit':
 import OLI32
