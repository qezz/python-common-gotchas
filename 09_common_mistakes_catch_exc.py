## Not allowed in Py3
# try:
#     l = ["a", "b"]
#     int(l[2])
# except ValueError, IndexError:  # To catch both exceptions, right?
#     pass

try:
    l = ["a", "b"]
    int(l[2])
except (ValueError, IndexError) as e:
    print("Caught:", e)
