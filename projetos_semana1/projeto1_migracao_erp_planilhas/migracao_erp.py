import pandas as pd
import gspread #usada para interagir com o Google Sheets
from oauth2client.service_account import ServiceAccountCredentials #usada para autenticar seu script com o Google usando uma Service Account (uma conta de serviço criada no Google Cloud).

df = pd.read_json('erp_pedidos.json')

sheet_data = []

sheet_data.append(["ID_Pedido", "Cliente", "Produto", "Quantidade", "Preco", "Data"])

for index, pedido in df.iterrows(): #percorre cada linha do DataFrame como um objeto Series
    sheet_data.append([
        pedido["ID_Pedido"],
        pedido["Cliente"],
        pedido["Produto"],
        pedido["Quantidade"],
        pedido["Preco"],
        pedido["Data"]
    ])


#CONECTAR AO GOOGLE SHEETS

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)
sheet = client.open("ERPrecebimento").sheet1  
sheet.clear()
sheet.update('A1', sheet_data)
print("Dados enviados com sucesso para o Google Sheets!")
