"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

company_list = {'Компания1': 9000, 'Компания2': 30000,
                'Компания3': 8000, 'Компания4': 8100,
                'Компания5': 5000, 'Компания6': 7000}

# O(N)

def top3(dict_1):
    list1 = sorted(dict_1.values(), reverse=True)[:3]   # O(log N)
    top_company = {}                                    # O(1)
    for key, val in company_list.items():               # O(N)
        if val in list1:                                # O(N)
            top_company.update({key:val})               # O(len(..))
    return top_company                                  # O(1)

print(top3(company_list))


# O(N**2)

def top3_2(dict_1):
    list1 = sorted(dict_1.values(), reverse=True)[:3]   # O(log N)
    top_company = {}                                    # O(1)
    for el in list1:                                    # O(N)
        for key, val in company_list.items():           # O(N)
            if el == val:                               # O(N)
                top_company[key] = val                  # O(1)
    return top_company                                  # O(1)

print(top3_2(company_list))

# Первый способ лучше , руководствуясь натацией О большое