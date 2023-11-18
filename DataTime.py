"""
Python dasturlash tilida sanani ifodalash uchun joriy sanani aniqlash va
sanalar ustida amallar bajarish uchun tayyor modul bo'lib uning nomi datetime.

"""
import datetime
import datetime

"""hozir vaqt ni olish """
# x = datetime.datetime.now()
# print(x)
# output --> 2022-02-22 23:46:40.602510


"""
Modulda datetime sana ob'ekti haqidagi ma'lumotlarni qaytarishning
ko'plab usullari mavjud. Biz siz bilan joriy vaqtda yil va hafta kunini chiqaramiz.
"""
# x = datetime.datetime.now()
#
# print(x.year)
# print(x.strftime("%A"))
# output yil va hafta kuni


"""
Sana yaratish uchun modul datetime() sinfidan (konstruktor) foydalanishimiz mumkin.
Sana datetime()yaratish uchun sinf uchta parametrni talab qiladi: yil, oy, kun.
"""

# x = datetime.datetime(2022, 2, 22)
#
# print(x)
# output 2022-02-22 00:00:00


"""
Ob'ektda datetimesana ob'ektlarini o'qiladigan satrlarga formatlash usuli mavjud.
Satr formatini belgilash uchun strftime()bitta parametrni oladi.
"""

x = datetime.datetime(2022, 2, 22)

print(x.strftime("%B"))
# output February


"""
format kodlarining ma'lumotnomasi:
%a - Hafta kunlarini qisqa nomi (Wed)
%A - Hafta kunining to'liq nomi (Wednesday)
%w - Hafta kuni qaysi sanasida ya'ni nechanchi kuni 0 - 6 gacha (3)
%d - Oy kuni (31)
%b - Oyning qisqa nomi (Dec)
%B - Oyning to'liq nomi (December)
%m - Oylar raqamlarda 01 - 12 (12)
%y - Yilning qisqa raqami, oxirgi ikkita raqami (22)
%Y - Yilning to'liq nomi (2022)
%H - Soat tariflash 00 - 23 (18)
%I - Soat ta'riflash 00 - 12 (09)
%p - Soat ta'riflash AM/PM (PM)
%M - Minut ta'riflash 00 - 59 (35)
%S - Sekund 00 - 59 (09)
%f - millisekund 000000-999999 (465845)\
%Z - TimeZone (CST)
%j - Yil kuni 001 - 366 (263)
%C - Asr ni chiqarish (21)
"""
