# 09.02.2022 
# 16-dars: Nesting

# car0 = {
#     'model': 'lacetti',
#     'rang': 'oq',
#     'yil': 2018,
#     'narx': 13_000,
#     'km': 50_000,
#     'karobka': 'avtomat'
# }

# car1 = {
#     'model': 'nexia 3',
#     'rang': 'qora',
#     'yil': 2015,
#     'narx': 9000,
#     'km': 89_000,
#     'karobka': 'mexanika'
# }

# car2 = {
#     'model': 'gentra',
#     'rang': 'qizil',
#     'yil': 2019,
#     'narx': 15_000,
#     'km': 20_000,
#     'karobka': 'mexanika'
# }

# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")

# IZOH ---> YUQIRIDAGI USUL JUDA HAM ESKI BO'LIB QUYIDAGI 
# UNING OSON YO'LINI YOZAMAN

# cars = [car0, car1, car2] # 3ta lug'atni 1ta list ichiga oldik
# for car in cars:
#    print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")

# print(cars[0]['narx'])

# print(f"{cars[0]['rang'].title()}" ,
#       f"{cars[0]['model']}")