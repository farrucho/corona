from corona import baixar

informacao_file = open(baixar.file_future_location, "r")
#print(informacao_file.readable())

linhas_a_ler = informacao_file.readlines()

lista = []

for index in linhas_a_ler:
    #print(index.split(","))
    lista.append(index.split(","))

lista.remove(lista[0])
#print(lista)
#print(lista[0][1])

dia_mes_data = []

def dia_mes(dia, mes):
    dia_mes_data.append([dia, mes, str(dia) + "/" + str(mes)])

for index in lista:
        #print("MES:", index[0][3] + str(index[0][4]))
        #print("DIA:", index[0][0] + str(index[0][1]))
        month = index[0][3] + str(index[0][4])
        day = index[0][0] + str(index[0][1])

        dia_mes(day, month)

#print(dia_mes_data)

dia_mes = []
for index in dia_mes_data:
    #print(index[2])
    dia_mes.append(index[2])

n_casos = []
obitos = []
for index in lista:
    #print(index[3])
    n_casos.append(index[3])
    #print(index[13])
    obitos.append(index[13])
#print(n_casos)
