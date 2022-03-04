# 01.03.2022
# 23-dars: Modullar

# import qilish

# 1-usul
# import avto_info_mod

# avto1 = avto_info_mod.avto_info("Gm", "Malibu", "Qora", "avtomat", 2020, 40000)
# avto_info_mod.info_print(avto1)

# 2-usul
# import avto_info_mod as aim

# avto1 = aim.avto_info("Gm", "Malibu", "Qora", "avtomat", 2020, 40000)
# aim.info_print(avto1)

# 3-usul
# from avto_info_mod import avto_info
# from avto_info_mod import info_print

# avto1 = avto_info("Gm", "Malibu", "Qora", "avtomat", 2020, 40000)
# info_print(avto1)

# 4-usul  
# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("Gm", "Malibu", "Qora", "avtomat", 2020, 40000)
# iprint(avto1)

# 5-usul
# from avto_info_mod import * # no recommended

# avto1 = avto_info("Gm", "Malibu", "Qora", "avtomat", 2020, 40000)
# info_print(avto1)

# PYTHON MODULES
# MATH

# import math
# x = 400 
# print(math.sqrt(x))   # kvadrat ildiz hisoblagich
# print(math.pow(5,3))  # 5 ning 3-darajasini hisoblaydi
# print(math.pi)        # Pi ning qiymati
# print(math.log2(8))   # 2 asosli logarifm ni hisoblaydi
# print(math.log10(100)) # 10 asosli logarifm


# RANDOM

import random as r

# randint() ---> berilgan oraliqdagi bitta tasodifiy sonni generatsiya qilib beradi
# son = r.randint(0, 100)
# print(son)

# choice() --> ro'yxat ichidan 1ta tasodifiy qiymatni tanlab oladi
# ismlar = ['anvar', 'begzod', 'jamshid', 'shokir']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))
# print(r.choice("Nurshod"))

# x = list(range(0, 100, 5))
# print(x)
# print(r.choice(x))


# SHUFFLE() --> aralashtirib tashlash uchun ishlatiladi
x = list(range(11))
print(x)
r.shuffle(x)
print(x)


