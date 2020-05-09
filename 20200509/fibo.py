# count = 1000
# number = 1
# result = 1
#
# while result < count:
#     result = number + number
#     number = result-1
#     count = result + number
# print(count)


count = 1000000000000
first = 1
second = 1

print(first)
print(second)

while second < count:
    myeongwoo = second
    second = first + second
    first = myeongwoo
    print(second)
