import os,string

f1  = open('todosjugadores.txt', 'r')

dic = {}
dic_13_14 = {} 
contador = 0
f1.readline()
while 1:
    linea = f1.readline()
    if not linea:break
    lista = linea.split('\t')
    contador = contador + 1
   # print lista[12]
    if lista[0] not in dic.keys():
        if lista[7].find('EBA') != -1:
            dic[lista[0]] = [1, 0, 0, [lista[12]], 1]
        elif lista[7].find('L.V.Jun. F.') != -1:
            dic[lista[0]] = [0, 0, 1, [lista[12]], 1]
        elif lista[7].find('L.V. Jun. M.') != -1:
            dic[lista[0]] = [0, 1, 0, [lista[12]], 1]
        else: 
            print 'no hemos encontrado la categoria del jugador %s'%lista[0]
    else:
        #print dic[lista[0]]
        for n in dic[lista[0]][3]:
          #  print n
            if lista[12] != n:
                lista_club = []
                lista_club = dic[lista[0]][3]
                lista_club.append(lista[12])
           #     print dic[lista[0]][3],lista_club, n, lista[12]
                clubes = len(lista_club)
            else:
                lista_club = dic[lista[0]][3]
                clubes = len(lista_club)
        if lista[7].find('EBA') != -1:
            dic[lista[0]] = [dic[lista[0]][0] +1, dic[lista[0]][1], dic[lista[0]][2], lista_club, clubes]
        elif lista[7].find('L.V.Jun. F.') != -1:
            dic[lista[0]] = [dic[lista[0]][0], dic[lista[0]][1] , dic[lista[0]][2] +1, lista_club, clubes]
        elif lista[7].find('L.V. Jun. M.') != -1:
            dic[lista[0]] = [dic[lista[0]][0], dic[lista[0]][1] +1, dic[lista[0]][2], lista_club, clubes]
        else: 
            print 'no hemos encontrado la categoria del jugador %s'%lista[0]
#print dic

contador_4EBA = 0
contador_3EBA = 0
contador_2EBA = 0
contador_1EBA = 0
contador_1jun = 0
contador_2jun = 0
cont_1_1 = 0
cont_1_2 = 0
cont_2_1 = 0
cont_2_2 = 0
cont_3_1 = 0
cont_mas2_jun = 0
masc = 0
fout = open('chicos.txt', 'w')
for b in dic.keys():
    if dic[b][0] >0 or dic[b][1] >0 and dic[b][2] == 0: 
        masc = masc + 1
        #fout.write(str(dic[b][0]) +'\t' + str(dic[b][1]) +'\n')
    if dic[b][0] == 4: contador_4EBA = contador_4EBA + 1
    elif dic[b][0] == 3 and dic[b][1] == 0: contador_3EBA = contador_3EBA + 1
    elif dic[b][0] == 2 and dic[b][1] == 0: contador_2EBA = contador_2EBA + 1
    elif dic[b][0] == 1 and dic[b][1] == 0: contador_1EBA = contador_1EBA + 1
    elif dic[b][0] == 0 and dic[b][1] == 1: contador_1jun = contador_1jun + 1
    elif dic[b][0] == 0 and dic[b][1] == 2: contador_2jun = contador_2jun + 1
    elif dic[b][0] == 1 and dic[b][1] == 1: cont_1_1 = cont_1_1 + 1
    elif dic[b][0] == 1 and dic[b][1] == 2: cont_1_2 = cont_1_2 + 1
    elif dic[b][0] == 2 and dic[b][1] == 1: cont_2_1 = cont_2_1 + 1
    elif dic[b][0] == 2 and dic[b][1] == 2: cont_2_2 = cont_2_2 + 1
    elif dic[b][0] == 3 and dic[b][1] == 1: cont_3_1 = cont_3_1 + 1
    elif dic[b][1] >2: cont_mas2_jun = cont_mas2_jun + 1
    elif dic[b][3] == 0:
        print b, dic[b][0], dic[b][1]
#print masc, contador_4EBA + contador_3EBA+ contador_2EBA+ contador_1EBA+ contador_1jun+ contador_2jun + cont_1_1 + cont_1_2 +cont_2_1 +cont_2_2 + cont_3_1 + cont_mas2_jun
fout.write('4 EBA' + '\t' +'3 EBA' + '\t' +'2 EBA' + '\t' +'1 EBA' + '\t' + '2 Junior' + '\t' + '1 Junior' + '\t' + '1 EBA 1 Junior' + '\t' + '1 EBA 2 Junior' + '\t' + '2 EBA 1 Junior' + '\t' + '2 EBA 2 Junior' + '\t' + '3 EBA 1 Junior' + '\t' + '3 Jun' + '\n')
fout.write(str(contador_4EBA) + '\t' +str(contador_3EBA) + '\t' +str(contador_2EBA) + '\t' + str(contador_1EBA) + '\t' + str(contador_2jun)+ '\t' + str(contador_1jun) + '\t' + str(cont_1_1) + '\t' + str(cont_1_2) + '\t' + str(cont_2_1) + '\t' + str(cont_2_2) + '\t' + str(cont_3_1) + '\t' + str(cont_mas2_jun) + '\n') 
fout.close()
dic_chicas = {}
fchicas = open('chicas.txt', 'w')
for f in dic_chicas.keys():
    print f
    fchicas.write(f +'\t')
fchicas.write('\n')
for f in dic_chicas.keys():
    fchicas.write(str(dic_chicas[f]) +'\t')
fchicas.close()
