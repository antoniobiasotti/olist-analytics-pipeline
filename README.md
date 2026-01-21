# Olist Analytics Pipeline

Projeto de análise de dados construído do zero a partir do dataset público de e-commerce da Olist, com foco em simular um fluxo real de trabalho em dados.

## Objetivo
Reproduzir um pipeline analítico completo em ambiente local, contemplando:
- Ingestão de dados brutos
- Armazenamento em um warehouse analítico
- Análises utilizando SQL e Python
- Geração de insights orientados a negócio

## Tecnologias utilizadas
- Python
- Pandas
- DuckDB
- SQL

## Estrutura do projeto
- `data/raw`: arquivos CSV originais (não versionados)
- `data/processed`: dados tratados e intermediários
- `data/warehouse`: banco analítico local (DuckDB)
- `src`: scripts de ingestão e transformação
- `notebooks`: análises exploratórias
- `docs`: documentação de apoio

## Execução do projeto
1. Fazer o download do dataset **Olist Brazilian E-Commerce Public Dataset** no Kaggle
2. Extrair os arquivos CSV para o diretório `data/raw`
3. Criar e ativar um ambiente virtual Python
4. Instalar as dependências do projeto
5. Executar o script de ingestão dos dados
