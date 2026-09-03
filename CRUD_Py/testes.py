from crud import create
from crud import read

print("CAMPOS:\n Id  -  1\n Nome do Produto  -  2\n Valor  -  3")
campo = input("Digite o o codigo do campo no qual deseja buscar: ")

match campo:
    case 1:
        id = input("Digite o id do produto desejado: ")
        print(create(id))
    case 2:
        nome = input("Digite o nome do produto desejado: ")
        print(create( , nome))
    case 3:
        valor = input("Digite o valor do produto desejado: ")

         

