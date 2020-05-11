objects = [1, 2, 1, 2, 3]

print(len(set(id(i) for i in objects)))


# b = 1
# c = '1'
#
# print(b.__hash__(), c.__hash__())
# print(id(b),id(c))

def h():
  print(12)

def f():
  g(h)

def g(a):
  a()

g(f)

'''
print
h
g
f
g
module
'''