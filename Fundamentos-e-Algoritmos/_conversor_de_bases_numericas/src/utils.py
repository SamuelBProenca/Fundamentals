#utils.py
from menu import OptionsMenu
from conversor import convert_value, BASES

def get_value(message: str) -> str:
    """
    Solicita ao usuário que digite um valor.

    Args:
        message (str): Mensagem a ser exibida.

    Returns:
        str: Valor digitado pelo usuário.
    """
    return input(message)

def verify_value(value: str, option: int) -> int:
    """
    Verifica se o valor digitado é válido de acordo com a base escolhida e o converte para inteiro.

    Args:
        value (str): Valor digitado.
        option (int): Base escolhida.

    Raises:
        ValueError: Se o valor não for válido para a base escolhida.

    Returns:
        int: Valor convertido para inteiro.
    """
    info = BASES.get(option)
    if info is None:
        raise ValueError("Opção de base inválida.")
    if not all(ch in info["allowed"] for ch in value.upper()):
        raise ValueError(f"⚠️ O valor digitado {value} não é um número {info['name']}. Por favor, tente novamente.")
    return int(value, info["base"])


def get_base_destination(origin_option: int, menu: OptionsMenu) -> int:
    """
    Solicita ao usuário a base de destino e verifica se é diferente da base de origem.

    Args:
        origin_option (int): Base de origem escolhida.
        menu (OptionsMenu): Instância do menu para reutilizar a exibição.

    Returns:
        int: Base de destino escolhida.
    """
    while True:
        destination_option = menu.display_menu(title="Escolha a base de destino")
        if destination_option != origin_option:
            return destination_option
        print("A base de destino deve ser diferente da origem. Tente novamente.")
