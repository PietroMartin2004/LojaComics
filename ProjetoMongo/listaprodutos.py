import pymongo
import pymongo.errors

# Listar produtos no banco
def listar_produtos(colecao):
    try:
        produtos = colecao.find()
        for produto in produtos:
            print(produto)
    except pymongo.errors.PyMongoError as e:
        print("Deu ruim na lista de produtos:", e)
