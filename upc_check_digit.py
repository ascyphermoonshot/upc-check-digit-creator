upcinput=input()
lupc=[0]
cnum=0
for digit in upcinput:
    lupc.append(int(digit))
catch=lupc.pop(0)
dig=3*sum(lupc[::2])+sum(lupc[1::2])
m=dig%10
if m==catch:
    cnum=catch
else:
    cnum=10-m
upc=upcinput+str(cnum)
print(upc)