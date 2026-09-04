from crud import create

print("Bem vindo a Interface de controle de vendas!!")
verificador = input("Deseja cadastrar uma nova venda?      - sim       - nao\n- ")

while True:
    if verificador == "sim":
        print("Preecha os dados da venda!")
        nome = input("Nome do produto: ")
        valor = input("Valor do produto: ")
        if create(nome=nome, valor=valor) is True:
            print("Cadastro Realizado Com Sucesso!!")
            break
        else:
            print("Cadastro não realizado!!")
            nova_tentativa = input("Deseja tentar novamente? ")
            if nova_tentativa == "sim":
                continue
            else:
                break
    elif verificador == "nao":
        print("Encerrando interface!!")
        break
    else:
        print("Digite   - sim ou - nao")
        verificador = input("- ")
        continue
