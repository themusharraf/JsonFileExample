"""
pip install pandas
"""


def natija():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]
    listtt = []
    for i in matrix:
        for a in i:
            if a % 2 == 0:
                b = a ** 2
                listtt.append(b)
            else:
                listtt.append(a)


    return listtt
