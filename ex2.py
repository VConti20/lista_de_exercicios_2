vogal = ["a", "e", "i", "o", "u"]
letra=input("Digite uma letra: ").title()

if letra in vogal:
    print(f"A letra [ {letra} ] é uma vogal")
else:
    print(f"A letra [ {letra} ] NÃO é uma vogal")

