import Bilangan

print(Bilangan.__file__)
print(hasattr(Bilangan, "Cek_Ganjil_Genap"))

# Input bilangan prima
x = int(input("Masukkan angka: "))

print(f"Bilangan prima dari 1 sampai {x} adalah: {Bilangan.Mencari_Bilangan_Prima(x)}")

# Input ganjil genap
x = int(input("Masukkan angka: "))

print(f"{x} adalah bilangan {Bilangan.Cek_Ganjil_Genap(x)}")
