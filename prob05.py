def gcd(a,b):
    if a<b:
        return gcd(b,a)
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    g = gcd(a,b)
    return a/g*b/g*g

print reduce(lambda x,y: lcm(x,y), range(1,21))

