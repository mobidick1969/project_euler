x=range(1000)
y=range(1000)
triples=[ (xx,yy,1000-xx-yy) for xx in x for yy in y if xx<yy and yy<(1000-xx-yy)]
pytas = [ (x,y,z) for (x,y,z) in triples if (x**2+y**2==z**2) ]
(rx,ry,rz)=pytas[0]
print rx*ry*rz
