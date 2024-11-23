def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b

def hitung(a, b):
    penjumlahan = tambah(a, b)
    perkalian = kali(a, b)
    print(f"Hasil penjumlahan: {penjumlahan}")
    print(f"Hasil perkalian: {perkalian}")

# Memanggil fungsi hitung
hitung(20, 40)


# FUNCTION GLOBAL
def myfunc():
    z = "emang bisa?? "
    print ("pakek bahasa py? " + z)


