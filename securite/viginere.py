# chiffrement de viginere
def chiffrementViginere(cle,texte):
    texte = texte.upper()
    cle = cle.upper()
    str=""
    list = []
    chiffre = []
    for i in range(65,91):
        list.append(chr(i))
    j = 0
    i = 0
    while(j<len(texte)):
        if(i<len(cle)):
            chiffre.append(((ord(texte[j])+ord(cle[i]))%26)+65)
            i += 1
            j += 1
        else:
            i = 0
    print(chiffre)
    for i in chiffre:
       str+=chr(i)
    print(str)
    return str


#dechiffrement
def dechiffrementViginere(cle,texte):
    texte = texte.upper()
    cle = cle.upper()
    str = ""
    list = []
    chiffre = []
    for i in range(65, 91):
        list.append(chr(i))
    j = 0
    i = 0
    while (j < len(texte)):
        if (i < len(cle)):
            if((ord(texte[j])-ord(cle[i]))>=0):
                chiffre.append((ord(texte[j]) - ord(cle[i])) + 65)
            else:
                chiffre.append(26-(abs(ord(texte[j]) - ord(cle[i]))) + 65)
            i += 1
            j += 1
        else:
            i = 0
    print(chiffre)
    for i in chiffre:
        str += chr(i)
    print(str)
    return str

print("chiffrement")
chiffrementViginere("VIGENERE","EXAMENSSIET")
print("fin chiffrement")
#print("dechiffrement")
#dechiffrementViginere("MATHWEB","ORRWPSHDAIOEI")
#print("fin dechiffrement")