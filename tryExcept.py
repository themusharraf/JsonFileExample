"""
1.--> try Dastur kodida kod blokini xatolar uchun sinab ko'rish imkonini beradi.
2.--> except Dastur kodida sizga xatoni hal qilishga imkon beradi.
3.--> else Dastur kodida xato bo'lmaganda kodni bajarishga imkon beradi.
4.--> finally Dastur kodida sinash natijasidan qat'i nazar, kodni bajarishga imkon beradi- va bloklardan tashqari.
"""


# try:
#   print(x)
# except:
#   print("Bu yerda x mavjud bo'lmasa")


# x = 4
# try:
#   print(x)
# except NameError:
#   print("x topilmadi")
# except:
#   print("boshqa bir xatolik")

def bolish(x, y):
    try:
        natija = x / y
        print(f"{x} ni {y} ga bo'lganda natija: {natija}")
    except ZeroDivisionError:
        print("Xato: Nolga bo'lish mumkin emas.")
    except TypeError:
        print("Xato: Iltimos, bo'lish uchun to'g'ri sonlarni kiriting.")


# Misol qo'shish:
bolish(10, 2)  # Bu 'try' blokni muvaffaqiyatli bajaradi.

bolish(10, 0)  # Bu ZeroDivisionError ni keltiradi va mos 'except' blokni bajaradi.

bolish("abc", 2)  # Bu TypeError ni keltiradi va mos 'except' blokni bajaradi.
