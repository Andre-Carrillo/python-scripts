firstlist = [i*2 for i in range(50)]
secondlist = [i**2 for i in range(50)]
thirdlist = [i-1 for i in range(50)]

ziplist = zip(firstlist, secondlist, thirdlist)
print(list(ziplist))
