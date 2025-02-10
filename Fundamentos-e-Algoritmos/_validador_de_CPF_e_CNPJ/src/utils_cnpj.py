from datetime import datetime
from config import CNPJLEN

def _sanitize(value: str) -> str:
    """
    Remove caracteres especiais do CNPJ e retorna apenas números.
    """
    return value.replace('.', '').replace('-', '').replace('/', '')

def _len_verifyer(value: str) -> bool:
    """
    Verifica se o CNPJ tem o tamanho correto (14 dígitos).
    """
    return len(value) == CNPJLEN

def _calculate_digit(base: str) -> int:
    """
    Calcula um dos dígitos verificadores do CNPJ.
    """
    weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights_second = [6] + weights_first  # O segundo dígito tem um peso extra 6 no início

    def calculate(numbers, weights):
        total = sum(int(n) * w for n, w in zip(numbers, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    first_digit = calculate(base, weights_first)
    second_digit = calculate(base + str(first_digit), weights_second)

    return first_digit, second_digit

def validate_cnpj(value: str) -> bool:
    """
    Valida um CNPJ verificando:
    1. Se tem 14 dígitos
    2. Se os dígitos verificadores são corretos
    3. Se o sufixo (filial e ano) é coerente (opcional)
    """
    sanitized_cnpj = _sanitize(value)

    # Verifica tamanho
    if not _len_verifyer(sanitized_cnpj):
        return False

    # Verifica dígitos verificadores
    expected_digits = _calculate_digit(sanitized_cnpj[:12])
    if sanitized_cnpj[-2:] != f"{expected_digits[0]}{expected_digits[1]}":
        return False

    return True  # CNPJ válido

