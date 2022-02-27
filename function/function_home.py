# 27.02.2022
# Funksiya uyga vazifalari

# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting:"))

# def yosh_hisobla(name, age):
#     print(f"Assalomu aleykum {ism.title()}, siz {2022 - yosh}yilda tugilgansiz, tugrimi")
    
# yosh_hisobla(ism, yosh)

# kvadrat va kub
# number = int(input("Son kiriting: "))
# def son_darajasi(a):
#     kvadrat = a ** 2
#     kubi = kvadrat * a
#     print(f"{a} ning kvadrati: {kvadrat} ga \n"
#           f"kubi {kubi}ga teng")
#     return kvadrat, kubi

# son_darajasi(number)

    
# Juft toq
# son = int(input("son kiriting: "))

# def juft_toq(num):
#     if num % 2 == 0:
#         print("Bu juft son")
#     elif num % 2 == 1:
#         print("Bu toq son")
#     else:
#         print("Xatolik ketdi")
        
# juft_toq(son)

# Katta kichik
# son1 = int(input("son kiriting: "))
# son2 = int(input("son kiriting: "))

# def kotta_kichik(son1, son2):
#     if son1 < son2:
#         print("Ikkinchi son katta")
#     elif son1 > son2:
#         print("Birinchi son katta")
#     elif son1 == son2:
#         print("Ikkita son teng")
        
# kotta_kichik(son1, son2)


# son1 = int(input("son kiriting: "))
# son2 = int(input("darajani kiriting: "))

# def daraja(x, y):
#     i = 1
#     z= x
#     while i < y:
#         x = x * z
#         i+=1
#     print(x)
    
# daraja(son1, son2)    
    

son = int(input("son kiriting: "))
def bolinish(num):
    for x in range(2, 11):
        if not num % x:
            print(f"{num} soni {x}ga qoldiqsiz bo'linadi \n")
        
bolinish(son)