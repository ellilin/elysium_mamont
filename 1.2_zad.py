f = open("input.csv", "r")

sumali = 0      #ценность грузов для Алисы
sumbob = 0      #ценность грузов для Боба
sumcha = 0      #ценность грузов для Чарли
sumdev = 0      #ценность грузов для Дэвда
sumeri = 0      #ценность грузов для Эрика

for i in f:

    s=i.split(';')
    sumali+=int(s[2])
    sumbob+=int(s[3])
    sumcha+=int(s[4])
    sumdev+=int(s[5])
    sumeri+=int(s[6])

print("Суммарная ценность Алисы ", sumali)
print("Суммарная ценность Боба ", sumbob)
print("Суммарная ценность Чарли ", sumcha)
print("Суммарная ценность Дэвида ", sumdev)
print("Суммарная ценность Эрика ", sumeri)

f.close()
