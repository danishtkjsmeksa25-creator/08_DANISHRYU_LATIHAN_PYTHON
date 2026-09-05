def menu():
    print("==============================")
    print("         MENU PROGRAM")
    print("==============================")
    print("1. Bangun Datar")
    print("2. Bilangan Ganjil / Genap")
    print("3. Keluar")
    print("==============================")


def bangun_datar():
    print("\n=== BANGUN DATAR ===")
    print("1. Persegi Panjang")
    print("2. Segitiga")

    
def ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


def hitung_luas_persegi(panjang, lebar):
    return panjang * lebar


def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2