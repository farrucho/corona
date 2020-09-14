import urllib.request
import os


nome_fich = os.path.basename(__file__)
path = os.path.realpath(__file__).replace(nome_fich, "")

user_name = os.getlogin()

file_future_location = "/Users/" + str(user_name) + "/resultados.txt"

print('A baixar o ficheiro...')
url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/data.csv'
urllib.request.urlretrieve(url, file_future_location)