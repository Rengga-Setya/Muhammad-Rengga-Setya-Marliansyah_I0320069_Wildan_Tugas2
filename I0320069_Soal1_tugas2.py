#MUHAMMAD RENGGA SETYA MARLIANSYAH
#NIM I0320069
#KELAS B
#SOAL LATIHAN NOMOR 1

def persegi_panjang():
    while True:
        try:
            p = int(input("Masukkan Nilai Panjang : "))
            l = int(input("Masukkan Nilai Lebar : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = p * l
            keliling    = 2 * (p + l)
            hasil       = [luas, keliling]
        break
    return hasil

def lingkaran():
    while True:
        try:
            r = int(input("Masukkan Nilai Jari-Jari : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            if r % 7 == 0:
                luas        = 22 / 7 * r * r
                keliling    = 2 * (22 / 7 * r)
                hasil       = [luas, keliling]
            else:
                luas        = 3.14 * r * r
                keliling    = 2 * 3.14 * r
                hasil       = [luas, keliling]
        break
    return hasil

def kubus():
    while True:
        try:
            s = int(input("Masukan Nilai Sisi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas_permukaan    = 6 * s * s
            volume            = s * s * s
            hasil             = [luas_permukaan, volume]
        break
    return hasil

def celcius_farenheit():
    while True:
        try:
            c = int(input("Masukan Nilai Suhu Celcius : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            farenheit   = ((9 / 5 * c) + 32)
            hasil       = [farenheit]
        break
    return hasil

def reamur_kelvin():
    while True:
        try:
            r = int(input("Masukan Nilai Suhu Reamur :   "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            kelvin  = ((5 / 4 * r) + 273)
            hasil   = [kelvin]
        break
    return hasil

confirm = "y"
while confirm == "y":
    print("Pilih Fungsi Program")
    print("1. Persegi Panjang")
    print("2. Lingkaran")
    print("3. Kubus")
    print("4. Konversi Celcius ke Farenheit")
    print("5. Konversi Reamur ke Kelvin")

    pilihan = input("Masukkan Pilihan (1/2/3/4/5) : ")

    if pilihan == "1":
        hasil = persegi_panjang()

        print("Luas Persegi Panjang : {}".format(hasil[0]))
        print("Keliling Persegi Panjang : {}".format(hasil[1]))
    elif pilihan == "2":
        hasil = lingkaran()

        print("Luas Lingkaran : {}".format(hasil[0]))
        print("Keliling Lingkaran : {}".format(hasil[1]))
    elif pilihan == "3":
        hasil = kubus()

        print("Luas Permukaan Kubus : {}".format(hasil[0]))
        print("Volume Kubus : {}".format(hasil[1]))
    elif pilihan == "4":
        hasil = celcius_farenheit()

        print("Suhu Farenheit : {}".format(hasil[0]))
    elif pilihan == "5":
        hasil = reamur_kelvin()

        print("Suhu Kelvin : {}".format(hasil[0]))
    else:
        print("Input Tidak Valid")

    confirm = input("Mulai Program Kembali? (Ya : y, Tidak : t) : ")
    if confirm == "t":
        break
    elif confirm == "y":
        continue
    else:
        print("Input Tidak Valid")

print("Terima kasih")