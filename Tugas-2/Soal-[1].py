#Example for assignment
nama = []
telepon = []
def nama_telepon():
    input_nama = str(input("Nama :"))
    input_telepon = int(input("No. Telepon :"))
    nama.append(input_nama)
    telepon.append(input_telepon)
    print("Kontak Berhasil ditambahkan!")
while True : 
    print('Selamat datang!')
    print('--- Menu---')
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    inputan = int(input("Pilih menu :"))
    if inputan == 1:
        print("Daftar Kontak : ")
        for i in nama :
            print(f"Nama : {i}, No.telp : {i2}")
        for i2 in telepon:
            print(f"No. Telepon : {i2}")
    elif inputan ==2:
        nama_telepon()
    elif inputan ==3:
        print('Program selesai, sampai jumpa!')
        break
    else :
        print('Menu tidak tersedia')
        pass