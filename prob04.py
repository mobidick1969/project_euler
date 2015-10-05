def is_palindrome(num):
    num=list(str(num))
    return num==list(reversed(num))

if __name__=="__main__":
    assert(is_palindrome(99))
    ans = []
    for x in xrange(100,1000):
        for y in xrange(100,1000):
            if is_palindrome(x*y):
                ans.append(x*y)
    print max(ans)
