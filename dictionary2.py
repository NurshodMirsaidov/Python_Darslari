# 04.02.2022
# 15-dars: Lug'atlar bilan ishlash

#               .items() --> bu metod bizga lug'atdagi har bir 
#       har bir key value larni juftlikda chiqarib beradi
# talaba_0 = {
#     'ism': 'alijon',
#     'familiya': 'shamsiyev',
#     'yosh' : 22,
#     'fakultet': 'matematika',
#     'kurs': 4
# }
# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'majid': 'mi 10 pro',
#     'olim': 'nokia x3 f4 ad3'
# }

# for k , v in telefonlar.items():
#    print(f"{k.title()}ning telefoni {v}")

# #  .keys() - lug'atni ichidagi har bir kalitni qaaytaradi

# mahsulotlar = {
#     'olma': 10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir': 25000,
#     'shaftoli': 30000
# }

# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar: ')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print('Do\'kondagi mahsulotlar: ')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot} {mahsulotlar[mahsulot]} so'm")



# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum}ni ham olib keling ")



# Sorted() lug'atni taxlash
# print(sorted(mahsulotlar.keys()))
# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
    # print(mahsulot.title())



# .values()
# print(telefonlar.values())

# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi")
# for telefon in telefonlar.values():
#     print(telefon)


# .set() ----> qiymatlar takrorlansa faqat 1tasini oladi

# telefonlar = {
#     'olim': 'iphone x10',
#     'jasur': 'galaxy s9',
#     'meroj': 'samsung',
#     'naim': 'galaxy s9',
#     'majid': 'samsung',
#     'orif': 'iphone x10'
# }

# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
# for tel in set(telefonlar.values()):
#     print(tel)

# SET HAM MA'LUMOT TURI  

# toys = {'ball', 'car', 'lamp', 'ball', 'car'}
# print(type(toys))

# UYGA VAZIFA

# 1.Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
#  Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 

# python = {
#     'If': 'Shartlarni tekshirish operatori',
#     'Float': "O'nlik son",
#     'Boolean': 'Mantiqiy qiymat',
#     'For': 'Biror amalni qayta - qayta bajarish tsikli',
#     'Integer': 'Butun son'
# }

# for kalit, qiymat in sorted(python.items()):
#     print(f"{kalit} - {qiymat}")


# 2.Davlatlar va ularning poytaxtlari lug'atini tuzing. 
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 

# davlatlar = {
#     'Amerika': 'Washington',
#     'Uzbekistan': 'Tashkent',
#     'Germaniya': 'Berlin',
#     'Italiya': 'Rim',
#     'Angliya': 'London',
#     'Xitoy': 'Pekin',
#     'Rossiya': 'Moskva',
#     'Hindiston': 'New Dehli'
# }

# print("Dunyo davlatlari: ")
# for davlat in sorted(davlatlar):
#     print(davlat)

# print("\nDavlatlar poytaxti: ")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt)

# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').title()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")



# 3.Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
#  Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.


# davlatlar = {
#     'Amerika': 'Washington',
#     'Uzbekistan': 'Tashkent',
#     'Germaniya': 'Berlin',
#     'Italiya': 'Rim',
#     'Angliya': 'London',
#     'Xitoy': 'Pekin',
#     'Rossiya': 'Moskva',
#     'Hindiston': 'New Dehli'
# }

# state = input("Istalgan davlat nomini kiriting: ").title()
# davlat_bor = davlatlar.get(state)
# if davlat_bor == None:
#     print(f"Afsuski bizda {state} haqida hech qanday ma'lumot yo'q")
# else:
#     print(f"{state.title()} ning poytaxti - {davlat_bor.title()} shahri")


# 4.Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
#  Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

# restoran_taomlar = {
#     'manti': 5000,
#     'somsa': 6000,
#     'osh': 20_000,
#     'shashlik': 16_000,
#     'sho\'rva': 18_000,
#     'non': 3500,
#     'choy': 2000
# }

# print("3 ta taom buyurtma bering.")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n + 1}-taom: ").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in restoran_taomlar:
#         print(f"Sizning buyurtmangiz {buyurtma} narxi - {restoran_taomlar[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz bizda {buyurtma} yo'q")