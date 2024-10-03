import pymongo
import pymongo.errors

# inserir produtos tamanho e cor
def inserir_produto(colecao):
    
    nome = input("Nome do Cliente: ")
    produto = input("Nome do Produto (camisa/calça): ")
    tamanho = input("Tamanho (P, M ou G) ")
    cor = input("Cores (Azul, Preto ou Branco) Escolha imediatamente: ").split("azul,preto,branco")

    documento = {
        "Cliente": nome,
        "Produto": produto,
        "Tamanho": tamanho,
        "Cor": cor

    }

    try:
        inserir = (colecao.insert_one(documento))
        print(f"Produto inserido com sucesso! ID: {inserir}")
    except pymongo.errors.PyMongoError as e:
        print("Deu ruim em inserir produtos: ", e)