import os
import shutil

#Caminho da pasta de downloads
pastaDownloads = r"/home/isabella/Downloads"

#Caminho da pasta de destino
mapaDestino = {

    #Documentos
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".xlsx": "Documentos",
    ".pptx": "Documentos",

    #Imagens
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".bmp": "Imagens",
    ".tiff": "Imagens",
    ".svg": "Imagens",
    ".webp": "Imagens",

    #Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",

    #Musicas
    ".mp3": "Musicas",
    ".wav": "Musicas",
    ".flac": "Musicas",
    ".aac": "Musicas",
    ".ogg": "Musicas",
    ".wma": "Musicas",

    #Compactados
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",
    ".tar": "Compactados",
    ".gz": "Compactados",   

    #Programas
    ".exe": "Programas",
    ".msi": "Programas",
    ".bat": "Programas",
    ".sh": "Programas",

}

pastaOutros = "Outros"


# Verifica se o caminho da pasta Downloads existe
if not os.path.exists(pastaDownloads):
    print(f"Erro: A pasta {pastaDownloads} não foi encontrada.")
    print("Por favor, verifique o caminho e tente novamente.")
    exit() 

print(f"Iniciando organização da pasta {pastaDownloads}...")
arquivos_movidos = 0

# Lista todos os itens (arquivos e pastas) dentro da pastaDownloads
try:
    for item in os.listdir(pastaDownloads):
        # Cria o caminho completo do item 
        caminho_completo_item = os.path.join(pastaDownloads, item)

        # 1. Verifica se é um ARQUIVO (ignora subpastas)
        if os.path.isfile(caminho_completo_item):
            
            # Pega a extensão do arquivo
            # os.path.splitext() divide "arquivo.pdf" em ("arquivo", ".pdf")
            nome_arquivo, extensao = os.path.splitext(item)
            extensao = extensao.lower() # Converte para minúscula (ex: .JPG vira .jpg)

            # Acha a pasta de destino no mapa
            # Usamos .get() para procurar. Se não achar, ele retorna None
            nome_pasta_destino = mapaDestino.get(extensao)

            # Se não achou no mapa, usa a pasta "Outros"
            if nome_pasta_destino is None:
                nome_pasta_destino = pastaOutros
            
            # Cria o caminho completo da pasta de destino
            caminho_pasta_destino = os.path.join(pastaDownloads, nome_pasta_destino)

            # Cria a pasta de destino (se ela não existir)
            # exist_ok=True evita que o programa dê erro se a pasta já existir
            os.makedirs(caminho_pasta_destino, exist_ok=True)

            # Move o arquivo
            try:
                # Move o arquivo da origem (caminho_completo_item) para o destino (caminho_pasta_destino)
                shutil.move(caminho_completo_item, caminho_pasta_destino)
                print(f"  [MOVENDO] {item} -> {nome_pasta_destino}")
                arquivos_movidos += 1
            except Exception as e:
                print(f"  [ERRO] Não foi possível mover {item}: {e}")
                
except Exception as e:
    print(f"Ocorreu um erro ao listar os arquivos: {e}")


print(f"\nOrganização concluída!")
print(f"{arquivos_movidos} arquivos foram movidos.")