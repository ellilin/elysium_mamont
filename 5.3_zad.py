f = open("input.csv", "r")
f1 = open("output_5.3.txt", "w")

sumali = 0      #ценность всех грузов для Алисы
sumbob = 0      #ценность грузов для Боба
sumcha = 0      #ценность всех грузов для Чарли

for i in f:

    s=i.split(';')
    sumali+=int(s[2])
    sumbob+=int(s[3])
    sumcha+=int(s[4])

f.close()
f = open("input.csv", "r")

for i in f:

    s=i.split(';')
    f1.write(s[0] + ';' + s[1] + ';' + str(round(((int(s[2])/sumali)*100), 3))+ ';' + str(round(((int(s[3])/sumbob)*100), 3)) + ';' + str(round(((int(s[4])/sumcha)*100),3))  + '\n')

f1.close()
f.close()
f = open("output_5.3.txt", "r")

sumali = 0      #ценность грузов для Алисы
sumcha = 0      #ценность грузов для Чарли
sumbob = 0      #ценность грузов для Боба
kbob = 0        #количество грузов Боба
kali = 0        #количество грузов Алисы
kcha = 0        #количество грузов Чарли

for i in f:

    s=i.split(';')
    print(s[0], '   ',s[1], end = ' ')

    if float(sumali) <=  float(sumcha) and float(sumali) <= float(sumbob):
        print('Алиса')
        sumali+=float(s[2])
        kali+=1

    elif float(sumali) >=  float(sumcha) and float(sumbob) >=  float(sumcha):
        print('Чарли')
        sumcha+=float(s[4])
        kcha+=1

    elif float(sumali) >=  float(sumbob) and float(sumbob) <=  float(sumcha):
        print('Боб')
        sumbob+=float(s[3])
        kbob+=1
        
print("Алиса ценность:", sumali, " количество:", kali)
print("Боб ценность:", sumbob, " количество:", kbob)
print("Чарли ценность:", sumcha, " количество:", kcha)


f.close()
