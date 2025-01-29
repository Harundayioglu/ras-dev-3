def toplama (num1,num2):
    sonuç=num1+num2
    return sonuç

def çıkarma (num1,num2):
    sonuç=num1-num2
    return sonuç
def çarpma (num1,num2):
    sonuç=num1*num2
    return sonuç
def bölme (num1,num2):
    sonuç=num1/num2
    return sonuç

while True:
    a = int(input("""Hesap Makinesi
    1. Toplama
    2. Çıkarma
    3. Çarpma
    4. Bölme
    5. Çıkış
    İşlem seçin: """))
    if a==5:
        print("Çıkış yapılıyor...")
        break

    d = float(input("Ilk sayıyı girin: "))
    c = float(input("Ikinci sayıyı girin: "))

    if a == 1:
        print(f"Sonuç: {toplama(d, c)}")
    if a == 2:
        print(f"Sonuç: {çıkarma(d, c)}")
    if a == 3:
        print(f"Sonuç: {çarpma(d, c)}")
    if a == 4:
        print(f"Sonuç: {bölme(d, c)}")
    else:
        print("Geçersiz işlem! Lütfen 1-5 arasında bir seçim yapın.")

