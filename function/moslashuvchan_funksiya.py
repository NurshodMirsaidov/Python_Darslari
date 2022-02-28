# 28.02.2022
# 22-dars: Moslashuvchan funksiya

# args kwargs


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
#     print(f"{avto['rangi']} {avto['model']}, Narxi: {narh}")

# *
    # def summa(*sonlar):
    #     """Kiritilgan sonlar yig'indisini hisoblaydigan funsiya"""
    #     yigindi = 0
    #     for son in sonlar:
    #         yigindi += son
    #     return yigindi
    # print(summa(2,3,4))
    # print(summa(2,3,4, 2323))
    # print(summa(2,3,4, 4, 5, 23))

    # def summa(*sonlar):
    #     """Kiritilgan sonlar yig'indisini hisoblaydigan funsiya"""
    #     return sum(sonlar)    
    # print(summa(2,3,4))
    # print(summa(2,3,4, 2323))
    # print(summa(2,3,4, 4, 5, 23))


    # def summa(x, y, *sonlar):
    #     """Kiritilgan sonlar yig'indisini hisoblaydigan funsiya"""
    #     return x + y + sum(sonlar)    

    # print(summa(2,3,4))
    # print(summa(2,3,4, 2323))
    # print(summa(2,3,4, 4, 5, 23))
    # # print(summa(2)) # false 


    # # **kwargs
    # def avto_info(kompaniya, model, **malumotlar):
    #     malumotlar['kompaniya'] = kompaniya
    #     malumotlar['model'] = model
    #     return malumotlar 

    # avto1 = avto_info("GM", "malibu", rang = 'qora', yil = 2005)
    # avto2 = avto_info("GM", "lacetti", rang = 'oq', yil = 2010)

    # print(avto1)
    # print(avto2)

# Amaliyot
# 1.Istalgancha sonlarni qabul qilib, 
# ularning ko'paytmasini qaytaruvchi funksiya yozing

# def multiply(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma = kopaytma * son
#     return kopaytma

# print(multiply(2, 3))
# print(multiply(2, 3, 2))
# print(multiply(2, 3, 12))

# 2

# def talabalar(ism, familiya, **info):
#     info['ism'] = ism
#     info['familiya'] = familiya
#     return info

# talaba = talabalar("Nurshod", "Mirsaidov", yoshi = 12, sinfi = "A")
# print(talaba)