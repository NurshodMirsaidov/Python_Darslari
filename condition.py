# 28.01.2022
# 10-dars: IF-ELSE SHARTLAR VA TARMOQLANISH

# avtolar = ["audi", "bmw", "mersedes", "gm", "tesla"]

# for avto in avtolar:
    # print(avto.title())

# for avto in avtolar:
    # if avto == "bmw":
        # print(avto.upper())
    # else:
        # print(avto.title())

# print(avto)
# print(avto == "bmw")
# print(avto == "tesla")

#                   SHARTLARNI TEKSHIRISH
# a = 10
# a == 3 # a tengmi 3ga ---> False
# a == 10 # a tengmi 10ga ---> True

# ism = "Ali"
# ism == "Ali" # True
# ism == "ali" # False


# a = 5
# a == 5 #True
# a == 6 #False
#  != ----> teng emas
# print(a != 4 ) # True
# print(a != 5 ) # False

# ism = input("Ismingiz nima?\n--->")
# if ism.lower() != "ali":
#     print("Uzur biz Alini kutyapmiz")
# else:
#     print("Salom Ali")

# misol = float(input(f"12 * 6 nechchi?\n>>>"))
# if misol == 72:
#     print("Barakalla to'g'ri topdiz")
# else:
#     print("Eh afsus javob noto'ri")

# yosh = int(input("Yoshingizni kiriting\n>>> "))
# if yosh >= 18:
#     print("Xush kelibsiz")
# else:
#     print("Kirishingiz taqiqlanadi chunki yoshiz ", yosh)

# login = input("Yangi login tanlang   ")
# if (len(login)) <= 5:
#     print("5 harfdan ko'proq login tanlang")
# else:
#     print("Raxmat login qabul qilindi")

# t_yil = int(input("Tug'ilgan yilingizni kiiting   "))
# if 2022 - t_yil < 18:
#     print(f"Sizning yoshingiz {2022 - t_yil}ga teng ekan")
#     print("Siz kira olmaysiz")
# else:
#     print(f"Sizning yoshingiz {2022 - t_yil}ga teng ekan")
#     print("Marhamat kirishingiz mumkin")

# yosh = int(input("Yoshingizni kiriting "))
# if yosh > 65: print("Siz COVID-19 risk guruhida ekansiz")


#               TERNARNY OPERATOR (JS)
# x, y = 50, 44
# print("x > y") if x > y else print("x < y")

# Amaliyot

# 1. Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining
# birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

# cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())


#2.  Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring.
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

# ism = input("Ismingiz nima? ").title()
# if ism == "Admin":
#     print("Xush kelibsiz, Admin, Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Assalomu aleykum {ism}!")


# 3. Foydalanuvchidan 2 ta son kiritishni so'rang.
# Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

# print("2ta son kiriting")
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))

# if son1 == son2:
#     print("2ta son teng")


# 4. Foydalanuvchidan istalgan son kiritishni so'rang. 
# Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 

# son = int(input("Istalgan sonni kiriting: "))
# if son < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")


# 5. Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
#  Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

# son = float(input("Istalgan sonni kiriting: "))
# if son < 0:
#     print("Musbat son kiriting")
# else:
#     print(f"{son}ning ildizi -> {float(son**(1/2))}ga teng")