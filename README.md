# 🔐 Desafio CPF

> Validador e gerador de CPF (Cadastro de Pessoa Física) brasileiro com interface gráfica PyQt5

---

## 📌 Sobre o Projeto

**Desafio CPF** é uma aplicação robusta que valida e gera CPFs brasileiros válidos. O projeto demonstra a aplicação prática de:

- ✅ **Algoritmo de validação** — implementação correta do checksum do CPF
- ✅ **Geração de CPFs** — cria documentos válidos aleatoriamente
- ✅ **Interface gráfica** — PyQt5 com feedback visual intuitivo
- ✅ **Código profissional** — type hints, docstrings, tratamento de erros
- ✅ **Boas práticas** — refatoração, modularização, limpeza de código

---

## 🔐 Como Funciona a Validação de CPF

### Estrutura do CPF

```
XXX.XXX.XXX-XX
├─ Primeiros 9 dígitos: números do CPF
└─ 2 dígitos finais: dígitos verificadores (checksum)
```

### Algoritmo de Validação

**Passo 1: Cálculo do 1º Dígito Verificador**
- Multiplica os primeiros 9 dígitos pelos pesos: [10, 9, 8, 7, 6, 5, 4, 3, 2]
- Soma todos os resultados
- Calcula: resto = soma % 11
- Se resto < 2, dígito = 0; senão, dígito = 11 - resto

**Passo 2: Cálculo do 2º Dígito Verificador**
- Similar ao passo 1, mas usa os primeiros 10 dígitos (9 originais + 1º verificador)
- Pesos: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

**Passo 3: Validação**
- Compara os dígitos calculados com os fornecidos

### Exemplo Prático

```
CPF: 111.444.777-35

Primeiros 9 dígitos: 111444777
Pesos:               10  9  8  7  6  5  4  3  2

Cálculo: (1×10)+(1×9)+(1×8)+(4×7)+(4×6)+(4×5)+(7×4)+(7×3)+(7×2)
       = 10+9+8+28+24+20+28+21+14 = 162

162 % 11 = 8  →  digito = 11 - 8 = 3  ✓ (primeiro dígito é 3)

Primeiros 10 dígitos: 1114447773
Pesos:               11 10  9  8  7  6  5  4  3  2

Cálculo: (1×11)+(1×10)+(1×9)+(4×8)+(4×7)+(4×6)+(7×5)+(7×4)+(7×3)+(3×2)
       = 11+10+9+32+28+24+35+28+21+6 = 204

204 % 11 = 5  →  digito = 11 - 5 = 6  ✓ (segundo dígito é 6)

CPF Válido: 111.444.777-35 ✓
```

---

## 🚀 Como Usar

### Pré-requisitos

```bash
pip install PyQt5
```

### Execução da Interface Gráfica

```bash
python main.py
```

### Uso como Módulo (Terminal)

#### Validar um CPF

```python
from validadorCPF import valida_cpf

# Com formatação
print(valida_cpf('111.444.777-35'))  # True

# Sem formatação
print(valida_cpf('11144477735'))     # True

# CPF inválido
print(valida_cpf('111.444.777-36'))  # False
```

#### Gerar um CPF

```python
from geradorCPF import gera_cpf

# Gerar CPF formatado (padrão)
cpf_formatado = gera_cpf()
print(cpf_formatado)  # Exemplo: 123.456.789-09

# Gerar CPF sem formatação
cpf_sem_formato = gera_cpf(formatado=False)
print(cpf_sem_formato)  # Exemplo: 12345678909
```

---

## 📁 Estrutura do Projeto

```
DesafioCPF/
│
├── validadorCPF.py    # Módulo de validação de CPF
├── geradorCPF.py      # Módulo de geração de CPF válido
├── main.py            # Interface gráfica (PyQt5)
├── design.py          # Layout da interface (gerado automaticamente)
└── README.md          # Documentação
```

---

## 🛠️ Funcionalidades

### ✅ Validador

- Aceita CPF formatado ou sem formatação
- Remove caracteres especiais automaticamente
- Detecta sequências inválidas (111.111.111-11, etc)
- Valida algoritmo de checksum

### ✅ Gerador

- Gera CPFs válidos aleatoriamente
- Retorna formatado ou sem formatação
- Garante que o CPF gerado é válido
- Diversidade: cada execução gera um CPF diferente

### ✅ Interface Gráfica

- Campo de entrada para validar CPF
- Botão para gerar CPF
- Botão para validar CPF
- Feedback visual com cores (verde = sucesso, vermelho = erro)
- Tratamento de erros amigável

---

## 📊 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white)

---

## 📚 Conceitos Aplicados

| Conceito | Descrição | Implementação |
|----------|-----------|---------------|
| **Type Hints** | Anotação de tipos | `def gera_cpf(formatado: bool) -> str` |
| **Docstrings** | Documentação de funções | Cada função tem descrição clara |
| **Modularização** | Separação de responsabilidades | Validação, geração e UI separadas |
| **Tratamento de Erros** | Try/except para robustez | Captura erros e mostra ao usuário |
| **Expressões Regulares** | Limpeza de dados | `re.sub()` para remover caracteres |
| **Reutilização de Código** | DRY - Don't Repeat Yourself | `_calcular_digito()` usada em ambos |
| **Constantes** | Evitar valores mágicos | `PESO_PRIMEIRO_DIGITO`, `PESO_SEGUNDO_DIGITO` |
| **PEP 8** | Padrão Python | Nomes descritivos, formatação correta |

---

## 🔍 Exemplos de Testes

### CPFs Válidos para Teste

```python
valida_cpf('111.444.777-35')  # True
valida_cpf('11144477735')     # True (sem formatação)
```

### CPFs Inválidos para Teste

```python
valida_cpf('111.111.111-11')  # False (sequência)
valida_cpf('111.444.777-36')  # False (dígito inválido)
valida_cpf('123')              # False (muito curto)
valida_cpf('')                 # False (vazio)
```

---

## 🔮 Possíveis Extensões

- [ ] Validação em lote (arquivo CSV)
- [ ] Integração com API de consulta da Receita Federal
- [ ] Histórico de CPFs validados
- [ ] Exportar CPFs gerados para arquivo
- [ ] Testes unitários com pytest
- [ ] API REST com Flask/FastAPI
- [ ] Suporte a CPF de pessoa jurídica (CNPJ)
- [ ] Análise de CPF (qual região, etc)

---

## 🎓 Melhorias Implementadas

Este projeto passou por refatoração profissional:

✅ **Antes**
- Loops complexos com lógica confusa
- Variáveis com nomes pouco descritivos (r, t, l1, l2)
- Sem tratamento de erros
- Sem feedback visual adequado
- Sem type hints ou docstrings

✅ **Depois**
- Código limpo e legível
- Funções bem nomeadas e documentadas
- Tratamento robusto de erros
- Feedback visual intuitivo (cores, mensagens)
- Type hints para melhor compreensão
- Docstrings com exemplos
- Constantes bem definidas
- Modularização clara

---

## 👨‍💻 Autor

**Augusto Matos** — Analista de Dados & Desenvolvedor Python

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/augusto-matos-b92887204)
[![Gmail](https://img.shields.io/badge/Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:augusto.ivan83@outlook.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/augmatos)

---

## 📝 Licença

Este projeto é de código aberto e disponível para fins educacionais.

---

## 🔗 Referências Úteis

- [Validação de CPF - Algoritmo](https://www.gov.br/)
- [Type Hints - Python Docs](https://docs.python.org/3/library/typing.html)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
