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



hamkasblar = {
    'ali': {
        'familiya': "valiyev",
        'tyil': 1995,
        'malumot': 'oliy',
        'tillar': ["python", "c++"]
    },
    'vali': {
        "familiya": 'aliyev',
        'tyil': 2001,
        'malumot': "o'rta maxsus",
        "tillar": ["html", "css", "js"]
    },
    "husan": {
        "familiya": "murodov",
        "tyil": 2000,
        'malumot': "o'rta maxsus",
        'tillar': ["python", "php"] 
    }
}

for ism, info in hamkasblar.items():
    print(f"\n {ism.title()} {info['familiya'].title()} " ,
          f"{info['tyil']} yilda tug'ilgan. ",
          f"Ma'lumoti: {info['malumot']}. \n",
          "Quyidagi dasturlash tillarini biladi: ")

    for til in info['tillar']:
        print(til.upper())
