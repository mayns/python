

n = input()
l = list(input())

l.sort()

def pack(l, i, s):
    # global u
    # u +=1
    # print u
    if i >= len(l): return 1 if s == 0 else 0
    count = pack(l, i + 1, s)
    if count: return count
    count += pack(l, i + 1, s - l[i])
    return count

import timeit
start = timeit.default_timer()
if n in l:
    print 'YES'

else:
    print 'YES' if pack(l,0, n) else 'NO'

print timeit.default_timer() - start