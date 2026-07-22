for i in range(0,10):
    print(i)
    print("this is my  iteration sequence")

result=0
for i in range(0,1001):
    result=result+i
    print(f"this is at iterattion {i} and result is {result}")


movie=10




result=0
for i in range(1000,2001):
    result=result+i
    print(f"this is at iterattion {i} and result is {result}")



def sumOfNumbers(input1=300,input2=600):
    """ this is a sum of inputs method and this waas created on 16-07-26"""
    #this is also a comment
    print(f"the sum of the given inputs is {input1+input2} ")
    print(f"multiplication of the givnen inputs is {input1*input2}")

sumOfNumbers(3)
sumOfNumbers(5,20)
sumOfNumbers(10,30)
sumOfNumbers()


def calculator(input1, input2, operator):
    final=0
    if(operator=="+"):
        print(f"this is addition {input1+input2}")
        final=input1+input2
    elif(operator=="-"):
        print(f"this is substraction {input1-input2}")
        final=input1-input2
    elif(operator=="*"):
        print(f"this is multiplication {input1*input2}")
        final=input1*input2
    elif(operator=="/"):
        print(f"this is division {input1/input2}")
        final=input1/input2
    else:
        print("please provide a valid input for operation")
    return final

input1=int(input("please enter input1"))
input2=int(input("please enter input2"))
operator=(input("please enter an operation +,-,/,*"))

result=calculator(input1,input2, operator)
print(result)


def is_palindrom(value):
    reverse=value[::-1]
    print(f"reversed value is {reverse}")
    print(f"original value is {value}")
    return reverse==value

print(is_palindrom("python"))
print(is_palindrom("madam"))

"test string"
'test string'
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)

while movie>0:
   print("I am shopping")
   break
   movie=movie-1