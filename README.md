Um script simples em Python que organiza automaticamente sua pasta de "Downloads", movendo arquivos para pastas específicas com base em suas extensões.

---

## 🎯 Objetivo do Projeto

Este projeto foi criado para resolver o problema comum de uma pasta de `Downloads` desorganizada. Com o tempo, ela se acumula com centenas de arquivos de todos os tipos (PDFs, imagens, instaladores, etc.).

O script automatiza o processo de limpeza, lendo cada arquivo, verificando sua extensão (ex: `.pdf`, `.jpg`, `.zip`) e movendo-o para um diretório correspondente (ex: `Documentos`, `Imagens`, `Compactados`), mantendo a pasta principal limpa e organizada.

## ✨ Funcionalidades

* **Classificação automática:** Organiza arquivos com base em suas extensões.
* **Criação de Pastas:** Cria automaticamente as pastas de destino (como `Imagens`, `Documentos`, etc.) se elas ainda não existirem.
* **Mapeamento Extensivo:** Inclui um mapa detalhado para dezenas de tipos de arquivos, incluindo documentos (`.pdf`, `.docx`), planilhas (`.xlsx`), imagens (`.webp`, `.svg`), vídeos (`.mkv`, `.avi`), áudio (`.flac`, `.ogg`), programas (`.exe`) e scripts (`.sh`).
* **Arquivos "Outros":** Agrupa todos os arquivos com extensões não mapeadas em uma pasta "Outros" para revisão manual.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído puramente com **Python 3** e suas bibliotecas nativas:

* **`os`**: Para interagir com o sistema operacional (listar arquivos, verificar caminhos, criar pastas).
* **`shutil`**: Para mover os arquivos de um diretório para outro.

## 🚀 Como Usar

Você pode rodar este script localmente em sua máquina.

### Pré-requisitos

* [Python 3](https://www.python.org/downloads/) instalado em seu computador.

### Passos

1.  **Clone este repositório (ou baixe os arquivos):**
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU-USUARIO-GIT]/[NOME-DO-SEU-REPOSITORIO].git
    cd [NOME-DO-SEU-REPOSITORIO]
    ```

2.  **Abra o script:**
    Abra o arquivo `.py` (ex: `organizador.py`) em seu editor de código.

3.  **⚠️ IMPORTANTE: Configure o Caminho ⚠️**
    Na variável `pastaDownloads`, altere o caminho para o caminho **exato** da sua pasta de Downloads:

    ```python
    # Exemplo para Linux/macOS:
    pastaDownloads = r"/home/isabella/Downloads"
    
    # Exemplo para Windows:
    pastaDownloads = r"C:\Users\SeuUsuario\Downloads"
    ```

4.  **(Opcional) Customize as Pastas:**
    Se desejar, você pode adicionar ou alterar as regras no dicionário `mapaDestino`.

5.  **Execute o script:**
    Abra seu terminal, navegue até a pasta onde o script está salvo e rode o comando:
    ```bash
    python nome_do_seu_script.py
    ```

Pronto! Seu script irá rodar e organizar a pasta.

## 👤 Autor

Feito por **Isabella Rodrigues** (Coloque seu nome aqui).

* GitHub: `https://github.com/[SEU-USUARIO-GIT]`
* LinkedIn: https://www.linkedin.com/in/isabellazrodrigues/
