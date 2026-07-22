strTest="i love python"
print(strTest.capitalize())
print(strTest.upper())
print(strTest.lower())
print(strTest)
strTest=" i, l,o,v,e j,a,v,a "
strtest2="i love python"
print(strTest.replace("java", "go"))
print(strTest)
print(strTest.split(","))
print(strTest)
print(strTest.strip())

import string
testChar=input("provide a character")
print(string.ascii_letters)
if testChar in string.ascii_letters:
    print("this is an alphabet")
else:
    print("this is not an alphabet")


import random

password=""
for i in range(10):
    password=password+random.choice(string.ascii_letters)
    print(f"password is { password} and i value is {i}")
""" 
password=""
password=password+random=""+"u"="u"

password="u"
pass=pass+randon="u"+"e"=ue

password="ue"
pass=pass+randon=ue+C=ueC
"""


text="Hello!223 test uuu"

for i in text:
    print(i)

count=0

for i in range(10):
    count=count+1

print(count)

count=0
for i in text:
    count +=1
    if(i==" "):
        print(count)
        text= text[:count] + text[count].capitalize()+text[count+1:]
        print(text)

        


import tensorflow as tf
print(tf.__version__)
ann= tf.keras.models.Sequential()
print(ann)