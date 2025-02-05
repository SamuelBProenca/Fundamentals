from typing import Dict, Any

BASES: Dict[int, Dict[str, Any]] = {
    1: {"name": "binário", "allowed": "01", "base": 2},
    2: {"name": "decimal", "allowed": "0123456789", "base": 10},
    3: {"name": "hexadecimal", "allowed": "0123456789ABCDEF", "base": 16},
    4: {"name": "octal", "allowed": "01234567", "base": 8},
}

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

class OptionsMenu:
    """
    Classe responsável pela exibição e validação do menu de opções de bases numéricas.
    """
    def __init__(self) -> None:
        self.option_origin: int = 0
        self.option_destination: int = 0

    def display_menu(self, title: str = "Escolha a base") -> int:
        """
        Exibe o menu de opções para bases numéricas e solicita uma opção válida.

        Args:
            title (str, opcional): Título do menu.

        Returns:
            int: Opção válida escolhida pelo usuário.
        """
        print(f"\n{title}:")
        for key, info in BASES.items():
            print(f"{key} - {info['name'].capitalize()}")
        print("5 - Sair")
        return self._get_valid_option()

    def _get_valid_option(self) -> int:
        """
        Solicita e valida a opção digitada pelo usuário.

        Returns:
            int: Opção válida escolhida pelo usuário.
        """
        while True:
            option_str = input("Digite a opção desejada: ")
            try:
                option = int(option_str)
                if option in range(1, 6):
                    return option
                else:
                    print("Opção inválida, tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

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

def main() -> None:
    """
    Função principal do programa que gerencia o fluxo da conversão entre bases.
    """
    menu = OptionsMenu()
    origin_option = menu.display_menu(title="Escolha a base de origem")
    menu.option_origin = origin_option

    raw_value = get_value("Digite o valor a ser convertido: ")

    try:
        validated_value = verify_value(raw_value, origin_option)
    except ValueError as e:
        print(e)
        return

    destination_option = get_base_destination(origin_option, menu)
    menu.option_destination = destination_option

    converted_value = convert_value(validated_value, destination_option)
    print(f"O valor {raw_value} ({BASES[origin_option]['name']}) convertido para {BASES[destination_option]['name']} é: {converted_value}")

if __name__ == "__main__":
    main()