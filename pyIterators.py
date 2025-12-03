#Iterators is an object that contains a countable number of values
#__iter__()
#__next__()
tuplesta = ("waveguide","coaxial","network")
stringsta = "Hello World"
myiterator = iter(tuplesta)
myiterator2 = iter(stringsta)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator2))
print(next(myiterator2))
print(next(myiterator2))

for x in tuplesta:
    print(x)
