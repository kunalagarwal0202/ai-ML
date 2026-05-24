print("hello world")
print('I love prograamming in python 123456')
print(min(3,4,5,6))
print(max(3,4,56,8))

max(7,8,9,0)
print(4+5)

print(" python is a development langugae")

for x in range(0,10):
    print("this is my start loop operation happeing")
    print(x)
    print(x+2)
    print("end of one loop")

print("test")

age=30
print(age>20)


if(age>20):
    print("I am an adult")
    print("i CAN VOTE")
    print("I CAN WORK ")

print("outside condition")

def calculator_func(input1,input2, operator):
    result=None
    if(operator=="+"):
        result=input1+input2
    elif(operator=="-"):
        result=input1-input2
    elif(operator=="*"):
        result=input1*input2
    elif(operator=="/"):
        result=input1/input2
    elif(operator=="+"):
        result=input1*input2
    else: 
        print("invalid input/invalid operator")
    return [1,2,3,4,5,6]


    

print(f"this is from outside function{calculator_func(100,400,"+")}")

def palindrome (input1):
    value=str(input1)
    reverse=value[::-1]
    print(reverse)
    if(value==reverse):
        print("is a palindrom")
    else:
        print("not a palindrome")
    

palindrome(121)

test="myString"
print(test.capitalize())




class planet:
#__keyword__
    def __init__(self,name, distanceFromSun,radius):
        self.name=name
        self.distanceFromSun=distanceFromSun
        self.radius=radius
    
    def rotate(self):
        print(f"My planet whos name is {self.name} is rotatting")
    
    def revolve(self):
        print(f"my planet whos radius is {self.radius} is revolving arounf the sun")




earth=planet("earth",500,6400)
mercury=planet("mercury", 200, 2000)
venus=planet(" venus",700, 7800)

earth.revolve()
mercury.revolve()
venus.revolve()

print(earth)
print(mercury)
print(venus)

print(earth.name)
print(mercury.name)
print(venus.name)

earth.revolve()
mercury.revolve()
venus.revolve()


class car:
    def __init__(self):
        print("this my car creation")

baleno=car()