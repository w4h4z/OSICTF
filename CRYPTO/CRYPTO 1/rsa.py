from Crypto.Util.number import *

flag=bytes_to_long(open("flag.txt","r").read())
p=getPrime(256)
q=getPrime(256)
e=0x10001
n=p*q
enc=pow(flag,e,n)
for i in range(0xff):
	enc-=i
calc1=p+q
calc2=pow(p+q,2)

print "equation 1 = ",calc2+2*p*q
print "equation 2 = ",calc1-2*q
print "n = ",n
print "e = ",e
print "enc = ",enc
