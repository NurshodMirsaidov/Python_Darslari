# 27.01.2022
# 9-dars: FOR TSIKLI BILAN TANISHAMIZ

# mehmonlar = ["ali", "muhammad", "javox", "ruslan", "hasan", "husan"]

# for mehmon in mehmonlar:
#     print(f"Salom, {mehmon}")
#     print(f"Hayr, {mehmon}")

# mehmonlar = ["Ruslan", "Sardor", "Nurshod", "Sherzod"]

# for mehmon in mehmonlar:
    # print(f"Assalomu aleykum {mehmon} sizni 1-fevral kuni bo'ladigan naxorgi oshga taklif qilamiz") 
    # print("Hurmat bilan Palonchijon xonasi")

# sonlar = list(range(1, 11))

# for son in sonlar: 
#     print(f"{son} ning kvadrati ---> {son ** 2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []

# for son in sonlar:
#     sonlar_kvadrati.append(son**2)

# print(sonlar)
# print(sonlar_kvadrati)

dostlar = []
print("5ta eng yaqin do'stingiz ismini kiriting")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizni kiriting\n>>>>"))

print(dostlar)