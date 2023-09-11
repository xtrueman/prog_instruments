import profile
import pstats
from pstats import SortKey

longstr = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]"""

def have_similar_chars( s: str ) -> bool:
    for i, c in enumerate(s[:-1]):
        if c in s[:i] or c in s[i+1:]:
            return True
    return False

def lls0( s: str ) -> int:
    sl = len(s)
    if sl == 0: return 0
    maxlen = 1
    for i in range(sl):
        for j in range(i+1, sl+1):
            if not have_similar_chars( s[i:j] ):
                maxlen = max( maxlen, j - i )
    return maxlen


def lls1( s: str ) -> int:
    sl = len(s)
    if sl == 0: return 0
    maxlen = 1
    for i in range(sl):
        for j in range(i+1, sl+1):
            ht = set()
            hsc = False
            for c in s[i:j]:
                if c in ht:
                    hsc = True
                    break
                else:
                    ht.add(c)
            if hsc:
                break
            else:
                maxlen = max( maxlen, j - i )
    return maxlen


def lls2( s: str ) -> int:
    sl = len(s)
    if sl == 0: return 0
    maxlen = 1
    for i in range(sl):
        for j in range(i+1, sl+1):
            hsc = False
            ss = s[i:j]
            for k, c in enumerate(ss[:-1]):
                if c in ss[:k] or c in ss[k+1:]:
                    hsc = True
                    break
            if not hsc:
                maxlen = max( maxlen, j - i )
    return maxlen

def lls3( s: str ) -> int:
    sl = len(s)
    if sl == 0: return 0
    maxlen = 1
    for i in range(sl):
        for j in range(i+1, sl+1):
            hsc = False
            ss = s[i:j]
            for k, c in enumerate(ss[:-1]):
                if c in ss[:k] or c in ss[k+1:]:
                    hsc = True
                    break
            if hsc:
                break
            else:
                if j - i > maxlen:
                    maxlen = j - i
    return maxlen

def lls4( s: str ) -> int:
    sl = len(s)
    if sl <= 1: return sl
    maxlen = 1
    i = 0
    j = 1
    ccnt = { s[0] : 1 }
    while i < sl and j < sl:
        j += 1
        #print('ij1', i, j, s[i:j], maxlen, ccnt)
        if s[j-1] not in ccnt or ccnt[s[j-1]] == 0:
            ccnt[s[j-1]] = 1
            if j - i > maxlen:
                maxlen = j - i
        else:
            ccnt[s[j-1]] += 1
            while i < j and ccnt[s[j-1]] > 1:
                ccnt[s[i]] -= 1
                i += 1
                #print('ij2', i, j, s[i:j], maxlen)
    return maxlen



f = open(__file__)
lines = f.readlines()

def prof_lls0():
    for line in lines:
        maxlen = lls0( line )

def prof_lls1():
    for line in lines:
        maxlen = lls1( line )

def prof_lls2():
    for line in lines:
        maxlen = lls2( line )

def prof_lls3():
    for line in lines:
        maxlen = lls3(longstr)

def prof_lls4():
    for line in lines:
        maxlen = lls4(longstr)


print('prof_lls0...')
prof = profile.Profile()
prof.runcall( prof_lls0 )
stats = pstats.Stats(prof)
stats \
 .strip_dirs() \
 .sort_stats(SortKey.CUMULATIVE) \
 .print_stats()

print('prof_lls1...')
prof = profile.Profile()
prof.runcall( prof_lls1 )
stats = pstats.Stats(prof)
stats.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()

print('prof_lls2...')
prof = profile.Profile()
prof.runcall( prof_lls2 )
stats = pstats.Stats(prof)
stats.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()

# print('prof_lls3...')
# prof = profile.Profile()
# prof.runcall( prof_lls3 )
# stats = pstats.Stats(prof)
# stats.strip_dirs().print_stats()

print('prof_lls4...')
prof = profile.Profile()
prof.runcall( prof_lls4 )
stats = pstats.Stats(prof)
stats.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()
