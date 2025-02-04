INVALID_INPUT_MSG = "⚠️ Entrada inválida! Por favor, responda com 's' ou 'n'."
MIN_COMPRIMENTO = 8

def getComprimento():
    """
    Solicita o comprimento da senha ao usuário, garantindo que o valor 
    seja um número inteiro válido e maior ou igual ao comprimento mínimo.
    """
    try:
        comprimento = int(input(f"Digite o comprimento da senha (mínimo {MIN_COMPRIMENTO}): "))
    except ValueError:
        print(f"⚠️ Entrada inválida! Por favor, digite um número inteiro maior ou igual a {MIN_COMPRIMENTO}.")
        comprimento = MIN_COMPRIMENTO
    
    return comprimento if comprimento >= MIN_COMPRIMENTO else MIN_COMPRIMENTO

def get_boolean_inputs(prompt):
    """
        Solicita ao usuário uma entrada booleana, garantindo que a resposta seja 's' ou 'n'.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ["s", "n"]: 
            return response == "s"
        print(INVALID_INPUT_MSG)
