teori   = 70
praktek = 70
if teori >= 70 and praktek >= 70 :
    print("Selamat, anda lulus!")
elif teori >= 70 and praktek <70 :
    print("Anda harus mengulang ujian praktek.")
elif teori <70 and praktek >= 70 :
    print("Anda harus mengulang ujian teori.")
else :
    print("Anda harus mengulang ujian teori dan praktek.")