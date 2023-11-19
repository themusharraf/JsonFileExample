# Python #numpy
Numpy docs uzbek tilida 
Creator: Musharraf ibragimov
                  NumPy: yangi boshlanuvchilar uchun mutlaq asoslar
🟢NumPy ( Raqamli Python ) ochiq manba Python kutubxonasi boʻlib, fan va muhandislikning deyarli barcha sohalarida qoʻllaniladi.
Bu Python-da raqamli ma'lumotlar bilan ishlash uchun universal standart bo'lib, Python va PyData ilmiy ekotizimlarining asosini
tashkil etadi. NumPy foydalanuvchilari boshlang'ich kodlovchilardan tortib, eng zamonaviy ilmiy va sanoat tadqiqotlari va ishlanmalari
bilan shug'ullanuvchi tajribali tadqiqotchilargacha bo'lgan barchani o'z ichiga oladi. NumPy API Pandas, SciPy, Matplotlib, scikit-learn,
scikit-image va boshqa ko'plab ma'lumotlar fanlari va ilmiy Python paketlarida keng qo'llaniladi.

Agar sizda allaqachon Python bo'lsa, NumPy-ni quyidagi bilan o'rnatishingiz mumkin:

                      conda install numpy    
                      pip install numpy

Qanday import qilinadi

                      import numpy as np

np NumPy yordamida kodni yaxshiroq o'qish uchun import qilingan nomni qisqartiramiz . Bu keng ko'lamda qabul qilingan konventsiya bo'lib
u sizning kodingiz ustida ishlayotgan har bir kishi uchun o'qilishi mumkin bo'ladi. Biz har doim import numpy dan foydalanishni tavsiya qilamiz np.

Python ro'yxati va NumPy massivi o'rtasidagi farq nima?

🟢NumPy sizga massivlarni yaratish va ulardagi raqamli ma'lumotlarni manipulyatsiya qilishning juda ko'p tez va samarali usullarini taqdim etadi.
Python ro'yxati bitta ro'yxatda turli xil ma'lumotlar turlarini o'z ichiga olishi mumkin bo'lsa-da, NumPy massividagi barcha elementlar bir hil bo'lishi kerak.
Agar massivlar bir hil bo'lmasa, massivlarda bajarilishi kerak bo'lgan matematik amallar juda samarasiz bo'lar edi.

Nima uchun NumPy dan foydalanish kerak?

🟢NumPy massivlari Python ro'yxatlariga qaraganda tezroq va ixchamroq. Massiv kamroq xotira sarflaydi va ulardan foydalanish qulay.
NumPy ma'lumotlarni saqlash uchun kamroq xotiradan foydalanadi va u ma'lumotlar turlarini belgilash mexanizmini ta'minlaydi. Bu kodni yanada optimallashtirish imkonini beradi

🟢Massiv nima? 
Massiv NumPy kutubxonasining markaziy ma’lumotlar strukturasidir. Massiv qiymatlar to'plami bo'lib, unda xom ma'lumotlar, elementni qanday topish va elementni qanday izohlash
haqida ma'lumotlar mavjud. Unda turli yo'llar bilan indekslanishi mumkin bo'lgan elementlar to'plami mavjud . Elementlarning barchasi bir xil turdagi, massiv deb ataladi dtype.

Massiv manfiy bo'lmagan butun sonlar majmuasi, mantiqiy, boshqa massiv yoki butun sonlar bilan indekslanishi mumkin. rankMassivning o'lchamlari soni .
Massiv shapehar bir oʻlcham boʻyicha massivning oʻlchamini beruvchi butun sonlar majmuasidir.

  Masalan:
  
    a = np.array([1, 2, 3, 4, 5, 6])
    
  yoki:

    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

🟢Massivning atributlari qanday?

Massiv odatda bir xil turdagi va o'lchamdagi elementlarning qat'iy o'lchamli konteyneridir. Massivdagi o'lchamlar va elementlarning soni uning shakli bilan belgilanadi. 
Massivning shakli har bir o'lchamning o'lchamlarini belgilaydigan manfiy bo'lmagan butun sonlar to'plamidir.

🟢Asosiy massivni qanday yaratish kerak
    Ushbu bo'lim:
    
    np.array() , np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(),dtype

NumPy massivini yaratish uchun funksiyadan foydalanishingiz mumkin 

    import numpy as np
    a = np.array([1, 2, 3])

🟢Siz massivingizni quyidagicha tasavvur qilishingiz mumkin:
<img width="559" alt="image" src="https://github.com/themusharraf/Python/assets/122869450/a3f837d3-af9f-4738-bf42-cddc9af5783b">

Elementlar ketma-ketligidan massiv yaratishdan tashqari, osongina 0's bilan to'ldirilgan massivni yaratishingiz mumkin:

        np.zeros(2)
        
Yoki 's bilan to'ldirilgan massiv 1:

        np.ones(2)
      
