"ALAT PENGHITNG ANGKA GANJIL DAN GENAP "

"INPUT ANGKA"
X = int(input("Masukkan Angka : "))

while True:
    print("\n=== PENGECEKAN GANJIL / GENAP ===")
    print("Ketik 'q' untuk keluar dari program.")
 # Tombol keluar
    if X .lower() == "q":
        print("Program selesai. Terima kasih!")
        break

"LOGIKA PENGHITUNGAN"
if X % 2 == 0:
    print("Angka", X, "Termasuk Bilangan Genap")
"UNTUK CODINGAN DIATAS UNTUK MENENTUKAN ANGKA GENAP YANG HABIS DI BAGI 2"
if X % 2 != 0:
    print("Angka", X, "Termasuk Bilangan Ganjil")
" UNTUK CODINGAN DIATAS UNTUK MENENTUKAN ANGKA GANJIL YANG TIDAK HABIS DI BAGI 2 "

except ValueError:
print("Input tidak valid! Masukkan angka atau 'q' untuk keluar.")
