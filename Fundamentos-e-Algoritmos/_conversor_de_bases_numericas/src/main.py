# main.py
from menu import OptionsMenu
from utils import get_value, verify_value, get_base_destination, convert_value
from conversor import convert_value, BASES

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