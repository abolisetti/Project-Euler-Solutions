#Project Euler 24
from Euler import *
#import ceil
import itertools
def perm(n, s):
    """
    requires function factorial()
    Find the nth permutation of the string s. Example:

    >>>perm(30, 'abcde')
    bcade
    """
    if len(s)==1: return s
    q, r = divmod(n, factorial(len(s)-1))
    return s[q] + perm(r, s[:q] + s[q+1:])

print(perm(1000000, "0123456789"))
