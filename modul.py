"Modul Matematika"

print("<=== PROGRAM PENGECEKAN BILANGAN MATEMATIKA ===>")

while True:
    # Menu unuk memilih opsi
    print("\n1. Cek Bilangan Prima")
    print("2. Cek Ganjil / Genap")
    print("3. Keluar")

    #input dari user untuk memilih menu
    pilihan = input("Pilih menu: ")

    # Mengecek pilihan user (1, 2, atau 3)
    if pilihan == "1":
        angka = int(input("Masukkan angka: "))

        if angka < 2:
            print(f"{angka} bukan bilangan prima")
        else:
            prima = True

            for i in range(2, angka):
                if angka % i == 0:
                    prima = False
                    break

            if prima:
                print(f"{angka} adalah bilangan prima")
            else:
                print(f"{angka} bukan bilangan prima")

    #Fungsi untuk mengecek bilangan ganjil/genap (saat user memilih opsi 2)
    elif pilihan == "2":
        angka = int(input("Masukkan angka: "))

        if angka % 2 == 0:
            print(f"{angka} adalah bilangan genap")
        else:
            print(f"{angka} adalah bilangan ganjil")

#command user untuk keluar dari program (saat user memilih opsi 3)
    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia!")