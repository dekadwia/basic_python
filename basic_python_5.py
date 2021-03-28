#Create own module
import module_saya
module_saya.greeting("Deka")

#create abbreviation for simple call
import module_saya as ms
ms.greeting("Deka")
ms.intro("Deka")

#Specific import greeting form module saya
from module_saya import greeting
greeting("Deka")

#Import 2 module in one time from module saya
from module_saya import greeting, intro
greeting("Deka")
intro("Deka")

#Import all contain from module_saya
from module_saya import *
greeting("Deka")
intro('Deka')
bye("deka")

#Try import module math from python
import math 
print(math.pi)

#Another using of math module
import math
print(math.floor(8.4))
print(math.pow(9,2)) #return to float
print(9**2) #return integer

#Make a simple call from math module
import math as m
print(m.floor(8.4))
print(m.pow(9,2)) #return to float
print(9**2) #return integer

#Import 2 module in one time from math module
from math import floor, pow
print(floor(8.4))
print(pow(8,2))

#Import datetime
import datetime
print(datetime.datetime.now())
print(type(datetime.datetime.now()))

#to create new file. file automatically save in working directory that we set
file = open("test.txt", "x")
file.close()

#write the contain of the file
file = open("test.txt","w")
file.write("Halo! ini adalah test")
file.close()

#Append new contain to the file
file = open("test.txt","a")
file.write("test 123\n") #Make new line
file.close()

#Read the file
file = open("test.txt","r")
print(file.read())
file.close()

#Read per line in the file
file = open("test.txt","r")
print(file.readline())
file.close()

#Read per line in the file and subset 3 first letter
file = open("test.txt","r")
print(file.readline(3))
file.close()

#Another way to open the file
with open("test.txt","r", encoding="utf-8") as file_saya:
    print(file_saya.read())
    
#Delete File
import os
os.remove("test.txt")
    
#Build programe to create and delete file
import os
while True :
    print("1. Create and then add the contain of file")
    print("2. Delete File")
    options = int(input('Choose the option: '))
    if options == 1:
        with open("test.txt", "w") as my_file:
            file_contain = input("Contain of the file: ")
            my_file.write(file_contain)
    if options == 2:
        os.remove("test.txt")

#Import module if the module is not in the same directory (module located in the back file)
import sys
sys.path.append('C:\\Users\\Administrator\\Desktop\\basic-python\\module')
from module_saya import greeting, intro
greeting('deka') 
intro('deka')        

#Import module if the module is not in the same directory (module located in front of the file)
from module.modul_saya import greeting, intro
greeting("deka")
intro("deka")

#Exercise
nama_anggota = []
file_anggota = open("nama.txt", "r")
for nama_nama in file_anggota:
    nama_bersih = nama_nama.replace("\n", "")
    nama_anggota.append(nama_nama)
print(nama_anggota)
file_anggota.close()