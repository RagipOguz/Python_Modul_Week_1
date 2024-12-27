#soru1_cevabi

for x in range(0,11):
    print(x)


#soru2_cevabi

sayi=int(input("bir sayi girin:"))
print("cift sayilar:")
for i in range(sayi+1):
    if i % 2 ==0:
        print(i)

#while 
sayi=int(input("bir sayi girin:"))
print("cift sayilar:")
x=0
while x<=sayi:
    if x%2==0:
        print(x)
    x+=1


#soru3_cevabi

sayi1=int(input("bir baslangic degeri girin:"))
sayi2=int(input("bir bitis degeri girin:"))
for x in range (sayi1,sayi2+1):
    print(x)


#soru4_Oneven/even getal bepalen(tek/cift sayi belirleme)

sayi = int(input("Voer alstublieft een nummer in(luften bir sayi giriniz): "))
if sayi/2 != 0:
    print(sayi,"is een oneven getal(tek bir sayidir)" )
else:
    print(sayi, "is een even getal(bir cift sayidir)")


#soru5_Faculteitsberekening(faktoriyelhesaplama)

sayi=int(input("Voer alstublieft het getal in waarvan u de faculteit wilt berekenen(Lutfen faktoriyelini hesaplamak istediginiz sayiyi girin):"))
import math
print("Het factorial van het ingevoerde getal(girdiginiz sayinin faktoriyeli):", math.factorial(sayi))


#soru6_Priemgetal berekening(asal sayi hesaplama)

def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, n):
        if n % i == 0:  
            return False
    return True  


sayi = int(input("Voer alstublieft een getal in(Lutfen bir sayi giriniz):"))
if is_prime(sayi):
    print(f"{sayi} is een priemgetal(bir asal sayidir).")
else:
    print(f"{sayi} is geen priemgetal(bir asal sayi degildir).")


#7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?
""""
limit = int(input("Bir limit giriniz: "))
fib_seq = [0,1]
while True:
    next_fib = int(fib_seq[-1]+fib_seq[-2])
    if next_fib>limit:
        break
    fib_seq.append(next_fib)
print(fib_seq)
"""

#8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.
"""
word = input("Bir kelime giriniz: ")
reverse_word = print(word[::-1])
"""

#9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

kelime = input("Bir kelime giriniz: ")
kelime = kelime.replace(" ", "").lower()
pal_kelime = kelime[::-1]
if kelime == pal_kelime:
    print("Palindrom")
else:
    print("Palindrom değil")


# Soru10_cevabi:
agirlik = float(input("Kilonuzu giriniz: "))
katman = float(input("Boyunuzu giriniz: "))
vki = agirlik / (katman** 2)
print("Vücut Kitle İndeksiniz:", round(vki, 2))
if vki < 25 :
    print("Kilonuzyetersiz.")
elif vki < 30:
    print("Normal kilodasınız.")
elif vki < 40:
    print("Fazla kilolusunuz.")
else:
    print("Obezsiniz.")


# Soru11_cevabi:
sayi1 = int(input("İlk sayiyi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))
enBuyuk = max(sayi1, sayi2, sayi3)
print("En büyük sayı:", enBuyuk)


#soru12_cevabi:
ders_sonucu = " "
dersler=["Matematik", "Coğrafya", "Kimya", "Biyoloji"]
for i in dersler:
    vize = float(input(f"{i} için Vize: "))
    final = float(input(f"{i} için Final: "))
    ort = (vize * 0.4) + (final * 0.6)
    if ort >= 50:
        sonuç = "Başarılı"
    else:
        sonuç = "Başarısız"
    ders_sonucu += f"Ders {i} - ortalama: {ort:.2f}, Durum: {sonuç}\n"
print(ders_sonucu)
