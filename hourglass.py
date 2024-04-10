def triangle():
    length = 10
    hash = "#"
    for i in range(length):
        for j in range(length - i):
            print(" ", end='')
        print(hash)
        hash += "##"

# def old_reverse_triangle():
#     length = 10
#     astr = "*" * (2 * length - 1)
#     for i in range(length):
#         for j in range(length + i):
#             print(" ", end='')
#         print(astr)
#         astr = astr[2:]

    
def reverse_triangle():
    length = 10
    hash = "#" * (2 * length - 1)
    for i in range(length):
        print(" " * (i + 1), end='')
        print(hash)
        hash = hash[2:]

reverse_triangle()
triangle()
