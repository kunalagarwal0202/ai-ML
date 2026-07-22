isPizzaAvailabe=False
isCheeseAvailable=False
isMaggiAvailable=False
isNoodlesAvailable=False
ifPastaisAvailable=False
ifPannerisAvailable=False
testCondition=False

if(testCondition):
    print("this is a test stetment")

if(isPizzaAvailabe):
    print("I am making pizza")
    if(isCheeseAvailable):
        print("I will be adding cheese")

elif(isNoodlesAvailable):
    print("I am making noodles")

elif(ifPastaisAvailable):
    print("I am making pasta")

elif(ifPannerisAvailable):
    print("I am making panner curry")

else:
    print("I will be making maggie")



print("8"+"9")
print(8+9)


"""input1=int(input("Please provide with a input 1: "))
input2=int(input("Please provide with a input 2: "))

operation=input("Please provide with the following operators: +, -, *, /")

if(operation=="+"):
    print(f"this is addition: {input1+input2}")

elif(operation=="-"):
    print(f"this is substraction: {input1-input2}")

elif(operation=="*"):
    print(f"this is multiplication: {input1*input2}")

elif(operation=="/"):
    print(f"this is division: {input1/input2}")

else:
    print(f"You have provided a wrong operator, Please check and verify {operation}")"""




if(isPizzaAvailabe and isCheeseAvailable):
    print("we have eveything for our pizza")
else:
    print("we dont have some of the ingrdients")


if(isPizzaAvailabe or isCheeseAvailable):
    print("we have eveything for our pizza")
else:
    print("we dont have some of the ingrdients")



    
"""for i in range(0,10): for i =0, for i=1, for i=2, for i=3, for i= 4, for i=5, for i=6, for i=7, for =8, fori=9
    print(i) print(0), print(1),print(2)...........print"""

result=0

for i in range(0,1000):
    result=result+i
    print(result)

