# 26.01.2022
# 7-dars: Lists (Ro'yxatlar)

#                   Matnli ro'yxat
# mevalar = ['olma', 'anor', 'shaftoli', "o'rik"]
# print(mevalar)

#                  Sonli ro'yxat
# narxlar = [12_000, 23_323, 342_323_233434, -545456546]
# print(narxlar)

#                   Aralash ro'yxat
# sonlar = ["bir", "ikki", 3, 4, 5]
# print(sonlar)

#                   Bosh ro'yxat
# ismlar = []
# print(ismlar)

#                   List ichidagi elementlarni chaqirish
# print(mevalar[2])
# print(mevalar[-1])

# print(mevalar[0].upper())

# print(narxlar[0])
# print(narxlar[0] + narxlar[1])

#                   Elementlarni o'zgartirish
# mevalar[0] = "anor"
# print(mevalar)

# mevalar[-1] = "uzum"
# print(mevalar)


#                   Listga elementlar qo'shish

# # APPEND
# print(mevalar)
# mevalar.append("Tarvuz")
# print(mevalar)
# mevalar.append("o'rik")
# print(mevalar)

# INSERT
# mevalar.insert(3, "banan")
# print(mevalar)


# cars = []
# cars.append("malibu")
# cars.append("gentra")
# cars.append("spark")
# print(cars)


#  DEL
# del cars[0]
# print(cars)
# cars.insert(2, "traccer")
# print(cars)
# del cars[2]
# print(cars)

#   REMOVE
# cars.remove("gentra")
# print(cars)

# hayvonlar = ["it", 'mushuk', 'it', 'ot', 'sigir']
# print(hayvonlar)
# hayvonlar.remove("it")
# print(hayvonlar)

#  POP
# bozorlik = ["yog'", "un", "go'sht", "sabzi"]
# print(bozorlik)

# mahsulot = bozorlik.pop(1)
# print(mahsulot)
# print(bozorlik)

# DASTUR
bozorlik = ["yog'", "un", "go'sht", "sabzi"]
mahsulot = bozorlik.pop(2)
print(f"Men {mahsulot}ni sotib oldim")
print(f"Olinmagan mahsulotlar--> {bozorlik}")
mahsulot2 = bozorlik.pop()
print(mahsulot2)