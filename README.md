# 🗃️ Organizador de Arquivos Inteligente em Python

Este projeto é uma ferramenta escrita em Python que organiza automaticamente os arquivos de uma pasta, movendo-os para subpastas de acordo com suas extensões. É ideal para manter sua pasta de **Downloads** (ou outra) organizada, melhorando a produtividade e a organização dos seus arquivos.

## ⚙️ Funcionalidades

- Organiza arquivos por extensão (ex.: .pdf, .jpg, .zip, etc.)
- Cria subpastas automaticamente se não existirem
- Configurável através de um arquivo JSON (`config.json`)
- Exibe mensagens no terminal informando as ações realizadas

## 🧠 Como funciona

1. Configure as regras de organização no arquivo `config.json`.
2. Execute o script informando a pasta a ser organizada.
3. O script verifica a extensão de cada arquivo e move-o para a subpasta correspondente.

## 🚀 Como usar

### Pré-requisitos:
- Python 3 instalado
- Git (caso deseje clonar o repositório)

### Passos para executar:

1. **Clonar o repositório (opcional)**:
   ```bash
   git clone https://github.com/seunome/organizador-de-arquivos-python.git
   cd organizador-de-arquivos-python
