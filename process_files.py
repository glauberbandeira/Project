import os
import shutil
import time

# Define source and destination directories
pasta_origem = './relatorios'
pasta_destino = './relatorios_processados'

# Check if the source folder exists before proceeding
if not os.path.exists(pasta_origem):
    print(f"Error: The source folder '{pasta_origem}' does not exist.")
    exit()  # Terminates execution if the source folder does not exist

# Create the destination folder if it does not exist
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# List all files in the source folder
arquivos = os.listdir(pasta_origem)

# Dictionary to store file information
info_arquivos = {}

# Filter files that end with '_processado.xlsx'
arquivos_processados = [arquivo for arquivo in arquivos if arquivo.endswith('_processado.xlsx')]

# If there are no files to process, exit the program
if not arquivos_processados:
    print("No processed files found to move.")
    exit()

# Collect file information before moving them
for arquivo in arquivos_processados:
    caminho_completo = os.path.join(pasta_origem, arquivo)
    
    # Get file information before moving
    try:
        tamanho = os.path.getsize(caminho_completo)  # Get the file size
        data_criacao = time.ctime(os.path.getctime(caminho_completo))  # Get the file creation date

        # Save the information in the dictionary
        info_arquivos[arquivo] = [data_criacao, tamanho]
    except FileNotFoundError:
        print(f"Error: File {arquivo} not found for retrieving information.")
        continue

# Move processed files to the destination folder
for arquivo in arquivos_processados:
    caminho_completo_origem = os.path.join(pasta_origem, arquivo)
    caminho_completo_destino = os.path.join(pasta_destino, arquivo)

    try:
        shutil.move(caminho_completo_origem, caminho_completo_destino)
        print(f'File "{arquivo}" moved to "{pasta_destino}"')
    except Exception as e:
        print(f"Error moving file {arquivo}: {e}")

# Display the number of processed files and their information
print(f"Number of files moved: {len(info_arquivos)}")

# Display the stored file information
for arquivo, dados in info_arquivos.items():
    print(f"File: {arquivo}, Created on: {dados[0]}, Size: {dados[1]} bytes")

# Check if a specific file is in the dictionary before accessing it
arquivo_especifico = 'relatorio_0_processado.xlsx'
if arquivo_especifico in info_arquivos:
    print(f"Information for file {arquivo_especifico}: {info_arquivos[arquivo_especifico]}")
else:
    print(f"The file {arquivo_especifico} was not found in the processed list.")
