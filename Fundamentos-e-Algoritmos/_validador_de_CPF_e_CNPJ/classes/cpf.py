# Name: main.py
from ..src.utils import _sanitize
CPFLEN = 11

class CPF:
    def __init__(self, cpf : str) -> None:
        """
        Inicializa um objeto CPF, sanitizando o número informado e armazenando os dados.
        """
        self.__cpf = self._sanitize(cpf)
        self.valid = self._cpf_validator()
    

    def _cpf_validator(self) -> bool:
        """
        Valida um CPF verificando se ele tem o tamanho correto e se os dígitos verificadores são válidos.
        """
        try: 
            if not self._len_verifyer():
                return False
            return self.__cpf_validator_digit()

        except Exception as error:
            print(f'Error: {error}')
            
    def _len_verifyer(self) -> bool:
        """
        Verifica se o CPF tem o tamanho correto (11 dígitos)
        """
        return len(self.cpf) == CPFLEN


    def _cpf_validator_digit(self) : 
        """
        Verifica se os dois últimos dígitos do CPF são válidos conforme o cálculo oficial.
        """
        first_digit = self._calculate_digit(self.cpf[:9], 10)
        second_digit = self._calculate_digit(self.cpf[:9] + str(first_digit), 11)
        return self.cpf[-2:] == f"{first_digit}{second_digit}"
    
    def _calculate_digit(self, cpf_part: str, weight: int ) -> int:
        """
        Calcula um dígito verificador do CPF.
        """
        result = sum(int(num) * (weight - i) for i, num in enumerate(cpf_part))
        remainder = result % 11
        return 0 if remainder < 2 else 11 - remainder
     