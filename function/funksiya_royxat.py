# 28.02.2022
# 21-dars: Funksiyaga ro'yxat uzatish

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"{ism.title()} ismli talabaning  bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)        
# print(talabalar)

# Amaliyot
# 1.Matnlardan iborat ro'yxat qabul qilib,
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

# def katta_qil(ismlar):
#     """Funksiyaga ismlar joylangan ro'yxat joylashtirib ko'ring"""
#     for n in range(len(ismlar)):
#         ismlar[n] = ismlar[n].title()
        
#     return ismlar

# names = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_qil(names[:])
# print(yangi_ismlar)
# print(names)

# Yuqoridagi 1- masalaning ishlanishining ikkinchi yo'li

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = int(input(f"{ism.title()} ning bahosini kiriting: "))
#         baholar[ism] = baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)        
# print(talabalar)