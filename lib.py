def equalElements(mas):
    seen = set()
    for element in mas[0]:
        count = 1
        for list in mas[1:]:
            count += 1 if element in list else False
        seen.add(element) if count == len(mas) else False
    print(seen)

mas = [[1,"e",6,89,9],
       [2,5,"6",7,6],
       [23,"6",7,8,6]]

equalElements(mas)