def list_fibonacci(bound):
    res=[]
    f_a = 1
    f_b = 2
    f_c = 3
    res.append(f_b)
    while f_c < bound:
        f_a=f_b
        f_b=f_c
        f_c=f_a+f_b
        if f_c %2 == 0:
            res.append(f_c)
    return sum(res)

if __name__=="__main__":
    print list_fibonacci(4000000)
