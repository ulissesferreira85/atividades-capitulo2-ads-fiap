faturamento = float(input("Informe o faturamento anual: "))
assinatura = input("Informe o tipo de assinatura (BASIC, SILVER, GOLD, PLATINUM): ")
tipo_assinatura = assinatura.upper()
bonus = 0.00

if tipo_assinatura == "BASIC":
    bonus = faturamento * 30 / 100
    print(f"Conta tipo {tipo_assinatura}. O valor do bônus a ser pago é de R$ {bonus:,.2f}")
elif tipo_assinatura == "SILVER":
    bonus = faturamento * 20 / 100
    print(f"Conta tipo {tipo_assinatura}. O valor do bônus a ser pago é de R$ {bonus:,.2f}")
elif tipo_assinatura == "GOLD":
    bonus = faturamento * 10 / 100
    print(f"Conta tipo {tipo_assinatura}. O valor do bônus a ser pago é de R$ {bonus:,.2f}")
elif tipo_assinatura == "PLATINUM":
    bonus = faturamento * 5 / 100
    print(f"Conta tipo {tipo_assinatura}. O valor do bônus a ser pago é de R$ {bonus:,.2f}")
else:
    print("Tipo de assinatura inválida!")


