answer = [3, 7, 4, 1, 7, 4, 1, 3]
cardback = ["A","A","A","A","A","A","A","A" ]
cardopen = ["A","A","A","A","A","A","A","A" ]

print("MyeongWoo Game Starts!")

while True :
    print(cardback)
    num =  int (input("type 1st number : "))
    a1 = answer[num-1]
    # print( card[int(num)-1] ) #,( card[int(num)-1] ))
    num2 = int( input("type 2nd number : "))
    a2 = answer[num2-1]
    # print( card[int(num2)-1] )
    cardopen[num-1] = a1
    cardopen[num2-1] = a2
    print(cardopen)


    #if( int (input("type 1st number : ")) == int( input("type 2nd number : "))):
    if(a1 == a2):
        print("good job!")
    else :
        print("try again!")

    input("아무거나 눌러서 계속...")
    cardopen[num-1] = "A"
    cardopen[num2-1] = "A"
    count = 10
    while count > 0:
        print(" ")
        count -= 1 #count = count -1
