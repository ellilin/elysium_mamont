f = open("input.csv", "r")
f1 = open("1.3.txt", "w")

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

f.close()
f1.close()
f = open("input.csv", "r")
f1 = open("1.3.txt", "w")

for i in f:
    s=i.split(';')
    f1.write(s[0] + ';' + s[1] + ';' + str(round((float(s[2])*100)/sumali, 3)) + ';' + str(round((float(s[3])*100)/sumbob, 3)) + ';' + str(round((float(s[4])*100)/sumcha, 3)) + ';' + str(round((float(s[5])*100)/sumdev, 3)) + ';' + str(round((float(s[6])*100)/sumeri, 3))+'\n')

f.close()
f1.close()
