# Função para calcular a contribuição ao INSS
def calcular_inss(salario_bruto):
    if salario_bruto <= 1212.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2427.35:
        return salario_bruto * 0.09
    elif salario_bruto <= 3641.03:
        return salario_bruto * 0.12
    elif salario_bruto <= 7087.22:
        return salario_bruto * 0.14
    else:
        return 828.39  # Teto do INSS

# Função para calcular o IRRF
def calcular_irrf(salario_liquido):
    if salario_liquido <= 1903.98:
        return 0
    elif salario_liquido <= 2826.65:
        return salario_liquido * 0.075 - 142.80
    elif salario_liquido <= 3751.05:
        return salario_liquido * 0.15 - 354.80
    elif salario_liquido <= 4664.68:
        return salario_liquido * 0.225 - 636.13
    else:
        return salario_liquido * 0.275 - 869.36

# Leitura do salário bruto
salario_bruto = float(input("Digite o valor do salário bruto: "))

# Cálculo da contribuição ao INSS
inss = calcular_inss(salario_bruto)

# Cálculo do salário líquido após a dedução do INSS
salario_liquido = salario_bruto - inss

# Cálculo do desconto do IRRF
irrf = calcular_irrf(salario_liquido)

# Exibição dos resultados
print("Salário Bruto: ", salario_bruto)
print("Contribuição ao INSS: ", inss)
print("Salário Líquido: ", salario_liquido)
print("Desconto do IRRF: ", irrf)
