from src.utils import _len_verifyer, _sanitize, _digits_verifyer
class CNPJ:
    def __init__(self, cnpj):
        """
        Inicializa um objeto CNPJ, sanitizando o número e validando automaticamente.
        """
        self.cnpj = _sanitize(cnpj)
        self.valid = self._cnpj_validator()
        
    def _cnpj_validator(self) -> bool:
        """
        Valida o CNPJ verificando o tamanho e os dígitos verificadores.
        """
        try:
            return _len_verifyer(self.cnpj, "cnpj") and _digits_verifyer(self.cnpj, "cnpj")
        

        
        except Exception as error:
            print(f"Erro na validação do CNPJ: {error}")
            return False
        