# Validador de CPF e CNPJ

Este projeto é um validador de CPF e CNPJ desenvolvido em Python, seguindo boas práticas e arquitetado para ser próximo de um sistema real. Ele inclui verificação da estrutura dos documentos, cálculo dos dígitos verificadores e consulta de situação cadastral via API.

## Recursos
- **Validação completa de CPF e CNPJ**
- **Sanitização dos dados** (remoção de caracteres não numéricos)
- **Verificação avançada do CNPJ**, incluindo análise dos últimos quatro dígitos
- **Possível integração com APIs para consulta da situação cadastral**
- **Estrutura modular e organizada para facilitar manutenção e expansão**

## Estrutura do Projeto
```
_validador_de_CPF_e_CNPJ/
│── classes/
│   ├── cnpj.py   # Classe para validação de CNPJ
│   ├── cpf.py    # Classe para validação de CPF
│   └── __init__.py
│
│── src/
│   ├── cpf_utils.py        # Funções auxiliares para validação e sanitização
│   ├── cnpj_utils.py        # Funções auxiliares para validação e sanitização
│   ├── logger.py
│   ├── __init__.py
│
│── .env         
│── config.py    # Configurações do projeto (sem informações sensíveis)
│── main.py      # Ponto de entrada principal
```

## Instalação e Uso

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/validador-cpf-cnpj.git
   ```

2. Acesse o diretório do projeto:
   ```sh
   cd validador-cpf-cnpj
   ```

3. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

5. Configure seu arquivo `.env` (se necessário):
   ```sh
   cp .env.example .env
   ```

6. Execute o projeto:
   ```sh
   python main.py
   ```

## Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto.
2. Crie uma branch (`git checkout -b feature-nova`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Envie um push para a branch (`git push origin feature-nova`).
5. Abra um Pull Request.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Observação:** O arquivo `.env` não deve ser versionado! Certifique-se de adicioná-lo ao `.gitignore` para evitar vazamento de dados sensíveis.

