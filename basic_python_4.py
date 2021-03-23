#Dictionaries
name_age ={
    "Name"      : 'Deka',
    "Age"       : "26",
    'Status'    : "Double",
    'Hobby'     : 'Main Python'
    }
for i in name_age :
    print(f"Data {i} berisi {name_age[i]}")
    
for i,b in name_age.items() :
    print(f"Data {i}, berisi {b}")
    
#Function
def fungsi_saya ():
    nama = str(input("Nama Anda :"))
    print(f"nama saya {nama}")
fungsi_saya()

#Function with default
def fungsi_saya(nama):
    print(f"nama saya {nama}")
fungsi_saya("Deka")

def fungsi_saya(nama, umur, pend) :
    print(f"Nama saya {nama} berumur {umur} tahun dan pendidikan terakhir {pend}")
fungsi_saya("deka", 25, "S-1")

def fungsi_saya(nama= "kosong", umur = "kosong", pend = "kosong") :
    print(f"Nama saya {nama} berumur {umur} tahun dan pendidikan terakhir {pend}")
fungsi_saya()

#fungsi Jika urutan acak
def fungsi_saya(nama, umur, pend) :
    print(f"Nama saya {nama} berumur {umur} tahun dan pendidikan terakhir {pend}")
fungsi_saya(pend = 'S2', nama ='Deka', umur =25)

#Combine Function dengan break
def fungsi_saya():
    x = 0
    while True:
        x = x+1
        if x == 50 :
            break
        print(x)
    print("selesai")
fungsi_saya()

def fungsi_saya():
    x = 0
    while True:
        x = x+1
        if x == 50 :
            break
        print(x)
    print("selesai")
    print("sampai jumpa")
fungsi_saya()
print()
print("Coba-Coba")

#Return Function
def fungsi_saya():
    x = 0
    while True:
        x = x+1
        if x == 51 :
            return #Fungsi return akan mengembalikan ke fungsi awalnya, jadi print selesai dan sampai jumpa dilewat
        print(x)
    print("selesai")
    print("sampai jumpa")
fungsi_saya()
print()
print("Coba-Coba")

def fungsi_saya (nama) :
    return 5*10
print(fungsi_saya('Deka'))

def fungsi_saya (nama) :
    return nama
print(fungsi_saya('Deka'))

def fungsi_saya1():
    print("Ini adalah Fungsi luar")
    def fungsi_saya2() :
        print("Ini aalah fungsi dalam")
fungsi_saya1()

def fungsi_saya1():
    print("Ini adalah Fungsi luar")
    def fungsi_saya2() :
        print("Ini aalah fungsi dalam")
    fungsi_saya2()
fungsi_saya1()

def fungsi_saya1():
    print("Ini adalah Fungsi luar")
    def fungsi_saya2() :
        print("Ini aalah fungsi dalam")
    return fungsi_saya2()
fungsi_saya1()

def fungsi_saya1():
    print("Ini adalah Fungsi luar")
    def fungsi_saya2() :
        return 5*20
    return fungsi_saya2()
fungsi_saya1()

def fungsi_saya1():
    print("Ini adalah Fungsi luar")
    def fungsi_saya2() :
        print(5*10)
    fungsi_saya2()
    return fungsi_saya2()
fungsi_saya1()

def fungsi_saya1():
    print("Ini adalah Fungsi luar")
    def fungsi_saya2() :
       return 5*10
    return fungsi_saya2()
fungsi_saya1()
print(fungsi_saya1())

def fungsi_saya1():
    print("Ini adalah Fungsi luar")
    def fungsi_saya2() :
       return 5*10
    return fungsi_saya2()
fungsi_saya1()

#Example for assignment
nama = []
def ambil_nama():
    input_nama = str(input("Nama Customer :"))
    nama.append(input_nama)
    print("Done!")
while True : 
    print("1. Simpan Nama")
    print("2. Tampilkan Nama")
    print("3. Keluar")
    inputan = int(input("Pilih Menu :"))
    if inputan == 1:
        ambil_nama()
    elif inputan ==2:
        for i in nama :
            print(i)
    elif inputan ==3:
        break
    else :
        pass