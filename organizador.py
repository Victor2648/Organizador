import os
import shutil

# Dicionário que define categorias de arquivos e suas extensões
EXTENSION_MAP = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'videos': ['.mp4', '.avi', '.mov'],
    'music': ['.mp3', '.wav', '.aac'],
    'archives': ['.zip', '.tar', '.rar', '.gz'],
    'scripts': ['.py', '.js', '.html', '.css']
}

# Função que organiza os arquivos de acordo com a extensão
def organize_files(folder_path):
    # Verifica se o diretório base existe
    if not os.path.exists(folder_path):
        print(f'O diretório {folder_path} não existe.')
        return

    # Lista todos os arquivos e diretórios dentro da pasta base
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Verifica se é um arquivo (ignora diretórios)
        if os.path.isfile(file_path):
            # Pega a extensão do arquivo
            _, file_extension = os.path.splitext(filename)

            # Busca a categoria do arquivo
            moved = False
            for category, extensions in EXTENSION_MAP.items():
                if file_extension.lower() in extensions:
                    # Define o diretório de destino
                    dest_folder = os.path.join(folder_path, category)

                    # Cria a pasta se ela não existir
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder)

                    # Move o arquivo para a pasta correspondente
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f'Movido: {filename} -> {dest_folder}')
                    moved = True
                    break
            
            # Caso o arquivo não corresponda a nenhuma categoria, move para 'others'
            if not moved:
                others_folder = os.path.join(folder_path, 'others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f'Movido: {filename} -> {others_folder}')

# Função principal
if __name__ == "__main__":
    # Diretório que será organizado
    directory_to_organize = input("Digite o caminho do diretório que deseja organizar: ")
    
    # Organiza os arquivos no diretório
    organize_files(directory_to_organize)
    print("Organização concluída!")
