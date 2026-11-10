idade=int(input("Digite sua idade: "))
documento=input("Você possui documento : (sim/não): ")

if idade >= 18 and documento in ["sim", "Sim", "SIM"]:
    print("Entrada permitida")
else:
    print("Entrada negada")