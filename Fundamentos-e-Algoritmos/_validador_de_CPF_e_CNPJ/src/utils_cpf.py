from config import CPFLEN

def _sanitize(value: str) -> str:
    """
    Remove caracteres especiais do CPF e retorna apenas números.
    """
    return ''.join(filter(str.isdigit, value)) 

def _len_verifyer(value: str) -> bool:
    """
    Verifica se o CPF tem o tamanho correto (11 dígitos).
    """
    return len(value) == CPFLEN

def _all_digits_equal(value: str) -> bool:
    """
    Verifica se todos os dígitos do CPF são iguais (ex: 000.000.000-00), o que torna o CPF inválido.
    """
    return value == value[0] * len(value)  

def _digit_verifyer(value: str) -> bool:
    """
    Verifica os dígitos verificadores do CPF.
    """
    # Calcula o primeiro dígito verificador
    first_digit = _calculate_digit(value[:9], "cpf")
    # Calcula o segundo dígito verificador
    second_digit = _calculate_digit(value[:9] + str(first_digit), "cpf")
    # Verifica se os dígitos calculados coincidem com os dígitos fornecidos
    return value[-2:] == f"{first_digit}{second_digit}"

def _calculate_digit(base: str, doc_type: str) -> int:
    """
    Calcula um dígito verificador para CPF.
    """
    # Pesos para o cálculo dos dígitos verificadores
    if doc_type == "cpf":
        weights = {
            "first": [10, 9, 8, 7, 6, 5, 4, 3, 2],
            "second": [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        }

    # Seleciona os pesos apropriados
    if len(base) == 9:
        selected_weights = weights["first"]
    elif len(base) == 10:
        selected_weights = weights["second"]
    else:
        raise ValueError("Base length must be 9 or 10 characters for CPF verification")

    # Calcula a soma dos produtos dos dígitos pelos pesos
    total_sum = sum(int(digit) * weight for digit, weight in zip(base, selected_weights))

    # Calcula o dígito verificador
    remainder = total_sum % 11
    if remainder < 2:
        return 0
    else:
        return 11 - remainder

def validate_cpf(value: str) -> bool:
    """
    Função principal de validação do CPF, combinando todas as verificações necessárias.
    """
    cpf = _sanitize(value)

    if not _len_verifyer(cpf):
        return False  # CPF não tem 11 dígitos

    if _all_digits_equal(cpf):
        return False  # CPF com todos os dígitos iguais é inválido

    if not _digit_verifyer(cpf):
        return False  # Dígitos verificadores inválidos

    return True  # CPF válido
