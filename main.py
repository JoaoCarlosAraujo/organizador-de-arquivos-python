# main.py
import os        # Módulo para interagir com o sistema operacional (acessar arquivos, pastas, etc.)
import shutil    # Módulo para operações de cópia e movimentação de arquivos
import argparse  # Módulo para ler argumentos do terminal
import json      # Módulo para trabalhar com arquivos JSON (usado para ler a configuração)

def carregar_configuracao(caminho_config="config.json"):
    """
    Lê o arquivo de configuração (JSON) e retorna as regras de organização.
    
    Parâmetros:
      caminho_config (str): Caminho para o arquivo JSON que contém as regras.
      
    Retorna:
      dict: Dicionário com as regras de extensão: nome da pasta.
    """
    with open(caminho_config, "r", encoding="utf-8") as f:
        return json.load(f)

def organizar_arquivos(pasta, regras):
    """
    Organiza os arquivos da pasta conforme as regras de extensão passadas.
    
    Parâmetros:
      pasta (str): Caminho da pasta onde os arquivos serão organizados.
      regras (dict): Regras de organização, onde a chave é a extensão e o valor é o nome da subpasta.
    """
    # Lista todos os arquivos e pastas na pasta informada
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        # Se for um arquivo (e não uma subpasta)
        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)  # Separa o nome e a extensão do arquivo
            # Verifica se a extensão do arquivo está definida nas regras
            if extensao in regras:
                # Define o destino (subpasta) baseado na regra
                destino = os.path.join(pasta, regras[extensao])
                # Cria a subpasta se ela não existir
                os.makedirs(destino, exist_ok=True)
                # Define o caminho final para onde o arquivo será movido
                novo_caminho = os.path.join(destino, arquivo)
                # Move o arquivo para o novo destino
                shutil.move(caminho_arquivo, novo_caminho)
                # Exibe uma mensagem no terminal indicando a ação realizada
                print(f"Movido: {arquivo} para {destino}")

def main():
    # Cria um parser para receber argumentos via linha de comando
    parser = argparse.ArgumentParser(description="Organizador de Arquivos")
    parser.add_argument("--pasta", required=True, help="Caminho da pasta a ser organizada")
    args = parser.parse_args()

    # Carrega as regras de organização a partir do arquivo de configuração
    regras = carregar_configuracao()
    # Chama a função que organiza os arquivos
    organizar_arquivos(args.pasta, regras)

# A partir deste ponto, o script é executado diretamente
if __name__ == "__main__":
    main()
