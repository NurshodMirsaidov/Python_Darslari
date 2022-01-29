# 28.01.2022

# 1. Foydalanuvchidan juft son kiritishni so'rang.
#  Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son = int(input("Juft son kiriting: "))
print("Raxmat!") if son % 2 != 1 else print("Bu juft son emas")

# 2.Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingiz nechida: "))
# if yosh < 4 and yosh > 60:
#     print("Bepul")
# elif yosh < 18:
#     narx = 10_000
# elif yosh > 18:
#     narx = 20_000
# print(f"Chipta narxi siz uchun {narx}sum")