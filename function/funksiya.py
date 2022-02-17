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