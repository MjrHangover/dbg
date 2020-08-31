#!/usr/bin/env python
# user def function magic
# __module__
# __qualname__
# __module__
# __defaults__
# __globals__
# __dict__
# __closure__
# __annotations__
# __kwdefaults__
# __all__ # defines what to import when M import *
# __doc__
# __debug__
##
# __author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
# __copyright__ = "Copyright 2007, The Cogent Project"
# __credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
#                     "Matthew Wakefield"]
# __license__ = "GPL"
# __version__ = "1.0.1"
# __maintainer__ = "Rob Knight"
# __email__ = "rob@spot.colorado.edu"
# __status__ = "Production" # prototype, development, production
#
# **--- just going to leave that there for future reference
###
"""Module for custom debugger"""
import sys
import functools
import timeit

__author__ = "Tyler Sammons"
__version__ = '0.3'
__maintainer__ = "Tyler Sammons"
__status__ = "Prototype"
__date__ = '8/30/2020'

# init
global RED
global YEL
global RST
global DBGFLG

DBGFLG = 'debug'

try:
	from unbufferedIO import Unbuffered
	sys.stdout = Unbuffered(sys.stdout)
except ImportError:
	print("\n\nERR: unbufferedIO failed to import\n")
	pass
try:
	import colorama

	RED = colorama.Fore.RED
	YEL = colorama.Fore.LIGHTYELLOW_EX # Fore.YELLOW stopped working
	RST = colorama.Style.RESET_ALL
	colorama.init()
except ImportError:
	print("\nERR: colorama failed to import\n")
	RED = ''
	YEL = ''
	RST = ''
	pass

def DBGMSG(MSG): print(f'\n\n{RED}{MSG}{RST}\n\n')
def DBGLOC(MSG): print(f'\n\n{YEL}{MSG}{RST}\n\n')

def Debug(func):
	if not DBGFLG in sys.argv:
		return func
	@functools.wraps(func)
	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]
		kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
		signature = ", ".join(args_repr + kwargs_repr)
		DBGLOC(f"Calling {func.__name__}({signature})")
		value = func(*args, **kwargs)
		DBGMSG(f"{func.__name__!r} returned {value!r}")
		return value
	return wrapper_debug

def main():
	print(f"Nothing to see here")
if __name__ == '__main__':
	main()
