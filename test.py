## WITH CHAT GPT

def triangle():
    length = 10
    hash = "#"
    for i in range(length):
        print("-" * (length - i - 1), end='')
        print(hash, end='')
        print("-" * (length - i - 1))
        hash += "##"

def reverse_triangle():
    length = 10
    hash = "#" * (2 * length - 1)
    for i in range(length):
        print("-" * i, end='')
        print(hash, end='')
        print("-" * i)
        hash = hash[2:]

reverse_triangle()
triangle()
