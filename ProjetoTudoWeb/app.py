# Programa de pesquisa sobre opinião da satisfação de 50 clientes no atendimento da TudoWeb.
# 1.Contadores de pesquisa
excelente = 0
bom = 0
ruim = 0

# 2.Roteiro para receber a opinião de 50 clientes.

for i in range(1, 50):
    print(f"Cliente {i}:")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a idade: "))
    opiniao = input("Digite a opinião sobre o atendimento (excelente, bom, ruim): ")

    # Imprimi os dados do cliente atual
    print(f"Nome: {nome}, Idade: {idade}, Opinião: {opiniao}")

    # Atualizar contadores com base na opinião
    if opiniao == "excelente":
        excelente += 1
    elif opiniao == "bom":
        bom += 1
    elif opiniao == "ruim":
        ruim += 1

# Imprimir os resultados finais
print(f"Quantidade de clientes com opinião excelente: {excelente}")
print(f"Quantidade de clientes com opinião boa: {bom}")
print(f"Quantidade de clientes com opinião ruim: {ruim}")
