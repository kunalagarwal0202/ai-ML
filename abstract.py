from abc import ABC, abstractmethod
import math
#maruthi susuki manufacturing desgin unit
class car(ABC):
    @abstractmethod
    def engine(self):
       pass
    
    @abstractmethod
    def stereo(self):
        pass

    @abstractmethod
    def tyres(self):
        pass

    def mirror(self):
        print("this is addition of mirrors")

class test:
     def __init__(self):
         print("test constructor")

     def engine(self):
         print("this is from the test functionality of the engine")

class petrolCar(test):
 
    def __init__(self,name):
        self.name=name
        print("this is constructor of petrol car")
        super().__init__()


    def engine(self):
        print("This is a petrol car functionality")
        #super().engine()
    
    def stereo(self):
        print("We have a JBL Company Stereo")

    def tyres(self):
        print("we have ceat tyres")

    def ignition(self):
        print("we are starting the car")
    
class dieselCar(car):
    def engine(self):
        print("We have diesel enginer here")
    def stereo(self):
        print("we have bose stereo")
    def tyres(self):
        print("we have michelene tyres installed")
    def ignition(self):
        print("this is diesel car ignition")
    
class electricCar(car):
    def engine(self):
        print("this a electic engine")
    def tyres(self):
        print("we have MRF Tyres")
    def startButton(self):
        print("please start the car with the button")
    def stereo(self):
        print("stereo in eelctric car")
    
    def mirror(self):
        print("these are electic mirrros")

balenoPetrol=petrolCar("balenoPetrol")
balenoDiesel=dieselCar()
balenoElectric=electricCar()

balenoDiesel.engine()
balenoPetrol.engine()
balenoElectric.engine()
balenoDiesel.ignition()
balenoElectric.startButton()
balenoElectric.stereo()
balenoDiesel.mirror()
balenoElectric.mirror()


balenoPetrol.engine()
balenoDiesel.engine()

def draw (radius):
    print(f"area{math.pi*radius*radius}")
    return 5

def draw (input1, input2):
    print(f"area {input1*input2}")
    return "string"


def area(input1, input2=10):
    print(f"area {input1*input2}")


draw(4,6)
draw(5,9)

test=test()
petrol=petrolCar("baleno")
test.engine()
petrol.engine()

area(10)
area(10,20)






try:
    input1=int(input("Please provide a numerical input"))
    input2=int(input("Please provide a numerical input"))
    print(input1/input2)
    raise ZeroDivisionError


except Exception as e:
    print("please verify inputs, something is wrong")
    print(e)
except ZeroDivisionError:
    print("please change your input to non zero")
except TypeError:
    print("please provide numbercal inputs only")
finally:
    print("all closing or safe implementation")




print("test out of try and except")



class InsufficientbalanceException(Exception):
    def __init__(self):
        super().__init__()
        print("banking excpetion")


def withdraw(amount):
    if(amount>1000):
        raise InsufficientbalanceException
    if(amount<1000):
        updated= 1000-amount
        print(f"amount withdrawn, updated balance is: {updated}")

try:
   withdraw(1500)
except InsufficientbalanceException:
    print("sufficent balance not available")


    math
    abc
    
