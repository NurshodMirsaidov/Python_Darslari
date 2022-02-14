# 13.02.2022
# While Loops 

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)

# while()
# son = 1
# while son <= 5:
#     print(son, end = " ")
#     son +=1

# print("Dastur tugadi")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ""
# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# else:
#     print("Dastur tugadi")

# # ISHORA YORDDAMIDA DASTURNI TO'XTATISH
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


# BREAK TSIKLI 
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
    
# while True:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur tugadi!")


# while for

# sonlar = list(range(1, 11))

# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son}ning kvadrati {son ** 2} ga teng")


# Continue while
# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)


# INFINITE LOOP
# son = 0
# while son < 10:
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)


# 1.Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
#  Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

# kitob = "Yaxshi ko'rgan kitobingizni kiriting: "

# while True:
#     book = input(kitob)
#     if book == 'stop':
#         break
# print("Dastur tugadi")


# 2.Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
# 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

savol = "Yoshingizni kiriting: "

while True:
    value = input(savol)
    if value == "quit" or value == "exit":
        break
    yosh = int(value)

    if yosh < 7:
        narx = 2000
    elif 7<= yosh <18:
        narx = 3000
    elif 18 <= yosh < 65:
        narx = 10000
    else:
        narx = 0

    if narx == 0:
        print("Sizga kirish bepul")
    else:
        print(f"Sizga chipta narxi - {narx}")