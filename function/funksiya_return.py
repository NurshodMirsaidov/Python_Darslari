# 18.02.2022
# 20-dars: Funksiyadan qiymat qaytarish

def toliq_ism_yasa(ism, familiya):
    """Foydalanuchiga to'liq ism familiyani ko'rdatib beradi"""
    toliq_ism = f"{ism.title()} {familiya.title()}"
    return(toliq_ism)
talaba1 = toliq_ism_yasa("nurshod", 'mirsaidov')
talaba2 = toliq_ism_yasa("sanjar", 'nurmuhammedov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")