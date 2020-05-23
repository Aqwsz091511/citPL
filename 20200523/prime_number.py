#count = 24 #count라는 variable 안에 10이라는 숫자가 있다.
#number = 2#number라는 variable안에 2라는 숫자가 있다.
#while number < count:  #number가 count보다 작을때
#    if(count%number == 0): #만약 count를 number로 나눴을때의 나머지가 0이라면
#        print("oh no") #oh no라는 말을 print한다.
    # if(count%number != 0):
    #     print("it's not prime number")
#    number = number + 1 #number라는 variable은 number라는 variable 에다가 +1을 한것이다.






count = 23
number = 2
ohno = 0
while number < count:
    if(count%number == 0):
        # print("oh no")
        ohno = ohno + 1
    number = number + 1

if (ohno == 0 ):
    print("Yes!")
else :
    print('no')
print(ohno)
