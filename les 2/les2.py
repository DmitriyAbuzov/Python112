niz = int(input("Нижний диапазон:"))
verh = int(input("Верхний диапазон:"))
for i in range(niz, verh+1):
    if(i % 2 != 0):
        print(i)