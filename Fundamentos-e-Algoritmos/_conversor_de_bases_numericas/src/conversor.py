#conversor.py
from typing import Dict, Any

BASES: Dict[int, Dict[str, Any]] = {
    1: {"name": "binário", "allowed": "01", "base": 2},
    2: {"name": "decimal", "allowed": "0123456789", "base": 10},
    3: {"name": "hexadecimal", "allowed": "0123456789ABCDEF", "base": 16},
    4: {"name": "octal", "allowed": "01234567", "base": 8},
}


def convert_value(value: int, destination_option: int) -> str:
    """
    Converte um valor para a base de destino escolhida.

    Args:
        value (int): Valor numérico na base de origem.
        destination_option (int): Base de destino.

    Returns:
        str: Representação do valor convertido na base de destino.
    """
    return format(value, {1: 'b', 2: 'd', 3: 'X', 4: 'o'}[destination_option])

