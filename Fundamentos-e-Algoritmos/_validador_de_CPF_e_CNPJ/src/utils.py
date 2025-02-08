from config import CPFLEN, CNPJLEN

def _sanitize(value : str) -> str:
    """
    Remove pontos e traços do CPF e retorna apenas numeros
    """
    try:        
        return value.replace('.', '').replace('-', '').replace('/', '')
    except Exception as error:
        print(f"Error: {error}")
        return ""
        
def _len_verifyer(value : str, _type : str) -> bool:
    """
        Verifica se o CPF ou CNPJ tem o tamanho correto 
    """
    value = _sanitize(value)
    try:    
        if _type and _type.lower() == "cpf":
            return len(value) == CPFLEN
        elif _type and _type.lower() == "cnpj":
            return len(value) == CNPJLEN
        else:
            print(f"Tipo {_type} não reconhecido.")
            return False
    except Exception as error:
        print(f"Erro : {error}")
        return False  
    
def _digits_verifyer(value : str, _type : str) -> bool:
    value = _sanitize(value)
    
    try:
        if _type.lower() == "cpf":
            first_digit = _calculate_digit(value[:9], "cpf")
            second_digit = _calculate_digit(value[:9] + str(first_digit), "cpf")
            return value[-2:] == f"{first_digit}{second_digit}"
        
        elif _type.lower() == "cnpj":
            first_digit = _calculate_digit(value[:12], "cnpj")
            second_digit = _calculate_digit(value[:12] + str(first_digit), "cnpj")
            return value[-2:] == f"{first_digit}{second_digit}"
        else: 
            print("O tipo ou valor recebidos não é válido.")
            return False
        
    except Exception as error:
        print(f"Erro inesperado : {error}")
        return False

def _calculate_digit(value : str, _type : str ) -> int:
    """
        Calcula um dígito verificador recebendo o valor sanitizado e o tipo "cpf ou cnpj" e fazendo o calculo.
    """
    _sanitize(value)
    if (_type.lower() == "cpf"):
        weight = list(range(10, 1, -1))
    elif (_type.lower() == "cnpj"):
        weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    else:
        print("Tipo inválido")
        return -1
    
    try:
        result = sum(int(num) * weight for num, weight in zip(value, weights))
        remainder = result % 11
        return 0 if remainder < 2 else 11 - remainder
    except Exception as error:
        print(f"Erro no cálculo do dígito: {error}")
        return -1 
    

