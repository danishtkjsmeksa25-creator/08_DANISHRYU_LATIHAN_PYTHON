def Mencari_Bilangan_Prima(x):
    bilangan_prima = []

    for angka in range(2, x + 1):
        prima = True

        for i in range(2, angka):
            if angka % i == 0:
                prima = False
                break

        if prima:
            bilangan_prima.append(angka)

    return bilangan_prima


def Cek_Ganjil_Genap(n):
    if n % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
    
def hitung_luas_persegi(panjang, lebar):
        return panjang * lebar

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi