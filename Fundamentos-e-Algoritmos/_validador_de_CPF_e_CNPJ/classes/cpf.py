# Name: cpf.py
from src.utils import _sanitize, _len_verifyer, _digits_verifyer
CPFLEN = 11

class CPF:
    def __init__(self, cpf : str) -> None:
        """
        Inicializa um objeto CPF, sanitizando o número informado e armazenando os dados.
        """
        self.__cpf = _sanitize(cpf)
        self.valid = self._cpf_validator()

    def _cpf_validator_digit(self) -> bool: 
        """
        Verifica se os dois últimos dígitos do CPF são válidos conforme o cálculo oficial.
        """
        try:
            _len_verifyer(self.__cpf) and _digits_verifyer(self.__cpf, "cpf")
        except Exception as error:
            print(f"Erro na validação do CPF: {error}")
            return False
        
