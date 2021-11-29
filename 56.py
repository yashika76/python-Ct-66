
for x in range(100, 501):
    if (x%7==0) and (x%9==0):
        nl.append(str(x))
print (','.join(nl))