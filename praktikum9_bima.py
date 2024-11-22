print ()
print ('## nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    konfersi=(celcius*9/5)+32
    return konfersi
print (celcius_ke_fahrenheit(0))
print (celcius_ke_fahrenheit(5))

print ('## nomor 2 ##')
def ganjil_genap (bilangan):
    penentu=bilangan % 2 == 0
    return penentu
print(ganjil_genap(4))
print(ganjil_genap(3))

print ("## nomor 3  ##")
def nilai(keterangan):
    if keterangan >=80:
        print ('lulus')
    elif keterangan <=60:
        print ('gagal')
    else:
        print('ga ada nilai')
print (nilai(80))

print ("## nomor 4 ##")
def bilangan_ganjil (bilangan):
    return[i for i in range(1,bilangan,2)]
print (bilangan_ganjil (20))