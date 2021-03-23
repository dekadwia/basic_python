buah = ["apel", "pisang", "semnagka", "jeruk"]
for i in buah :
    print(i)

#akan me-loop sebanyak 4 kali dalam list
buah = ["apel", "pisang", "semnagka", "jeruk"]
for i in buah :
    print(buah)

#looping for range
for i in range(6) :
    print(i)

'''
range(x1, x2, x3)
x1 =start
x2 =stop
x3 = step
'''

for i in range(0,11,2):
    print(i)

#Looping for string
buah = ["apel", "pisang", "semnagka", "jeruk"]
x = 0
for i in buah :
    x = x+1
    print(i)
    
#Menginput ke list kosong  dengan loop berdasarkan jumlah data yg diinput
cus_name = []
cus_age = []

banyak_data = int(input("Banyak data yg diinput: "))
for input_data in range(banyak_data):
    input_nama = str(input("Nama Customer : "))
    input_umur = int(input("Umur Customer : "))
    print("--------------------------------")
    cus_name.append(input_nama)
    cus_age.append(input_umur)
print(cus_name)
print(cus_age)

#Subset nama customer dan customer age dengan loop
for hasil_data in range(len(cus_name)):
    print("------------------------------")
    print(hasil_data)
    print("Nama Customer : {}".format(cus_name[hasil_data]))
    print("Umur Customer : {}".format(cus_age[hasil_data]))

#While Loop
x = 0
while x <=5 :
    print(x)
    x = x + 1

#For Loop dengan continue
for i in range(1,11):
    if i == 5:
        continue
    print(i)
 #For loop untuk memisahakan buah semangak   
buah = ["apel", "pisang", "semangka", "jeruk", "naga", "nangka"]
buah_mahal=[]
for i in buah:
    if i == "semangka":
        buah_mahal.append(i)
        continue
    print(i)
print(buah_mahal)
    
#For loop dengan logic dan continue function
buah = ["apel", "pisang", "semangka", "jeruk", "naga", "nangka"]
for i in buah:
    if i == "semangka":
        print("Buah ini paling besar")
        continue
    print(i)
    
#for loop dengan fungsi break
buah = ["apel", "pisang", "semangka", "jeruk", "naga", "nangka"]
for i in buah:
    if i == "semangka":
        print("Buah ini paling besar")
        break
    print(i)


#for loop dengan fungsi break dan continue
buah = ["apel", "pisang", "semangka", "jeruk", "naga", "nangka"]
for i in buah:
    if i == "semangka":
        print("Buah ini paling besar")
        continue
    if i == "naga":
        break
    print(i)

#Nested Loop flow
for i in range(2):
    for j in range(3):
        print("i:{},j:{}".format(i,j), end = " ") #fungsi end akan membuat 1 row saja
    print() # Membuat menjadi 2 row
    
for i in range(11):
    for i2 in range(i):
        print("*", end = " ")
    print()

for i in range(11):
    for i2 in range(i):
        print(i2, end = " ")
    print()
    
for i in range(11):
    for i2 in range(i):
        print(i, end = " ")
    print()
    
name = ["Ismail", "Ali", "Elif"]
car = ["Mercedes","Porsche", "Hyundai"]
number = (1,2,3)
for names in name :
    for cars in car :
        for numbers in number :
            print(f"{names} has {numbers} of{cars}")

#Try
try :
    angka = int(input("Masukkan Angka :"))
    print(angka)
except ValueError:
    print("yang anda masukkan bukan angka!")
else :
    print("Program Sukses!")
finally :
    print("Program Selesai")