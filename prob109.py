def score(num):
    if num==0: return 0
    (x,y) = num
    return x*y

dart_single = [(25,1)]+[(x,1) for x in xrange(1,21)]
dart_double = [(25,2)]+[(x,2) for x in xrange(1,21)]
dart_triple = [(x,3) for x in xrange(1,21)]
dart_all = dart_single + dart_double + dart_triple
dart_chkout = [(x,0,0) for x in dart_double]+\
              [(x,y,0) for x in dart_all for y in dart_double]+\
              [(x,y,z) for x in dart_all for y in dart_all for z in dart_double if x<=y]
assert(len(dart_chkout)==42336)
dart_chkout = [score(x)+score(y)+score(z) for (x,y,z) in dart_chkout]
print len(filter(lambda x:x<100,dart_chkout))

