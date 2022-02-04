# 28.01.2022
# 11-dars: IF-ELIF-ELSE 

# son = -50

# if son < 0:
    # print("Manfiy son")
# else: 
    # print("Musbat son")

# # ZOOPARK
# yosh = int(input("Yoshingiz nechida\n>>>> "))
# if yosh <= 4:
#     print("Kirish bepul")
# elif yosh <= 12:
#     print("Kirish haqqi 5000 so'm")
# elif yosh <= 18:
#     print("Kirish narxi 8000 so'm")
# else: 
#     print("Kirish narxi 10 000 so'm")

# TEPADAGI DASTURNING QULAY USULI - PASTDA--->

# yosh = int(input("Yoshingiz nechida\n>>>> "))
# if yosh <= 4:
#     narx = "bepul"
# elif yosh <= 12:
#     narx = 5000
# elif yosh <= 18:
#     narx = 8000
# else: 
#     narx = 10_000
# print(f"Siz uchun kirish narxi {narx}")

#               DAM OLISH KUNINI ANIQLOVCHI DASTUR
# kun = input("Bugun qaysi kun\n>>> ").lower()
# if kun == "shanba" or kun == "yakshanba":
    # print("Haa bugun demak dam olish kuni ekan")
# else:
    # print("Bugun ish kuni ekan")


# kun = input("Bugun qaysi kun\n>>> ").lower()
# harorat = int(input("Bugun havo harorati nechchi\n>>> "))

# if (kun == "shanba" or kun == "yakshanba") and harorat >= 30:
#     print("Kettik cho'milgani boramiz")
# elif (kun == "shanba" or kun == "yakshanba") and harorat < 30:
#     print("Uyda dam olamiz")

# #               BOOLEAN 
# narh = 15000
# choy = True
# salad = False

# if choy and salad:
#     narh = narh + 10000
# elif choy or salad:
#     narh = narh + 5000

# print(f"Jami {narh} so'm")


# narx = 15000
# choy = True
# salad = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("Mijoz choy oldi")
#     narx += 3000
# if salad:
#     print("Mijoz salat oldi")
#     narx += 5000
# if non:
#     print("Mijoz non oldi")
#     narx += 2000
# if kompot:
#     print("Mijoz kompot oldi")
#     narx += 5000
# if assorti:
#     print("Mijoz assorti oldi")
#     narx += 15000
# print("Mijoz hisob haqqi", narx)

# menu = ["osh", "qazonkabob", "somsa", "manti"]
# print("manti" in menu)

#           DASTUR
# menu = ["osh", "qazonkabob", "shashlik", "somsa", "manti"]
# ovqat = input("Nima ovqat yeysiz\n>>>").lower()

# if ovqat in menu:
    # print("Byurtma qabul qilindi")
# else:
    # print("Afsuski bizda bunday ovqat yo`q")


#               NOT IN

# print("sho'rva" not in menu)


#           DASTUR

# menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa", "manti"]
# buyurtmalar = ["osh", "olma", "manti", "shashlik"]

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
            # print(f"Kechirasiz, Menuda {taom} yuq")
# else:
#     print("Buyurtmada hech nima yo'q")

