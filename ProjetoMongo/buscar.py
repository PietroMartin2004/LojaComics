import pymongo
import pymongo.errors

# buscar produto especifico
def buscar_produto(colecao):
    nome = input("Nome do Cliente: ")
    try:
        produto = colecao.find_one({"Cliente": nome})
        if produto:
            print(produto)
        else:
            print("Cliente não encontrado.")
    except pymongo.errors.PyMongoError as e:
        print("Deu ruim em buscar o cliente: ", e)
