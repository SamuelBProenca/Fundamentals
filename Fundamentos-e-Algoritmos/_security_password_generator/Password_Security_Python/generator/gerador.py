import string
import secrets

MIN_COMPRIMENTO = 8

def generator(comprimento : int = 12, maiusculas : bool = True, numeros : bool = True, especiais : bool = True):
    """
    Gera uma senha aleatória com os parâmetros especificados.
    """
    caracteres = string.ascii_lowercase
    if maiusculas: caracteres += string.ascii_uppercase
    if numeros: caracteres += string.digits
    if especiais: caracteres += string.punctuation
    if comprimento < MIN_COMPRIMENTO: comprimento = MIN_COMPRIMENTO 
    
    password = _generate_pass(comprimento, caracteres)
    return password

def _generate_pass(comprimento, caracteres):
    return ''.join(secrets.choice(caracteres) for _ in range(comprimento))
