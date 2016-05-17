mygenerator = (x * x for x in range(3))

for i in mygenerator:
    print(i)

# >>> 0
#     1
#     4

print(mygenerator)
# <generator object <genexpr> at 0x0000000002A5F480>

print(0 in mygenerator)

# >>> False
