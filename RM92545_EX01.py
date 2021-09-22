altura = float(input("Informe sua altura: "))
peso = float(input("informe seu peso: "))
imc = 0.00
imc = peso / (altura * altura)

if imc < 16.00:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Baixo peso grau III")
elif imc <= 16.99:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Baixo peso grau II")
elif imc <= 18.49:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Baixo peso grau I")
elif imc <= 24.99:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Peso ideal")
elif imc <= 29.99:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Sobrepeso")
elif imc <= 34.99:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Obesidade grau I")
elif imc <= 39.99:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Obesidade grau II")
else:
    print(f"Seu IMC é: {imc:,.2f} e sua categoria é: Obesidade grau III")











