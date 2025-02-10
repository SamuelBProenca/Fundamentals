from classes.cpf import CPF
from classes.cnpj import CNPJ

def main():
    print("___Valide Seu CPF ou Seu CNPJ___")
    try:
        resposta = input("O que deseja validar? (CPF/CNPJ): ").strip().lower()
        
        if resposta == "cnpj":
            newCnpj = input("Digite seu CNPJ: ").strip()
            try:
                cnpj = CNPJ(newCnpj)
                if cnpj._cnpj_validator():
                    print("CNPJ válido!")
                else:
                    print("CNPJ inválido.")
            except Exception as error:
                print(f"Ocorreu um erro na validação do CNPJ: {error}")
        
        elif resposta == "cpf":
            newCpf = input("Digite seu CPF: ").strip()
            try:
                cpf = CPF(newCpf)
                if cpf._cpf_validator():  # <-- Alterado para o método correto
                    print("CPF válido!")
                else:
                    print("CPF inválido.")
            except Exception as error:
                print(f"Ocorreu um erro na validação do CPF: {error}")
        
        else:
            print("Valor inválido. Escolha 'CPF' ou 'CNPJ'.")
    
    except Exception as error:
        print(f"Ocorreu um erro inesperado: {error}. Contate um administrador.")

if __name__ == "__main__":
    main()