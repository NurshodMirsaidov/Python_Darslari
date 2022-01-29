# 29.01.2022
# 12-dars: "Eng ko'p uchraydigan xatolar"

#       SyntaxError
# print "hello world!"      # Xato
# print("hello world!")     # tugri

# print("hello world"       # EOF --> end of function
# print("hello world!       # EOL --> end of line


#       IndentationError --- > unexpected indent == (kutilmagan bo'sh joy mavjud)
    # print("Hello World!")   # error

# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n)                      # expected an indented block



#       Run time error
# 1. TypeError
# son = input("Istalgan sonni kiriting: ") # bu yerda int() yo'q
# print(f"{son} ning kvadrati {son ** 2} ga teng") # unsupported operand type(s) for ** or pow(): 'str' and 'int'

# 2. NameError
# prit("Hello world") #    name 'prit' is not defined

# mevalar = ["olma", "anor", "banan", "gilos"]
# for meva in mvalar:   # name 'mvalar' is not defined
    # print(meva)

# 3. ValueError
# son = int(input("Istalgan son kiriting: ")) # agar 23.4 yozsak:
# invalid literal for int() with base 10: '34.4
# if son < 0:
    # print("Manfiy son")
# else:
    # print("Musbat son")

# 4. IndexError
# mevalar = ["olma", "anor", "gilos"]
# print(mevalar[3])           # list index out of range == print(mevalar[2])


# 5. ZeroDivisionError
# x, y = 50, 50
# z = 250 / (x - y)   # division by zero
# print(z)



#                   Mantiqiy xatolar

# radius = 5
# pi = 4.14  # pi = 3.14
# aylana_yuzi = pi * (radius ** 2)
# print(aylana_yuzi)

# son = int(input("Son kiriting: "))
# ildiz = son ** (1/2)
# print(f"{son}ning ildizi {int(ildiz)}ga teng")

# mevalar = ["olma", "anor", "banan", "gilos"]
# for meva in mevalar:
    # print(meva)
    # print("Dastur tugadi")  # ushbu qatorni tsikldan tashqarida yozish kerak

