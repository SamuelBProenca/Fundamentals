import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Parâmetros do CPF e CNPJ
CPFLEN = 11
CNPJLEN = 14

# Configuração da API da Receita Federal (ou outra API pública)
CNPJ_API_URL = "https://api.receitaws.com.br/v1/cnpj"
CNPJ_API_KEY = os.getenv("CNPJ_API_KEY")  # Chave da API armazenada no .env

# Outros parâmetros do projeto podem ser adicionados aqui
