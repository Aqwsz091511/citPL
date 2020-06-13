count = 100000
first = 1
second = 1



print(first)
print(second)

while second < count:
    me = second
    second = first + second
    first = me
    print(second)
