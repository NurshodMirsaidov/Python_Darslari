# 16.02.2022
# 18 - dars: While, Ro'yxatlar, Lug'atlar

print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingizni ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("\nYana biror do'stingizning ismini qo'shmoqchimisz? (ha/yo'q)")
    n+=1
    if takrorlash != "ha":
        break

print("Sizning do'stlaringiz ro'yxati: ")
for ism in ismlar:
    print(ism)


print("Keling do'stlaringizning yoshini tuzamiz")
dostlar = {}
ishora = True

while ishora:
    ism = input("Do'stingiz ismini kiriting: ").title()
    yosh = input(f"{ism} ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    takrorlash = input("Yana do'stingizni qo'shasizmi? (ha/yo'q)")
    if takrorlash != 'ha':
        break

for ism, yosh in dostlar.items():
    print(f"{ism}ning yoshi {yosh}da")

cars = ['audi', 'mersedez', 'toyota', 'nexia', 'lacetti', 'nexia', 'nexia']
car = 'nexia'
while car  in cars:
    cars.remove(car)
print(cars)


talabalar = ['jasur', 'olim', 'sardor', 'anvar', 'rashid']
baholangan_talablar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talablar[talaba] = int(baho)

print(baholangan_talablar)