# script global

y = "Python adalah "

def myfunc():
    y = "python itu "
    print(y + " mudah broo!")

myfunc()
print(y + "sebuah bahasa pemrograman yg mudah")



def myfunc():
  global x
  x = "fantastic" 

myfunc()

print("Python is " + x)


# coba disini yak

z = "kalo emang bisa"
def myfunc():
    z = "emang bisa?? "
    print ("pakek bahasa py? " + z)

myfunc()
print ("coba aja lah!!! " + z)

