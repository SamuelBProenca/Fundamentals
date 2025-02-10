from generator.gerador import generator
from generator.utils import getComprimento, get_boolean_inputs
import pyperclip

def main():
    print("🔐 Gerador de Senhas Seguras 🔐")

    try:
        comprimento = getComprimento()
        maiusculas = get_boolean_inputs("Deseja que seja incluído letras maiúsculas? (s/n): ")
        numeros = get_boolean_inputs("Deseja que seja incluído números? (s/n): ")
        especiais = 'get_boolean_inputs'("Deseja que seja incluído caracteres especiais? (s/n): ")
        
        generated_pass = generator(comprimento, maiusculas, numeros, especiais)
        print(f"🔑 Senha gerada: {generated_pass}")
        pyperclip.copy(generated_pass)

    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")

if __name__ == "__main__":
    main()
