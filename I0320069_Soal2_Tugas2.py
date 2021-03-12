#Sistem Metrik
def bmi_metrik():
    nama = str(input("Masukan Nama Anda = "))
    umur = int(input("Masukan Umur Anda = "))
    kelamin = str(input("Masukan Jenis Kelamin Anda = "))
    berat = float(input("Masukan Berat Badan (KG) : "))
    tinggi = float(input("Masukan Tinggi Badan Anda (M) : "))
    bmi = berat * (tinggi ** 2)
    print((nama),(umur),("tahun"), (kelamin))
    print("Anda memiliki BMI = ", bmi, " kg/m2")
    if bmi <= 18.5:
        print("Anda memiliki berat badan KURANG")
        bmi_kalkulator()
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Kamu memiliki berat badan IDEAL")
        bmi_kalkulator()
    elif bmi >= 25 and bmi <= 29.9:
        print("Anda memiliki OBESITAS RINGAN")
        bmi_kalkulator()
    else:
        print("Anda memiliki OBESITAS BERAT")
        response = input("Mulai lagi? (Ya : y, Tidak : t) : ")
        if response == "y":
            bmi_kalkulator()
        elif response == "t":
            print("===== Terima Kasih =====")
            exit()
#Sistem Imperial
def bmi_imperial():
    nama = str(input("Masukan Nama Anda = "))
    umur = int(input("Masukan Umur Anda = "))
    kelamin = str(input("Masukan Jenis Kelamin Anda = "))
    berat_kg = float(input("Masukan Berat Badan (KG) : "))
    tinggi_cm = float(input("Masukan Tinggi Badan Anda (M) : "))
    berat = berat_kg * 2.2
    tinggi = tinggi_cm / 0.0254
    bmi = (tinggi * 703) / (berat ** 2)
    print((nama),(umur),("tahun"), (kelamin))
    print("Berat Badan = ", berat, "lbs")
    print("Tinggi Badan = ", tinggi, "inches")
    print("Anda memiliki BMI = ", bmi, "lbs/inches2")
    if bmi <= 18.5:
        print("Anda memiliki berat badan KURANG")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Kamu memiliki berat badan IDEAL")
        bmi_kalkulator()
    elif bmi >= 25 and bmi <= 29.9:
        print("Anda memiliki OBESITAS RINGAN")
        bmi_kalkulator()
    else:
        print("Anda memiliki OBESITAS BERAT")
        response = input("Mulai lagi? (Ya : y, Tidak : t) : ")
        if response == "y":
            bmi_kalkulator()
        elif response == "t":
            print("===== Terima Kasih =====")
            exit()
def bmi_kalkulator():
    print("""
    ========== KALKULATOR BMI ==========
    """)
    response = input(
        "Metrik (Kg/M) / Imperial (lbs/inchi)? : ")
    if response == 'metrik':
        print("---Anda menggunakan sistem metrik---")
        bmi_metrik()
    elif response == 'imperial':
        print("---Anda menggunakan sistem imperial---")
        return bmi_imperial()
    else:
        print("Input tidak valid")
        bmi_kalkulator()
bmi_kalkulator()