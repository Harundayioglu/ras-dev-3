yazı=str(input("Bir string girin: "))
def büyük_küçük(str):
    büyük=0
    küçük=0
    for harf in str:
        if harf.isupper():
            büyük+=1

        if harf.islower():
            küçük+=1

    return(f"""Büyük harf sayısı: {büyük}
Küçük harf sayısı: {küçük}""")



print(büyük_küçük(yazı))