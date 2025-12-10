#!/usr/bin/env python3

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))


operacao = input('Digite a operação desejada (+, -, *, /):')


soma_numero = (num1 + num2)
subtracao_numero = (num1 - num2)
multiplicacao_numero = (num1 * num2)
divisao_numero = (num1 // num2)


if operacao == '+':
  print(soma_numero)
elif operacao == '-':
  print(subtracao_numero)
elif operacao == '*':
  print(multiplicacao_numero)
elif operacao == '/':
  print(divisao_numero)
