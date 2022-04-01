upcinput=input('insert the UPC: ')
lupc=[0]
cnum=0
probcdig=upcinput[-1]
upcinput=upcinput[:-1]
for digit in upcinput:
    lupc.append(int(digit))
catch=lupc.pop(0)
dig=3*sum(lupc[::2])+sum(lupc[1::2])
m=dig%10
if m==catch:
    cnum=catch
else:
    cnum=10-m
if str(cnum)==probcdig:
    print('Valid UPC')
else:
    upc=upcinput+probcdig
    print('Invalid UPC')