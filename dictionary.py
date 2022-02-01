# 01.02.2022
# 14-DARS. Lug'at (Dictionary)

# car_0 = {
#     'model': 'ferrari',
#     'rang': 'qizil'
# }
# print(car_0['model'])
# print(car_0['rang'])

# en_uz = {
#     'apple': 'olma',
#     'apricot': "o'rik",
#     'banana': 'banan'
# }
# print(en_uz)
# print(en_uz['apple'])

# mevalar = {
#     'olma': 10000,
#     'tarvuz': 8000,
#     'qovun': 10000
# }
# print(f"Olma narxi {mevalar['qovun']} so'm")

# Lug'atni ichida har xil ma'lumotlarni saqlashimiz mumkin
# talaba_0 = {
#     'ismi': 'nurshod',
#     'yoshi': 16,
#     't_yil': 2006
# }
# print(f"{talaba_0['ismi'].title()},\
#     {talaba_0['t_yil']} - yilda tug'ilgan,\
#     {talaba_0['yoshi']} yoshda")

# Lug'atga ma'lumot qo'shish
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# print(talaba_0)

# Lug'atda ma'lumotlarni o'zgartirish
# talaba_0['ismi'] = 'Abdulloh' # Value ni o'zgartirish
# print(talaba_0)


# dastur
# user = {}
# user['name'] = input("Enter your name:  ")
# user['age'] = input("How old are you? ")
# user['job'] = input("Do you work or study? ")
# print(user)


# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} kurs va {talaba_1['yosh']} yoshda")

# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} kurs va {talaba_1['yosh']} yoshda")


# Lug'atdan elementni o'chirib tashlash (del)
# talaba_0 = {
#     'ismi': 'nurshod',
#     'yoshi': 16,
#     't_yil': 2006
# }

# del talaba_0['ismi']
# print(talaba_0)

# Qatorga bo'lib yozish
# telefonlar = {
#     'ali': 'iphone x', 
#     'vali': 'samsung j4',
#     'jamshid': 'redmi note 10',
#     'anvar' : 'mi 9 pro'
# }


#               GET()
# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')
# print(phone) 

# phone = telefonlar.get('hasan')
# print(phone)


# 
# 
#                   AMALIYOT
 
# 1.otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 
# 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring 

# otam = {
#     'ismi': "Ulug'bek",
#     'yoshi': 41,
#     "t_yil": 1981,
#     "shahri": 'qashqadaryo',
#     'manzil': 'Kitob tuman Varganza shaharchasi'
# }
# info = f"Otamning ismi {otam['ismi']}, {otam['t_yil']}-yilda, {otam['shahri'].title()} viloyati {otam['manzil']}da tug'ilgan. Hozir {otam['yoshi']}dalar."
# print(info)



# 2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# taomlar = {
#     'oyim': 'manti',
#     'otam': 'osh',
#     'ukam': 'kartoshka',
#     'men': 'somsa'
# }
# print(f"Oyimning sevimli ovqati {taomlar['oyim']}")
# print(f"Otamning sevimli ovqati {taomlar['otam']}")
# print(f"Ukamning sevemli ovqati {taomlar['ukam']}")


# 3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

python = {
    'integer': 'butun son',
    'float': "o'nli son",
    'string': "matn ma'lumot turi",
    'if': 'agar',
    'else': 'aks holda',
    'for in': 'tsikl da ishlatiladigan funksiya',
    'list': "ro'yxat ma'lumot turi"
}

# 4. Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
#  Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

info = input("Kalit so'z kiriting: ")
malumot = python.get(info, "Bunday kalit so'zni bilmayman")
print(malumot)