# Organizador de Downloads em Python

Script em Python que organiza automaticamente a pasta de Downloads, movendo cada arquivo para uma pasta específica de acordo com a sua extensão.

## Objetivo

Com o tempo, a pasta de Downloads acumula centenas de arquivos de todos os tipos: PDFs, imagens, instaladores, compactados e muito mais. Este projeto automatiza a limpeza: o script lê cada arquivo, identifica a extensão (por exemplo `.pdf`, `.jpg` ou `.zip`) e move o arquivo para a pasta correspondente (`Documentos`, `Imagens`, `Compactados`...), deixando a pasta principal organizada.

## Exemplo

Antes de executar:

```
Downloads/
├── relatorio.pdf
├── foto.jpg
├── trabalho.zip
└── arquivo.xyz
```

Depois de executar:

```
Downloads/
├── Documentos/
│   └── relatorio.pdf
├── Imagens/
│   └── foto.jpg
├── Compactados/
│   └── trabalho.zip
└── Outros/
    └── arquivo.xyz
```

## Funcionalidades

- **Classificação automática:** organiza os arquivos com base na extensão.
- **Criação de pastas:** cria as pastas de destino (como `Imagens` e `Documentos`) caso ainda não existam.
- **Mapeamento extensivo:** cobre dezenas de tipos de arquivo, incluindo documentos (`.pdf`, `.docx`), planilhas (`.xlsx`), imagens (`.webp`, `.svg`), vídeos (`.mkv`, `.avi`), áudios (`.flac`, `.ogg`), programas (`.exe`) e scripts (`.sh`).
- **Pasta "Outros":** reúne os arquivos com extensões não mapeadas para revisão manual.
- **Regras personalizáveis:** as regras ficam em um dicionário (`mapaDestino`), fácil de editar.

## Tecnologias

Python 3 e apenas bibliotecas nativas:

- `os`: listar arquivos, verificar caminhos e criar pastas.
- `shutil`: mover os arquivos entre pastas.

## Como usar

Testado no **Linux**. O script também deve funcionar no Windows e no macOS, ajustando o caminho da pasta.

### Pré-requisito

- [Python 3](https://www.python.org/downloads/) instalado.

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/isabellazr/python-downloads-organizer.git
   cd python-downloads-organizer
   ```

2. Abra o arquivo `automacaoDownload.py` em um editor de código.

3. Na variável `pastaDownloads`, informe o caminho da sua pasta de Downloads:

   ```python
   # Linux / macOS
   pastaDownloads = r"/home/seu-usuario/Downloads"

   # Windows
   pastaDownloads = r"C:\Users\SeuUsuario\Downloads"
   ```

4. (Opcional) Adicione ou altere as regras no dicionário `mapaDestino`.

5. Execute o script no terminal:

   ```bash
   python automacaoDownload.py
   ```

## Antes de executar

O script **move arquivos de lugar**. Na primeira vez, teste em uma pasta com arquivos de exemplo (apontando `pastaDownloads` para ela) para conferir o resultado antes de usar na sua pasta de Downloads real.

## Melhorias futuras

- Detectar a pasta de Downloads automaticamente, sem precisar editar o caminho.
- Ignorar arquivos em download (por exemplo `.crdownload` e `.part`).
- Gerar um registro (log) dos arquivos movidos.
- Agendar a execução automática (Agendador de Tarefas do Windows).

## Autora

Feito por **Isabella Rodrigues**.

- GitHub: [github.com/isabellazr](https://github.com/isabellazr)
- LinkedIn: [linkedin.com/in/isabellazrodrigues](https://www.linkedin.com/in/isabellazrodrigues/)
