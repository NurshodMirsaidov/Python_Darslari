# 17.02.2022
# Funksiya

# def salom_ber():
#     '''Salom beruvchi funksiya''' # FUNKSIYA haqida ma'lumot
#     print("Assalom aleykum")

# salom_ber()

# def salom_ber(ism):
#     """Foydalanuvchi beruvchi ismni qabul qilib,
#      unga salom beruvchi funksiya"""
#     print(f"Assalomu aleykum, hurmatli {ism.title()}!")

# salom_ber("hasan")
# salom_ber("Olim")

# # Docstrinng ---> Funksiya haqida ma'lumot
# print(salom_ber.__doc__) # funksiya haqida ma'lumot beradi


# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
    
# toliq_ism("Nurshod", "Mirsaidov")

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchining ismi va yoshini ko'rsatuvchi dastur"""
#     print(f"Salom {ism.title()}, siz {2022 - tugilgan_yil} yoshda ekansiz!")

# yosh_hisobla("nurshod", 2006)
# yosh_hisobla(tugilgan_yil=2006, ism='nurshod')


# def yosh_hisobla(tugilgan_yil, joriy_yil = 2022):
#     """Foydalanuvchi tug'ilgan yilifan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz!")

# yosh_hisobla(2006, 2022)
# yosh_hisobla(1000)

# Amaliyot
# 1.Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

# son = int(input("Son kiriting:\n>> "))
# def son_darajasini_hisobla(son):
#     kvadrat = son **2
#     kub = kvadrat*son
#     print(f"{son}ning kvadrati: {kvadrat}, kubi: {kub} ")
    
# son_darajasini_hisobla(son)

# 2.Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# son = int(input("Son kiriting:\n>> "))
# def son_darajasini_hisobla(son):
#     if son % 2 == 0:
#         print(f"{son} soni - juft sondir.")
#     elif son % 2 == 1:
#         print(f"{son} soni - toq sondir.")
        
# son_darajasini_hisobla(int(input("Son kiriting:\n>> ")))

# 3.Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

# son1 = int(input("1- sonni kiriting:\n>>>"))
# son2 = int(input("2- sonni kiriting:\n>>>"))

# def son_taqqosla(son1, son2):
#     if son1 < son2:
#         print(f"2-son katta: {son1} < {son2}")
#     elif son1 > son2:
#         print(f"1-son katta: {son1} > {son2}")
#     else:
#         print("2ta son teng")
        
# son_taqqosla(son1, son2)

# 4.Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing
# x = int(input("Sonning asosini kiriting:\n>>"))
# y = int(input("Sonning darajasini kiriting:\n>>"))

# def son_daraja(x, y):
#     print(f"{x} ning {y}-darajasi: {x**y} ga teng")

# son_daraja(x, y)
  