def factor(num):
    if num in [0,1]:
        return []
    for n in xrange(2,num):
        if num%n==0:
            return [n]+factor(num/n) 

    return [num]


if __name__=="__main__":
    print max(factor(600851475143))
