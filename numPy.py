"""
pip install numpy
"""
import numpy as np

"""
Python ro'yxati va NumPy massivi o'rtasidagi farq nima?

NumPy sizga massivlarni yaratish va ulardagi raqamli ma'lumotlarni manipulyatsiya qilishning
juda ko'p tez va samarali usullarini taqdim etadi. Python ro'yxati bitta ro'yxatda turli xil
ma'lumotlar turlarini o'z ichiga olishi mumkin bo'lsa-da, NumPy massividagi barcha elementlar
bir hil bo'lishi kerak. Agar massivlar bir hil bo'lmasa, massivlarda bajarilishi kerak bo'lgan
matematik operatsiyalar juda samarasiz bo'lar edi.

"""

x = np.arange(4)  # np.arange(4) bu berilgan qiymat uzunligicha massiv yaratib beradi
# print(x)  # [0 1 2 3]

"""
Va hatto bir xil intervalli intervallarni oz ichiga olgan massiv
Buni amalga oshirish uchun siz birinchi raqamni, oxirgi raqamni va qadam hajmini korsatasiz.

"""
s = np.arange(2, 9, 2)
# print(s)  # [2, 4, 6, 8]

"""
np.arange(15) bu berilgan qiymat uzunligicha massiv yaratib beradi
Massivni qayta shakllantirish uchun reshape() dan foydalanishingiz mumkin.
Masalan, siz ushbu massivni uchta qator va ikkita ustunli massivga o'zgartirishingiz mumkin:

"""

a = np.arange(15).reshape(3, 5)  # 3x5 array
print(a)
print(a.itemsize)
print(a.dtype)  # type of the array
