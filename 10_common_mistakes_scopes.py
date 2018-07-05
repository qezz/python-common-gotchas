x = 10

def foo_x():
    x += 1
    print(x)

def fixed_foo_x():
    global x
    x += 1
    print(x)


lst = [1, 2, 3]
def foo1():
    lst.append(5)   # This works ok...

foo1()
lst
# [1, 2, 3, 5]

lst = [1, 2, 3]
def foo2():
    lst += [5]      # ... but this bombs!

foo2()
