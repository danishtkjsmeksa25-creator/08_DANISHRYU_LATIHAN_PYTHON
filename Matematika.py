import Bilangan

print(Bilangan.__file__)
print(hasattr(Bilangan, "Cek_Ganjil_Genap"))

# Input bilangan prima
x = int(input("Masukkan angka: "))

print(f"Bilangan prima dari 1 sampai {x} adalah: {Bilangan.Mencari_Bilangan_Prima(x)}")

# Input ganjil genap
x = int(input("Masukkan angka: "))

print(f"{x} adalah bilangan {Bilangan.Cek_Ganjil_Genap(x)}")

#input luas persegi panjang
panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan lebar: "))
print(f"Luas Persegi: {Bilangan.hitung_luas_persegi(panjang, lebar)}")

#input luas segitiga
alas = int(input("Masukkan alas: "))
tinggi = int(input("Masukkan tinggi: "))
print(f"Luas Segitiga: {Bilangan.hitung_luas_segitiga(alas, tinggi)}")
