"ALAT PENGHITNG ANGKA GANJIL DAN GENAP "
while True:
    print("\n=== PENGECEKAN GANJIL / GENAP ===")
    print("Ketik 'q' untuk keluar dari program.")

    X = input("Masukkan Angka : ")

 # Tombol keluar
    if X .lower() == "q":
        print("Program selesai. Terima kasih!")
        break

    try:
        x = int(X)
        if x % 2 == 0:
            print("Angka", x, "Termasuk Bilangan Genap")
        else:
            print("Angka", x, "Termasuk Bilangan Ganjil")
            
    except ValueError:
        print("Input tidak valid! Masukkan angka atau 'q' untuk keluar.")