from src.utils_cpf import _sanitize, validate_cpf
from src.logger import log_info, log_error

class CPF:
    def __init__(self, cpf: str):
        self.cpf = _sanitize(cpf)
    
    def _cpf_validator(self) -> bool:
        """
        Valida um CPF verificando se ele atende a todas as regras.
        """
        try:
            if validate_cpf(self.cpf):  # Apenas essa chamada já basta!
                log_info("CPF validado com sucesso")
                return True
            else:
                log_error("CPF inválido")
                return False
        except Exception as error:
            log_error(f"Erro na validação do CPF: {error}")
            return False
