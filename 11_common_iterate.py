# odd = lambda x : bool(x % 2)
# numbers = [n for n in range(10)]
# for i in range(len(numbers)):
#     if odd(numbers[i]):
#         del numbers[i]  # BAD: Deleting item from a list while iterating over it

# solution

odd = lambda x : bool(x % 2)
numbers = [n for n in range(10)]
numbers[:] = [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
print(numbers)
# [0, 2, 4, 6, 8]
