from corona import object_data as dados
from matplotlib import pyplot as plt
from corona import baixar
import os

os.system("object_data.py")

dia_mes_x = dados.dia_mes[193:201]
n_casos_y = dados.n_casos[193:201]
#obitos_y = dados.obitos[14:30]

plt.style.use("fivethirtyeight")
plt.title("Gráfico de COVID-19")

plt.plot(dia_mes_x, n_casos_y)
#print(dia_mes_x)
#print(n_casos_y)
#print(obitos_y)


plt.xlabel("Dia/Mes", fontsize = 11)
plt.ylabel("Número de casos confirmados", fontsize = 11)
plt.tight_layout()
plt.show()

input("SAIR")
