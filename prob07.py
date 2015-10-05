def sieve(bound):
    s=[True]*bound
    for n in xrange(3,int(bound**0.5)):
        s[n*n::2*n]=[False]*((bound-1-n*n)//(2*n)+1)
    return [2]+[x for x in xrange(2,bound) if x%2!=0 and s[x]]

x=sieve(200000)
print x[10000]

