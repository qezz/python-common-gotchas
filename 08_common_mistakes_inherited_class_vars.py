class A(object):
    x = 1

class B(A):
    pass

class C(A):
    pass

print(A.x, B.x, C.x)
# 1 1 1


B.x = 2
print(A.x, B.x, C.x)
# 1 2 1

A.x = 3
print(A.x, B.x, C.x)
# 3 2 3
