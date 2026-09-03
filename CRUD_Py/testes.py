from crud import create
from crud import read
from crud import update
from crud import delete

print("CAMPOS:\n Id  -  1\n Nome do Produto  -  2\n Valor  -  3")
campo = input("Digite o o codigo do campo no qual deseja buscar: ")

if campo == 1:
    id = input("Digite o id do produto desejado: ")
    print(read(id=id))
elif campo == 2:
    nome = input("Digite o nome do produto desejado: ")
    print(read(nome=nome))
elif campo == 3:
    valor = input("Digite o valor do produto desejado: ")
    print(read(valor=valor))
