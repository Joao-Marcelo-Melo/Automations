import os
import time
import pandas as pd

pattern = ".xlsx"
dir_start = r"C:\Users\Marcelo\Downloads"
dir_end = r"C:\Users\Marcelo\Desktop\Planilhas-Jettax"

files_processed = []

while True:
    for file in os.listdir(dir_start):
        if file.endswith(pattern) and file not in files_processed:
            path_start = os.path.join(dir_start, file)
            path_end = os.path.join(dir_end, file)
            os.rename(path_start, path_end)
            
            df = pd.read_excel(path_end)
            colums_to_delete = [
                'Obrigação / Tarefa ',
                'Tipo ',
                'Cidade ',
                'Estado ',
                'Prazo legal ',
                'Prazo Técnico ',
                'Data da entrega ',
                'Status ',
                'Departamento ',
                'Responsável prazo ',
                'Responsável entrega ',
                'Competência ',
                'Protocolo '
            ]
            df = df.drop(columns=colums_to_delete, axis=1)

            new_file = os.path.join(dir_end, file)
            df.to_excel(path_end, index=False)
            files_processed.append(file)

    time.sleep(5)