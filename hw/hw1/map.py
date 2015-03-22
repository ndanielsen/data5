

list1 = [x for x in range(1,10)]

def add(x):
	return x + 1

print "hello"
print list1


mapped =  map(add, list1)

print sum(mapped)

print reduce(lambda x,y : x + y, mapped)