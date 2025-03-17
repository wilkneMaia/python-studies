from pyModbusTCP.client import ModbusClient
import csv

# Configurar o cliente Modbus
client = ModbusClient(host="192.168.100.123", port=502, unit_id=1, auto_open=True)

print ("Conectando ao inversor...")
print (client.open())

# # Ler os valores do inversor (exemplo de leitura dos registros)
# # Altere os endereços dos registros conforme a documentação do OpenDTU
# registers = client.read_holding_registers(100, 10)  # Lê 10 registros a partir do endereço 100

# # Verificar se a leitura foi bem-sucedida
# if registers:
#     # Nome do arquivo CSV
#     csv_filename = "opendtu_data.csv"

#     # Abrir o arquivo CSV para escrita
#     with open(csv_filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Data', 'Produção_gerada', 'Outros_valores'])  # Ajuste os cabeçalhos conforme necessário

#         # Exemplo de como escrever os dados nos registros (ajuste conforme a leitura dos dados)
#         for i, value in enumerate(registers):
#             writer.writerow([f"Data_{i+1}", value, "Outro_valor"])  # Adapte os dados que deseja escrever

#     print(f"Dados salvos em {csv_filename}")
# else:
#     print("Erro ao ler dados via Modbus")
