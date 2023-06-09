# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке


stih = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
glasn = set("ауоыиэяюёе")

lst = stih.split()
lst1 = list()

# 1 способ
for i in lst:
    lst1.append(len(list(filter(lambda x: x in glasn, i))))
                                                                       

# 2 способ
# for i in lst:
#     k = 0
#     for j in i:
#         if j in glasn:
#             k += 1
#     lst1.append(k)

def same_by(count):
     return  len(set(count)) < 2


if same_by(lst1):
    print("Парам пам-пам")
else:
    print("Пам парам")