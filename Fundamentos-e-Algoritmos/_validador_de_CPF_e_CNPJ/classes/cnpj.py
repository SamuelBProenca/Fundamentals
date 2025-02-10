from src.utils_cnpj import _sanitize, validate_cnpj, _calculate_digit
from src.logger import log_info, log_error

class CNPJ:
    def __init__(self, cnpj: str):
        self.cnpj = _sanitize(cnpj)
    
    def _cnpj_validator(self) -> bool:
        """
        Valida um CNPJ verificando todas as regras.
        """
        try:
            if validate_cnpj(self.cnpj):  # Só essa verificação já basta!
                log_info("CNPJ validado com sucesso")
                return True
            else:
                log_error("CNPJ inválido")
                return False
        except Exception as error:
            log_error(f"Erro na validação do CNPJ: {error}")
            return False
