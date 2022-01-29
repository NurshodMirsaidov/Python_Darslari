# 24.01.2022
# 5-dars: Matnlar bilan ishlash (Strings)

# ism = "Anvar"
# shahar = "Кукон"
# viloyat = "Фаргона"

# SAYT: UNICODE_TABLE.COM
# matn = "Men yangi telefon sotib oldim"

# ism = "Nurshod"
# print("Mening ismim " + ism)

# ism = "Davron"
# familiya = "Ergashev"
# print(ism + familiya)

# ism = "Sardor"
# familiya = "Hamroqulov"
# print(ism + " " + familiya)

# f string usuli
# ism = "Jasur"
# familiya = "Holiqov"
# print(f"{ism} {familiya}")

# ism = "James"
# familiya = "Bond"
# print(f"Salom mening ismim {ism}, {ism} {familiya}")

# ism = "Nurshod"
# familiya = "Mirsaidov"
# print(f"Salom mening ismim {ism}, {ism} {familiya}")

# MAXSUS BELGILAR
# print("Hello World")
# print("Hello \tWorld")  #UZUN BO'SHLIQ
# print("HEllo \nWorld") #QATORGA BO'LISH 





#                           STRING METODALARI
# UPPER
# ism = "James"
# familiya = "Bond"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())

# LOWER
# ism = "James"
# familiya = "Bond"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.lower())

# TITLE
# ism = "JAMES"
# familiya = "BOND"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.title())

# CAPITALIZE
# ism = "JAMES"
# familiya = "BOND"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.capitalize())


# meva = "    olma    "
# print(meva)
# print(f"Men {meva}ni yaxshi ko'raman")

# LSTRIP() --> bu metod chap tarafdagi bo'shliqni olib tashlaydi
# print(f"Men {meva.lstrip()}ni yaxshi ko'raman")

# RSTRIP() --> bu metod o'ng tarafdagi bo'shliqni olib tashlaydi
# print(f"Men {meva.rstrip()}ni yaxshi ko'raman")

# STRIP() --> bu metod ikkala tarafdagi bo'shliqlarni olib tashlaydi
# print(f"Men {meva.strip()}ni yaxshi ko'raman")

#                       INPUT 

# ism = input("Ismingiz nima? ")
# print(f"Salom, {ism}")

# ism = input("Ismingiz nima: \n")
# print("Assalomu aleykum " + ism.title())


#               UYGA VAZIFA

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(kocha, "ko`chasi,", mahalla, "mahallasi,", tuman, "tumani,", viloyat, "viloyati")

kocha = input("Ko'chani nomini kiriting: ")
mahalla = input("Mahalla nomini kiriting: ")
tuman = input("Tuman nomini kiriting: ")
viloyat = input("Viloyat nomini kiriting: ")
# print(kocha, "ko`chasi,", mahalla, "mahallasi,", tuman, "tumani,", viloyat, "viloyati")
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
