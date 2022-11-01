f = open("input.csv", "r")
f1 = open("output_5.4.txt", "w")

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
f = open("input.csv", "r")

for i in f:

    s=i.split(';')
    f1.write(s[0] + ';' + s[1] + ';' + str(round(((int(s[2])/sumali)*100), 3))+ ';' + str(round(((int(s[3])/sumbob)*100), 3)) + ';' + str(round(((int(s[4])/sumcha)*100),3)) + ';' + str(round(((int(s[5])/sumcha)*100),3)) + ';' + str(round(((int(s[6])/sumcha)*100),3))+ '\n')

f1.close()
f.close()
f = open("output_5.4.txt", "r")

sumali = 0      #ценность грузов для Алисы
sumbob = 0      #ценность грузов для Боба
sumcha = 0      #ценность грузов для Чарли
sumdev = 0      #ценность грузов для Дэвда
sumeri = 0      #ценность грузов для Эрика
kali = 0        #количество грузов Алисы
kbob = 0        #количество грузов Боба
kcha = 0        #количество грузов Чарли
kdev = 0        #количество грузов Дэвида
keri = 0        #количество грузов Эрика

for i in f:

    s=i.split(';')
    print(s[0], '   ',s[1], end = ' ')

    if float(sumali) <=  float(sumcha) and float(sumali) <= float(sumbob) and float(sumali) <= float(sumdev) and float(sumali) <= float(sumeri):
        print('Алиса')
        sumali+=float(s[2])
        kali+=1
    elif float(sumbob) <  float(sumali) and float(sumbob) < float(sumcha) and float(sumbob) < float(sumdev) and float(sumbob) < float(sumeri):
        print('Боб')
        sumbob+=float(s[3])
        kbob+=1
    elif float(sumcha) <=  float(sumali) and float(sumcha) <= float(sumbob) and float(sumcha) <= float(sumdev) and float(sumcha) <= float(sumeri):
        print('Чарли')
        sumcha+=float(s[4])
        kcha+=1
    elif float(sumdev) <=  float(sumali) and float(sumdev) <= float(sumbob) and float(sumdev) <= float(sumcha) and float(sumdev) <= float(sumeri):
        print('Дэвид')
        sumdev+=float(s[5])
        kdev+=1
    elif float(sumeri) <=  float(sumali) and float(sumeri) <= float(sumbob) and float(sumeri) <= float(sumcha) and float(sumeri) <= float(sumdev):
        print('Эрик')
        sumeri+=float(s[6])
        keri+=1

print("Алиса ценность:", sumali, " количество:", kali)
print("Боб ценность:", sumbob, " количество:", kbob)
print("Чарли ценность:", sumcha, " количество:", kcha)
print("Дэвид ценность:", sumdev, " количество:", kdev)
print("Эрик ценность:", sumeri, " количество:", keri)

f.close()
