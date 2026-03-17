import pandas as pd
import requests
from io import StringIO

def extrair_dados_hoquei():
    url = "https://www.hoqueipatins.pt/liga/1-divisao-regular/"
    
    # Adicionar um User-Agent ajuda a evitar que o site bloqueie o nosso pedido
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    print("A aceder à página...")
    resposta = requests.get(url, headers=headers)
    
    # Verificar se a ligação foi bem sucedida
    if resposta.status_code != 200:
        print(f"Erro ao aceder à página. Código: {resposta.status_code}")
        return
        
    print("A procurar tabelas de classificação...")
    # O pandas lê todas as tabelas presentes no código HTML
    tabelas = pd.read_html(StringIO(resposta.text))
    
    df_classificacao = None
    
    # Procurar a tabela correta (a que tem 'Equipa' e 'PTS' no cabeçalho)
    for tabela in tabelas:
        if 'Equipa' in tabela.columns and 'PTS' in tabela.columns:
            df_classificacao = tabela
            break
            
    if df_classificacao is not None:
        # Definir as colunas que realmente interessam para o Tableau
        # PTS: Pontos, JOG: Jogos, VIT: Vitórias, EMP: Empates, DER: Derrotas
        # GM: Golos Marcados, GS: Golos Sofridos
        colunas_desejadas = ['Equipa', 'PTS', 'JOG', 'VIT', 'EMP', 'DER', 'GM', 'GS']
        
        # Filtrar apenas as colunas que encontrámos e remover linhas que não tenham nome de equipa
        colunas_finais = [col for col in colunas_desejadas if col in df_classificacao.columns]
        df_limpo = df_classificacao[colunas_finais].copy()
        
        # Limpar linhas vazias (onde a coluna Equipa seja NaN)
        df_limpo = df_limpo.dropna(subset=['Equipa'])
        
        # Exportar os dados para um ficheiro Excel
        nome_ficheiro = 'classificacao_hoquei_1divisao.xlsx'
        df_limpo.to_excel(nome_ficheiro, index=False, engine='openpyxl')
        
        print(f"Sucesso! Os dados foram guardados no ficheiro: '{nome_ficheiro}'.")
        print("\nPré-visualização dos dados recolhidos:")
        print(df_limpo.head()) # Mostra as primeiras 5 equipas
        
    else:
        print("Não foi possível encontrar a tabela com os dados das equipas.")

def extrair_goleadores():
    url = "https://www.hoqueipatins.pt/goleadores-do-campeonato-placard-2024-25/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    print("A aceder à página dos Goleadores...")
    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code != 200:
        print(f"Erro ao aceder à página. Código: {resposta.status_code}")
        return
        
    # O pandas extrai as tabelas
    tabelas = pd.read_html(StringIO(resposta.text))
    df_goleadores = None
    
    # Procurar a tabela que tenha a coluna 'Equipa' ou um grande número de colunas (típico desta tabela)
    for tabela in tabelas:
        if 'Equipa' in tabela.columns or len(tabela.columns) > 10:
            df_goleadores = tabela
            break
            
    if df_goleadores is not None:
        try:
            # Selecionar apenas as 6 primeiras colunas (Rank, Jogador, Equipa, Golos, Média, Jogos)
            # Isto contorna o problema de o HTML ter ícones no lugar de texto no cabeçalho
            df_limpo = df_goleadores.iloc[:, :6].copy()
            
            # Forçar os nomes corretos das colunas para o Tableau
            df_limpo.columns = ['Rank', 'Jogador', 'Equipa', 'Golos', 'Media_Golos', 'Jogos']
            
            # Limpar linhas que possam ter vindo vazias ou ser lixo do HTML
            df_limpo = df_limpo.dropna(subset=['Jogador', 'Golos'])
            
            # Exportar para Excel
            nome_ficheiro = 'goleadores_campeonato_placard.xlsx'
            df_limpo.to_excel(nome_ficheiro, index=False, engine='openpyxl')
            
            print(f"Sucesso! Dados dos goleadores guardados no ficheiro: '{nome_ficheiro}'.")
            print("\nPré-visualização dos Goleadores:")
            print(df_limpo.head())
            print("\n")
        except Exception as e:
            print(f"Erro ao processar a tabela de goleadores: {e}")
    else:
        print("Não foi possível encontrar a tabela de goleadores.\n")

if __name__ == "__main__":
    extrair_goleadores()
    extrair_dados_hoquei()
   
