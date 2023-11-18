
"""
pip install numpy
"""

"""
Python ro'yxati va NumPy massivi o'rtasidagi farq nima?

NumPy sizga massivlarni yaratish va ulardagi raqamli ma'lumotlarni manipulyatsiya qilishning
juda ko'p tez va samarali usullarini taqdim etadi. Python ro'yxati bitta ro'yxatda turli xil
ma'lumotlar turlarini o'z ichiga olishi mumkin bo'lsa-da, NumPy massividagi barcha elementlar
bir hil bo'lishi kerak. Agar massivlar bir hil bo'lmasa, massivlarda bajarilishi kerak bo'lgan
matematik operatsiyalar juda samarasiz bo'lar edi.

"""

import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)