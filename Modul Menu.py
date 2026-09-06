import Bilangan

while True:
    print("\n==============================")
    print("        MENU UTAMA")
    print("==============================")
    print("1. Bangun Datar")
    print("2. Bilangan Ganjil / Genap")
    print("3. Keluar")
    print("==============================")

    pilihan = input("Pilih menu [1-3]: ")

    if pilihan == "1":
        while True:
            print("\n------------------------------")
            print("        BANGUN DATAR")
            print("------------------------------")
            print("1. Luas Persegi Panjang")
            print("2. Luas Segitiga")
            print("3. Kembali ke Menu Utama")
            print("------------------------------")

            pilih_bangun = input("Pilih menu [1-3]: ")

            if pilih_bangun == "1":
                panjang = int(input("Masukkan panjang: "))
                lebar = int(input("Masukkan lebar: "))

                hasil = Bilangan.hitung_luas_persegi(panjang, lebar)
                print(f"Luas Persegi Panjang: {hasil}")

            elif pilih_bangun == "2":
                alas = int(input("Masukkan alas: "))
                tinggi = int(input("Masukkan tinggi: "))

                hasil = Bilangan.hitung_luas_segitiga(alas, tinggi)
                print(f"Luas Segitiga: {hasil}")

            elif pilih_bangun == "3":
                break

            else:
                print("Pilihan tidak valid!")

    elif pilihan == "2":
        print("\n------------------------------")
        print("     BILANGAN GANJIL / GENAP")
        print("------------------------------")

        angka = int(input("Masukkan bilangan: "))

        if angka % 2 == 0:
            print(f"{angka} adalah bilangan GENAP")
        else:
            print(f"{angka} adalah bilangan GANJIL")

    elif pilihan == "3":
        print("\nProgram selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih 1-3.")
