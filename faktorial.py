def hitung_faktorial(a):
    hasil=1
    for i in range(1,a+1):
        hasil=hasil*i
        print (i)
    return hasil

n=5
print ("nilai n=",n)
print("Hasil faktorial adalah",hitung_faktorial(n))