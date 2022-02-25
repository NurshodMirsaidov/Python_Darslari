# 18.02.2022
# 20-dars: Funksiyadan qiymat qaytarish

# def toliq_ism_yasa(ism, familiya):
#     """Foydalanuchiga to'liq ism familiyani ko'rdatib beradi"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return(toliq_ism)
# talaba1 = toliq_ism_yasa("nurshod", 'mirsaidov')
# talaba2 = toliq_ism_yasa("sanjar", 'nurmuhammedov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# Ixtiyoriy argument
# def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
#     """Toliq ismni qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa("nurshod", "mirsaidov")
# talaba2 = toliq_ism_yasa("olim", "hakimov", "abdualiyev")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# avto info funksiya

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rangi": rangi,
#         "karobka": karobka,
#         "yil": yili,
#         "narh": narhi
#     }   
#     return avto

# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2017, 12000)
# avtolar = [avto1, avto2]
# print("Online bozorda mavjud avtomobillar: ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}, Narxi: {narh}")

# def oraliq(min, max, qadam = None):
#     sonlar= []
#     while min < max:
#         sonlar.append(min)
#         if qadam:
#             min += int(qadam)
#         else:
#             min += 1
#     return sonlar

# print(oraliq(0, 10, 2))


# avtolar malumotlarini kiritish

def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rangi": rangi,
        "karobka": karobka,
        "yil": yili,
        "narh": narhi
    }   
    return avto

print("Saytimizdagi avtolar ro'yxatini shakllantiring")
avtolar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end = "")
    kompaniya = input("Ishlab Chiquvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    karobka = input("Karobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narxi: ")
    
    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
    
    javob = input("Yana avtomobillarni qo'shasizmi? (yes/no)")
    if javob == 'no':
        break
    
print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rangi'].title()} {avto['model'].title()} {avto['karobka']} karobka. Narhi: {narh}")
    

    