# 1 способ
dct = {'AEIOULNSTR' : 1,
'DG' : 2,
'BCMP' : 3,
'FHVWY' : 4,
'K' : 5,
'JX' : 8,
'QZ' : 10,
'АВЕИНОРСТ' : 1,
'ДКЛМПУ' : 2,
'БГЁЬЯ' : 3,
'ЙЫ' : 5,
'ЖЗХЦЧ' : 6,
'ШЭЮ' : 8,
'ФЩЪ' : 10}


lst1 = list(input("Введите любое слово ").upper())
s = 0
for i in lst1:
    for j in dct.keys():
        if i in j:
            s += dct.get(j)
print(s)   


# 2 способ
# lst= [[1, 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
# [2, 'D', 'G'],
# [3, 'B', 'C', 'M', 'P'],
# [4, 'F', 'H', 'V', 'W', 'Y'],
# [5, 'K'],
# [8, 'J', 'X'],
# [10, 'Q', 'Z'],
# [1, 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
# [2, 'Д', 'К', 'Л', 'М', 'П', 'У'],
# [3, 'Б', 'Г', 'Ё', 'Ь', 'Я'],
# [4, 'Й', 'Ы'],
# [5, 'Ж', 'З', 'Х', 'Ц', 'Ч'],
# [8, 'Ш', 'Э', 'Ю'],
# [10, 'Ф', 'Щ', 'Ъ']]

# lst1 = list(input("Введите любое слово ").upper())
# s = 0
# for i in lst1:
#     j = 0
#     while (j < len(lst)):
#         p = 0
#         while (p < len(lst[j])):
#             if i == lst[j][p]:
#                 s += lst[j][0]
#                 break
#             p += 1
#         j += 1
# print(s)   