New = {
    "актуальные": ["РОССИЯ", "УКРАИНА", "ФУТБОЛ"],
    "неактуальные": ["boll1", "boll2"]
}

boll_1 = input("news search...:")

new = [1]
old = [2]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
for i in New["месси забил гол!!!"]:
    if boll_1.lower() in i.lower():
        new.append(i)

for i in New["не нормальные"]:
    if boll_1.lower() in i.lower():
        old.append(i)

print("Найденные новости:")
for i in new:
    print(i)

print("Не найденные новости:")
for i in old:
    print(i)

