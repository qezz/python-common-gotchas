def a(l=[]):
    l.append(1)
    return l

if __name__ == "__main__":
    print(a()) # returns [1]
    print(a()) # returns [1, 1] and so on...
