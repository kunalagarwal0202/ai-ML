from abc import ABC, abstractmethod
import math

class car(ABC):

    @abstractmethod
    def engine(self):
        print("test this is from abstarct method")

    @abstractmethod
    def stereo(self):
        pass
           
    def mirrors(self):
        print("This is mirror common functionality")

    def tyres(self, radius):
        print(f"all the functrionality of a tyre{radius}")





class PetrolCar(car):



    def engine(self):
       super().engine()

    def stereo(self):
        print("This is the stereo functionality of petrol car")

           
    def mirrors(self):
        print("This is mirror common petrol functionality")

    def tyres(self):
        print("test")
 


class dieselCar(car):
    def engine(self):
        print("This is a diesel car functionality")
    def stereo(self):
        print("This is the stereo functionality of diesel car")





balenoPetrol=PetrolCar()
balenoPetrol.engine()
balenoPetrol.stereo()
balenoPetrol.mirrors()
balenoDisel=dieselCar()
balenoDisel.engine()
balenoDisel.stereo()
balenoDisel.mirrors()



class shape:
    def draw(self,input1=0, input2=0):
        print(f"area{input1*input2}")

class circle(shape):
    def draw(self, input1=0, input2=0):
        print(f"area{math.pi*input2*input2}")

class rectangle(shape):
    def draw(self, input1=0, input2=0):
        return super().draw(input1, input2)

class square(shape):
    def draw(self, input1=0, input2=0):
        print(f"area{input2*input2}")


circlle=circle()
circlle.draw(0,9)

squaretest=square()
squaretest.draw(0,8)

rectangletest=rectangle()
rectangletest.draw(7,8)
