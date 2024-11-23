# Definisi fungsi

def aritmatika():
    #input pengguna
    a = int(input("Masukan Angka pertama : "))
    b = int(input("Masukan Angka kedua : "))

    #proses aritmatika
    hslTambah = a + b
    hslkurang = a - b
    hslbagi = a / b
    #mengembalikan nilai dari proses
    return hslTambah, hslkurang, hslbagi

# Memanggil fungsi
hslTambah, hslkurang, hslbagi = aritmatika()

# Menampilkan hasil
print (f"Hasil dari penjumlahan : {hslTambah}")
print (f"Hasil dari pengurangan : {hslkurang}")
print (f"Hasil dari pembagian : {hslbagi}")


