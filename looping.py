for x in range(1,250):
    print(x)


angka = int(input("Masukkan sebuah angka: "))
if angka % 2 == 0:
    print(f"{angka} adalah angka genap.")
else:
    print(f"{angka} adalah angka ganjil.")


i = 1
while i <= 5:
    print(i)
    i += 2  # Tambahkan 1 ke nilai i setiap kali loop berjalan


buah = ["apel", "pisang", "jeruk", "mangga"]
for item in buah:
    print(item)


while True:
    data = input("Masukkan angka antara 1 hingga 10: ")
    try:
        angka = int(data)
        if 1 <= angka <= 10:
            print(f"Terima kasih! Anda telah memasukkan angka yang valid: {angka}")
            break
        else:
            print("Input tidak valid. Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

# Penjelasan:
# 1. Loop `while True` akan terus berjalan sampai kondisi `break` tercapai.
# 2. `try-except` digunakan untuk menangani input yang bukan angka.
# 3. `if 1 <= angka <= 10` mengecek apakah angka yang diinput berada dalam rentang yang valid.
# 4. Jika input valid, program akan mencetak pesan terima kasih dan keluar dari loop dengan `break`.
# 5. Jika input tidak valid, program akan mencetak pesan kesalahan dan meminta input lagi.
