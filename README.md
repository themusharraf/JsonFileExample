# Python #numpy
# Numpy basic uzbek tilida 
# Creator: Musharraf ibragimov
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

🟢 Ma'lumotlar turini belgilash

Standart ma'lumotlar turi suzuvchi nuqta ( np.float64) bo'lsa-da, siz dtypekalit so'z yordamida qaysi ma'lumotlar turini aniq belgilashingiz mumkin.

        x = np.ones(2, dtype=np.int64)

🟢Elementlarni qo'shish, o'chirish va saralash 
Ushbu bo'lim o'z ichiga oladi np.sort() ,np.concatenate()

Elementni saralash bilan oddiy np.sort(). Funktsiyani chaqirganda siz o'qni, turni va tartibni belgilashingiz mumkin.
add array:

        arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
        
Siz raqamlarni o'sish tartibida tezda saralashingiz mumkin:

        np.sort(arr)

Indekslash va kesish :
Siz NumPy massivlarini xuddi Python roʻyxatlarini kesishingiz mumkin boʻlgan tarzda indekslashingiz va kesishingiz mumkin:

        data = np.array([1, 2, 3])

        data[1]
        data[0:2]
        data[1:]
        data[-2:]
<img width="586" alt="image" src="https://github.com/themusharraf/Python/assets/122869450/c0103c4a-fe5c-4558-88d3-0f5a0dd97f00">

        a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        print(a[a < 5])
        five_up = (a >= 5)
        print(a[five_up])
        juft = a[a%2==0]
        c = a[(a > 2) & (a < 11)]
Bundan tashqari, ikkita mavjud massivni vertikal va gorizontal ravishda joylashtirishingiz mumkin. Aytaylik, sizda ikkita massiv bor a1va a2:

        a1 = np.array([[1, 1],
               [2, 2]])

        a2 = np.array([[3, 3],
               [4, 4]])
Siz ularni vertikal ravishda quyidagi bilan biriktirishingiz mumkin vstack:

        s = np.vstack((a1, a2))
        
Yoki ularni gorizontal ravishda quyidagi bilan biriktiring hstack:

        m = np.hstack((a1, a2))

Agar siz massivni uchinchi va to'rtinchi ustundan keyin bo'lishni istasangiz, siz ishga tushirasiz:

        data = np.arange(1, 25).reshape(2, 12)
        
Yana foydali massiv operatsiyalari :

        data.max()
        data.min()
        data.sum()
<img width="571" alt="image" src="https://github.com/themusharraf/Python/assets/122869450/3f39ddef-7611-4648-9337-fde1aa92e614">

Agar siz ularga matritsaning o'lchamlarini tavsiflovchi kortejni bersangiz, 2D massivni yaratish uchun , ones()va zeros()dan ham foydalanishingiz mumkin :random()

        s = np.ones((3, 2))
        np.zeros((3, 2))
        rng.random((3, 2)) 

<img width="575" alt="image" src="https://github.com/themusharraf/Python/assets/122869450/e5a6694c-c5a8-4f9f-8cd6-638bee3bf1f7">

Tasodifiy raqamlarni yaratish:
yordamida Generator.integerssiz pastdan (numPy bilan birga ekanligini unutmang) yuqoridan (eksklyuziv) tasodifiy butun sonlarni
yaratishingiz mumkin. Siz endpoint=Trueyuqori raqamni qamrab oladigan qilib sozlashingiz mumkin.

Siz 0 dan 4 gacha bo'lgan 2 x 4 tasodifiy butun sonlarni yaratishingiz mumkin:

        rng.integers(5, size=(2, 4)) 


Noyob narsalar va hisoblarni qanday olish mumkin 
Ushbu bo'lim qamrab oladi np.unique()
Massivdagi noyob elementlarni yordamida osongina topishingiz mumkin np.unique.
Masalan, agar siz ushbu massivdan boshlasangiz:

      a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
      unique_values = np.unique(a)
      print(unique_values)
NumPy massividagi noyob qiymatlar indekslarini (massivdagi noyob qiymatlarning birinchi indeks pozitsiyalari massivi) olish uchun argumentni return_index massiv np.unique()bilan bir qatorda kiriting:

      unique_values, indices_list = np.unique(a, return_index=True)
      print(indices_list)

Matritsani ko'chirish va shaklini o'zgartirish 
Ushbu bo'lim arr.reshape() , arr.transpose(),arr.T

Matritsalaringizni ko'chirish odatiy holdir. TNumPy massivlari matritsani transpozitsiya qilish imkonini beruvchi xususiyatga ega :
<img width="543" alt="image" src="https://github.com/themusharraf/Python/assets/122869450/b37255e2-cceb-4f9d-b5aa-187ed9905479">


Bundan tashqari, matritsaning o'lchamlarini o'zgartirishingiz kerak bo'lishi mumkin. Bu, masalan, sizda ma'lumotlar to'plamidan farqli
bo'lgan ma'lum bir kirish shaklini kutadigan model mavjud bo'lganda sodir bo'lishi mumkin. Bu reshapeusul foydali bo'lishi mumkin. Siz shunchaki matritsa uchun kerakli yangi o'lchamlarga o'tishingiz kerak.
     
      data = np.arange(6)
      data.reshape(2, 3)
      data.reshape(3, 2)
      
<img width="590" alt="image" src="https://github.com/themusharraf/Python/assets/122869450/e9b1d403-4d58-4be5-8b8a-52dffe0fdb64">

bilan massivni ko'chirishingiz mumkin arr.transpose().

      data.transpose()



