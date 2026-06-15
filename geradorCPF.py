from random import randint
from typing import Tuple

PESO_PRIMEIRO_DIGITO = list(range(10, 1, -1))
PESO_SEGUNDO_DIGITO = list(range(11, 1, -1))


def _calcular_digito(numeros: str, pesos: list) -> str:
    """Calcula um dígito verificador usando pesos específicos."""
    total = sum(int(num) * peso for num, peso in zip(numeros, pesos))
    digito = 11 - (total % 11)
    return '0' if digito > 9 else str(digito)


def gera_cpf(formatado: bool = True) -> str:
    """
    Gera um CPF válido e aleatório.

    Args:
        formatado: Se True, retorna no formato XXX.XXX.XXX-XX. Se False, retorna sem formatação.

    Returns:
        str: CPF gerado e validado

    Exemplos:
        >>> cpf = gera_cpf()
        >>> len(cpf.replace('.', '').replace('-', ''))
        11
        >>> cpf_sem_formato = gera_cpf(formatado=False)
        >>> len(cpf_sem_formato)
        11
    """
    # Gera 9 números aleatórios
    numeros = str(randint(100000000, 999999999))

    # Calcula o primeiro dígito verificador
    primeiro_digito = _calcular_digito(numeros, PESO_PRIMEIRO_DIGITO)
    numeros += primeiro_digito

    # Calcula o segundo dígito verificador
    segundo_digito = _calcular_digito(numeros, PESO_SEGUNDO_DIGITO)
    cpf_completo = numeros + segundo_digito

    if formatado:
        return f"{cpf_completo[0:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:11]}"
    else:
        return cpf_completo
