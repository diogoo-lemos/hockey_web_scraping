# Hockey Web Scraping & Tableau Dashboard

Um projeto completo de extração de dados (*Web Scraping*) e visualização focada no Campeonato Placard de Hóquei em Patins. Este repositório contém os scripts em Python para recolher as estatísticas diretamente da web e o ficheiro Tableau (`Hockey.twb`) para exploração visual dos dados.

## Objetivo
O objetivo principal deste projeto é automatizar a extração das tabelas de classificação, plantéis das equipas e lista de goleadores do site [hoqueipatins.pt](https://www.hoqueipatins.pt). O script transforma o código HTML bruto das páginas em ficheiros Excel limpos e estruturados. Estes ficheiros servem como base de dados relacional para alimentar uma dashboard interativa no Tableau, permitindo cruzar métricas como a eficiência individual dos jogadores e o sucesso coletivo das equipas.

## Funcionalidades
- **Classificação da 1ª Divisão:** Extração automática dos pontos, jogos, vitórias, empates, derrotas e golos (marcados e sofridos) de todas as equipas.
- **Top Goleadores:** Recolha do ranking dos melhores marcadores do campeonato, cruzando o número de golos com a média por jogo.
- **Plantéis Detalhados:** Scraping direcionado para as páginas individuais de cada equipa para identificar os jogadores que compõem os respetivos plantéis.
- **Integração com Tableau:** O ficheiro `Hockey.twb` permite visualizar os dados de forma interativa.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Bibliotecas Python:** `pandas`, `requests`, `beautifulsoup4`, `openpyxl`
* **Visualização de Dados:** Tableau 

## Estrutura do Repositório
* `src/` - Contém o código-fonte em Python responsável pelo web scraping dos dados.
* `Hockey.twb` - O *workbook* do Tableau com as dashboards e gráficos construídos a partir dos dados recolhidos.
* `README.md` - Documentação principal do projeto.

## Como Executar o Projeto

### 1. Instalar Dependências

```bash
pip install pandas requests beautifulsoup4 openpyxl
