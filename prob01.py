def adduntil(times,num):
    res = [x*times for x in range(1,num) if x*times < num]
    return sum(res)

if __name__=="__main__":
    print adduntil(3,1000)+adduntil(5,1000)-adduntil(15,1000)
