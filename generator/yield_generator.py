def yield_generator(n):
    l = range(n)
    for i in l:
        yield i * i


mygenerator = yield_generator(3)
print(mygenerator)
for i in mygenerator:
    print(i)
# >>> <generator object createGenerator at 0xb7555c34>
# >>> 0
#     1
#     4
