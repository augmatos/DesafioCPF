import re
from typing import Union

PESO_PRIMEIRO_DIGITO = list(range(10, 1, -1))
PESO_SEGUNDO_DIGITO = list(range(11, 1, -1))


def limpar_cpf(cpf: Union[str, int]) -> str:
    """Remove caracteres não-numéricos do CPF."""
    return re.sub(r'[^0-9]', '', str(cpf))


def _calcular_digito(numeros: str, pesos: list) -> str:
    """Calcula um dígito verificador usando pesos específicos."""
    total = sum(int(num) * peso for num, peso in zip(numeros, pesos))
    digito = 11 - (total % 11)
    return '0' if digito > 9 else str(digito)


def _eh_sequencia_invalida(cpf: str) -> bool:
    """Verifica se o CPF é uma sequência inválida (11111111111, etc)."""
    return cpf == cpf[0] * len(cpf)


def valida_cpf(cpf: Union[str, int]) -> bool:
    """
    Valida um CPF brasileiro.

    Args:
        cpf: CPF a ser validado (string ou inteiro, formatado ou não)

    Returns:
        bool: True se o CPF é válido, False caso contrário

    Exemplos:
        >>> valida_cpf('123.456.789-09')
        False
        >>> valida_cpf('11144477700')
        True
    """
    cpf = limpar_cpf(cpf)

    # Validação básica de comprimento
    if not cpf or len(cpf) != 11:
        return False

    # Verifica se é uma sequência inválida
    if _eh_sequencia_invalida(cpf):
        return False

    # Extrai os primeiros 9 dígitos
    numeros = cpf[:9]

    # Calcula o primeiro dígito verificador
    primeiro_digito = _calcular_digito(numeros, PESO_PRIMEIRO_DIGITO)
    numeros += primeiro_digito

    # Calcula o segundo dígito verificador
    segundo_digito = _calcular_digito(numeros, PESO_SEGUNDO_DIGITO)

    # Compara com o CPF fornecido
    cpf_calculado = numeros + segundo_digito
    return cpf == cpf_calculado
