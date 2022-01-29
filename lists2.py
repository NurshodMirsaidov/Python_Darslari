# 26.01.2022
# 8-dars: Ro'yxatlar bilan ishlash. O'zgarmas ro'yxatlar (Tuples)

# cars = ["malibu", "gentra", "spark", "nexia", "matiz", "lacetti"]
# print(cars)

# cars.sort()
# print(cars)

# cars.sort(reverse = True)
# print(cars)

# print(sorted(cars))
# print(cars)
# print(sorted(cars, reverse=True))
# print(cars)


# sonlar = [-23. -34, 343, 34454, 2, 454,454434343333, -233333333333333]
# print(sonlar)
# print(sorted(sonlar))


# cars.reverse()
# print(cars)

# print(len(cars))

# sonlar = list(range(1,10))
# print(sonlar)

# toq_sonlar = list(range(1, 20, 2))
# print(toq_sonlar)
# juft_sonlar = list(range(0, 20, 2))
# print(juft_sonlar)

# sanash = list(range(0, 101, 10))
# print(sanash)

# max_qiymat = max(toq_sonlar)
# print(max_qiymat)

# narxlar = [12000, 23000, 34000, 454545]
# min_narx = min(narxlar)
# max_narx = max(narxlar)
# summa = sum(narxlar)
# print(min_narx, max_narx, summa)



# narxlar = [12000, 3443565, 23434, 4452, 23000, 34000, 454545]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print(f"Eng arzon mahsulot - {arzon}sum, eng qimmati - {qimmat}sum, jami esa - {jami}sum=")


# cars = ["bmw", "audi", "tesla", "gm", "mersedez", "volvo"]
# print(cars[2:13]) #2dan 13gacha 13emas
# print(cars[:3]) #3gacha

# my_cars = cars
# print(cars)
# print(my_cars)
# my_cars.remove("volvo")
# print(my_cars)
# my_cars[0] = "lacetti"
# print(my_cars)
# print(cars)

# cars.append("bmw")
# print(cars)
# print(my_cars)




#RO'YXATDAN NUSXA OLISH UCHUN QUYIDAGI METODNI QILISH KERAK SHUNDA 1TA LISTGA 2TA NOM BERILMAYDI
# my_cars = cars[:]
# my_cars.remove("bmw")
# print(my_cars)
# print(cars)



# TUPLE RO'YXATI
toys = ("car", "bear", "lizard", "snake")
# tupleni yasash uchun jingalak qavs emas, dumaloq qavs ochiladi

# print(toys[2])
# toys[0] = "teddy" #bunaqa qilib listni almashtirib olmaymiz

# AGAR O'ZGARTIMOQCHI BO'LSAK UNI QUYIDAGICHA QILAMIZ
# print(type(toys)) #class tuple
# toys = list(toys)
# print(toys)
# toys.append("shilliqurt")
# print(toys)
# print(type(toys)) #class list
