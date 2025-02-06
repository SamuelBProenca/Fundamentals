def _sanitize(value : str) -> int:
    """
    Remove pontos e traços do CPF e retorna apenas numeros
    """
    try:        
        return value.replace('.', '').replace('-', '').replace('/', '')
    except Exception as error:
        print(f"Error: {error}")