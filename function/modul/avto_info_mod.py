
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

def avto_kirit():
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
    return avtolar
    
def info_print(avto_info):
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['karobka']} karobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")
   
