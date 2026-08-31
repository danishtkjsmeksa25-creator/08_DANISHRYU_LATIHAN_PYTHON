import bangundatar

print(bangundatar.__file__)
print(hasattr(bangundatar, "hitung_luas_persegi"))

x = int(input("Masukkan panjang: "))
y = int(input("Masukkan lebar: "))

print(f"Luas Persegi Panjang: {bangundatar.hitung_luas_persegi(x, y)}")

alas = int(input("Masukkan alas: "))
tinggi = int(input("Masukkan tinggi: "))

print(f"Luas Segitiga: {bangundatar.hitung_luas_segitiga(alas, tinggi)}")