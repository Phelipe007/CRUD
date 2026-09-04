from crud import read



def mostrar_resultados(resultado):

    print("\n" * 3 + "=" * 50)
    print(f"{'ID':<5} {'PRODUTO':<25} {'VALOR':>15}")
    print("=" * 50)

    for produto in resultado:
        print(f"{produto[0]:<5} {produto[1]:<33} R$ {produto[2]:>7}")

    print("=" * 50)

print("\n" + "=" * 50)
print(f"{'CAMPOS':>28}")
print("=" * 50)
print(f"{'ID - 1':>5} {'Nome do Produto - 2':>25} {'Valor - 3':>17}")
print("=" * 50)
campo = input("Digite o o codigo do campo no qual deseja buscar: ")

if campo == "1":

    id = input("Digite o id do produto desejado: ")
    resultado = read(id=id)
    mostrar_resultados(resultado)

elif campo == "2":

    nome = input("Digite o nome do produto desejado: ")
    resultado = read(nome=nome)
    mostrar_resultados(resultado)

elif campo == "3":
    while True:
        filtro = input("Deseja pesquisar por filtros? ")
        if filtro == "sim":
            valor_min = int(input("Digite o valor minimo: "))
            valor_max = int(input("Digite o valor maximo: "))
            resultado = read(valor_min=valor_min, valor_max=valor_max)
            mostrar_resultados(resultado)
            break
        elif filtro == "nao":
            valor = int(input("Digite o valor do produto desejado: "))
            resultado = read(valor=valor)
            mostrar_resultados(resultado)
            break
        else:
            print("Digite sim ou nao!!")
            continue
        nova_consulta = input("Deseja fazer uma nova consulta? S / N\n- ")
        if nova_consulta == s:
            continue
        elif nova_consulta == n:
            break