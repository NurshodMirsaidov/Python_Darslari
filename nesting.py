# 09.02.2022 
# 16-dars: Nesting

#                Listni ichiga lug'atni joylash

# # car0 = {
# #     'model': 'lacetti',
# #     'rang': 'oq',
# #     'yil': 2018,
# #     'narx': 13_000,
# #     'km': 50_000,
# #     'karobka': 'avtomat'
# # }

# # car1 = {
# #     'model': 'nexia 3',
# #     'rang': 'qora',
# #     'yil': 2015,
# #     'narx': 9000,
# #     'km': 89_000,
# #     'karobka': 'mexanika'
# # }

# # car2 = {
# #     'model': 'gentra',
# #     'rang': 'qizil',
# #     'yil': 2019,
# #     'narx': 15_000,
# #     'km': 20_000,
# #     'karobka': 'mexanika'
# # }

# # car = car0
# # print(f"{car['model'].title()}, "
# #       f"{car['rang']} rang, "
# #       f"{car['yil']}-yil, {car['narx']}$")

# # IZOH ---> YUQIRIDAGI USUL JUDA HAM ESKI BO'LIB QUYIDAGI 
# # UNING OSON YO'LINI YOZAMAN

# # cars = [car0, car1, car2] # 3ta lug'atni 1ta list ichiga oldik
# # for car in cars:
# #    print(f"{car['model'].title()}, "
# #       f"{car['rang']} rang, "
# #       f"{car['yil']}-yil, {car['narx']}$")

# # print(cars[0]['narx'])

# # print(f"{cars[0]['rang'].title()}" ,
# #       f"{cars[0]['model']}")

# malibus = []
# for n in range(10):
#     new_car = {
#         'model': "malibu",
#         'rang': None,
#         'yil': 2021,
#         'narx': None,
#         'km': 0,
#         'karobka': 'avto'
#     }
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rang'] = "qizil"
    
# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus[3:6]:
#     malibu['rang'] = "qora"

# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['karobka'] = 'mexanika'


# for malibu in malibus:
#     if malibu["karobka"] == "avto":
#         malibu['narx'] = 40_000
#     else:
#         malibu['narx'] = 35_000


# for malibu in malibus:
#     print(malibu)


#                   Lug'at ichida Ro'yxat(list)
# dasturchilar  = {
#     'ali': ['python', 'c++'],
#     'vali': ['html', 'css', 'js'],
#     'husan': ['php', 'sql'],
#     'hasan': ['python', 'php'],
#     'jamshid': ['c++', 'c#']
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini bilishadi")
#     for til in tillar:
#         print(til.upper())


# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini bilishadi")
#     for til in tillar:
#         print(til.upper(), end = " ")



# hamkasblar = {
#     'ali': {
#         'familiya': "valiyev",
#         'tyil': 1995,
#         'malumot': 'oliy',
#         'tillar': ["python", "c++"]
#     },
#     'vali': {
#         "familiya": 'aliyev',
#         'tyil': 2001,
#         'malumot': "o'rta maxsus",
#         "tillar": ["html", "css", "js"]
#     },
#     "husan": {
#         "familiya": "murodov",
#         "tyil": 2000,
#         'malumot': "o'rta maxsus",
#         'tillar': ["python", "php"] 
#     }
# }

# for ism, info in hamkasblar.items():
#     print(f"\n {ism.title()} {info['familiya'].title()} " ,
#           f"{info['tyil']} yilda tug'ilgan. ",
#           f"Ma'lumoti: {info['malumot']}. \n",
#           "Quyidagi dasturlash tillarini biladi: ")

#     for til in info['tillar']:
#         print(til.upper())


#               AMALIYOT
# 1.Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.


shaxs1 = {
    'ism': 'abu abdulloh muhammad ibn ismoil',
    'tyil': 810,
    'tjoy': "buxoro",
    'yosh': 60,
    'asarlar': ["Al-jome' as-sahih", 
                "Al-adab al-mufrad",
                "At-tarix al-kabir",
                "At-tarix as-sag'ir"]
}
shaxs2 = {
    'ism': 'abdulla qodiriy',
    'tyil': 1984,
    'tjoy': "toshkent",
    'yosh': 44,
    'asarlar': ["O'tkan kunlar", 
                "Mehrobdan chayon",
                "Obid ketmon"]
}

shaxs3 = {
    'ism': 'erkin vohidov',
    'tyil': 1936,
    'tjoy': "farg'ona",
    'yosh': 80,
    'asarlar': ["Tong nafasi", 
                "Qo'shiqlarim sizga",
                "O'zbekim",
                "Qiziquvchan Matmusa"]
}
shaxs4 = {
    'ism': 'alisher navoiy',
    'tyil': 1441,
    'tjoy': 'xirot',
    'yosh': 60,
    'asarlar': ["Xamsa", 
                "Lison ut-Tayr",
                "Mahbub ul-qulub"]
}

buyuk_shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]

# for shaxs in buyuk_shaxslar:
#     print(f"{shaxs['ism'].title()} {shaxs['tyil']}-yilda {shaxs['tjoy'].title()}da tug'ilgan.", 
#     f"{shaxs['yosh']} yil umr ko'rgan.")


# 2.Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
#For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

# for shaxs in buyuk_shaxslar:
#     print(f"\n{shaxs['ism'].title()} ning mashxur asarlari: ")

#     for asar in shaxs['asarlar']:
#         print(asar)


# 3.Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, 
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.

# kinolar = {
#     'ali': ["Terminator", 'Rembo', "Titanik"],
#     'vali': ["Tenet", "Inception", "Intersteller"],
#     'hasan': ["Abdullajon", "Bomba", "Shaytanat"],
#     'husan': ["Mahallada duv-duv gap", "John Wick"]
# }

# for odam in kinolar:
#     print(f"\n{odam.title()}ning sevimli kinosi: ")
#     for kino in kinolar[odam]:
#         print(kino)


# 4.Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni
# lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

# davlatlar = {
#     "O'zbekiston": {
#         "poytaxt": "Toshkent",
#         "hududi": 448978,
#         "aholisi": 33_000_000,
#         "pul birligi": "so'm"
#     },
#       "Rossiya": {
#         "poytaxt": "Moskava",
#         "hududi": 17_098_246,
#         "aholisi": 144_000_000,
#         "pul birligi": "rubl"
#     },
#       "AQSH": {
#         "poytaxt": "Washington",
#         "hududi": 9_631_418,
#         "aholisi": 327_000_000,
#         "pul birligi": "dollar"
#     },
#       "Malayziya": {
#         "poytaxt": "Kuala-Lumpur",
#         "hududi": 329_750,
#         "aholisi": 25_000_000,
#         "pul birligi": "rinngit"
#     }
# }

# davlat = input("Davlat nomini kiriting: ")
# if davlat == 'aqsh':
#     davlat = davlat.upper()
# else:
#     davlat = davlat.title()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat}ning poytaxti {info['poytaxt']}"
#         f"\nHududi: {info['hududi']} kv.km"
#         f"\nAholisi: {info['aholisi']}"
#         f"\nPul birligi: {info['pul birligi']}")
# else:
#     print(f"Bizda {davlat} haqida ma'lumot yo'q")


# 5.