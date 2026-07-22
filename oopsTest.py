class planet:
    def __init__(self, name="test", distanceFromSun=100, radius=50):
        self.firstname=name
        self.distanceFromSun=distanceFromSun
        self.radius=radius

    def revolve(self):
        print("this is revolve funtion within planet object")
        print(self.distanceFromSun, " for the object", self.firstname)

    def rotate(self):
        print("this is the rotate function from planet class")


    def details(self, test):
        print("this is the details funtion of class planet,  i will now be provdiing with details of the object")
        print(f"this is the name of the planet{self.firstname}")
        print(f"this is the distance from sun {self.distanceFromSun}")
        print(f"this is the test inpur provided by the user{test}")

earth=planet("earth", 65000, 6500)
earth.details("test")
print("--------------------------------------------------------------")
venus=planet("venus","7600","4500")
venus.details("test2")


class test:
    def __init__(self):
        pass
    
    def funcTest(self):
        print("this is a test object")


test11=test()
test11.funcTest()

result=0

for i in range(1,10):
    result=result+i  # 0+1   #1+2=3