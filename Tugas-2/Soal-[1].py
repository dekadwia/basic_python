#Example for assignment
nama = []
telepon = []
def nama_telepon():
    input_nama = str(input("Nama :"))
    input_telepon = int(input("No. Telepon :"))
    nama.append(input_nama)
    telepon.append(input_telepon)
    print("Kontak berhasil ditambahkan")
while True : 
    print('Selamat datang!')
    print('--- Menu---')
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    inputan = int(input("Pilih menu :"))
    if inputan == 1:
        print("Daftar Kontak : ")
        for hasil_data in range(len(nama)):
            print("------------------------------")
            print(hasil_data+1)
            print("Nama        : {}".format(nama[hasil_data]))
            print("No. Telepon : {}".format(telepon[hasil_data]))
    elif inputan ==2:
        nama_telepon()
    elif inputan ==3:
        print('Program selesai, sampai jumpa!')
        break
    else :
        print('Menu tidak tersedia')
        pass
