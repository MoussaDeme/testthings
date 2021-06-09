#nombres premiers
def nombrePremiers(n):

    list_nbPremiers = [2,3]
    i = 5
    while(i<=n):
        k = 1
        for j in list_nbPremiers:
            if(i%j==0):
                k = 0
        if(k!=0):
            list_nbPremiers.append(i)
        if(i<3):
            i+=1
        else:
            i+=2
        for k in list_nbPremiers:
            print(k)



# chiffrement de cesar
def cesar(n,texte):
    alp_clair = []
    texte_chiffre = []
    newTexte = texte.upper()
    for i in range(65,91):
        alp_clair.append(chr(i))
    for i in newTexte:
        for j in range(0,26):
            if(i == alp_clair[j]):
                if((j+n)<26):
                    texte_chiffre.append(alp_clair[j+n])
                else:
                    texte_chiffre.append(alp_clair[(j+n)%26])
    chaine_chiffre = ''.join(texte_chiffre)
    return chaine_chiffre

# decodage du message
def dechiffrement(n,texteAdechiffrer):
    alp_clair = []
    texte_dechiffre = []
    newTexte = texteAdechiffrer.upper()
    for i in range(65, 91):
        alp_clair.append(chr(i))
    for i in newTexte:
        for j in range(0,26):
            if(i == alp_clair[j]):
                if((j-n)>=0):
                    texte_dechiffre.append(alp_clair[j-n])
                else:
                    texte_dechiffre.append(alp_clair[26-(j-n)])
    chaine_dechiffrer = ''.join(texte_dechiffre)
    return  chaine_dechiffrer

#casser le code
def casserLeCode(texteAchiffre,textechiffre):
    k = -1
    for i in range(0,26):
        texte = cesar(i,texteAchiffre)
        if(texte==textechiffre):
            k = i
    if(k!=-1):
        print("la clé est : ",k)
chaine_chiffre = cesar(3,"COUCOU")
chaine_dechiffre = dechiffrement(4,"FMK")
#nombrePremiers(50)
print(chaine_dechiffre)
#print(chaine_dechiffre)
#casserLeCode("COUCOU","NZFNZF")
