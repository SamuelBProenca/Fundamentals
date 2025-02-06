# menu.py
from conversor import convert_value, BASES

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
