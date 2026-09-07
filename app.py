# consumo-energia em kwh

# Entrada das informações.

input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia do aparelho em watts: " ))
horasDia = int(input("Digite o tempo medio de uso diario em horas: " ))

#Processamento das informações.

Calcule = (potencia * horasDia * 0.75) / 1000

# Saída das informações.

print("O consumo estimado: ", Calcule, "kWH/mês")
