def word():
    me = "Mau apa kau? \n"
    print (me + "Mixue...")

word() # Memanggil fungsi word
print("+++====================+++")
print("\n")

# FUNCTION GLOBAL
def myfunc():
    z = "emang bisa?? "
    print ("pakek bahasa py? " + z)

    x = "Bisa dong!"
    print (x)

myfunc() # Memanggil fungsi myfunc



# penerapan input dan juga fungsi untuk aritmatika
number = int(input("Masukkan angka: "))
def pangkat(number):
    return number ** 2

hasil = pangkat(number)
print(f"Hasil pangkat dari {number} adalah {hasil}")
