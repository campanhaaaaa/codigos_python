from Funcionario import Funcionario

f1 = Funcionario("Samuk", "Programador")

print(f" seu nome é {f1.getnome()}")

f1.setnome("Amanda")

print(f" seu nome é {f1.getnome()}")

print(f"Seu cargo é{f1.cargo}")

f1.cargo = "Gerente"
print(f"Seu cargo é{f1.cargo}")


