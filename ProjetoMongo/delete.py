import pymongo
import pymongo.errors

# deletar um produto
def deletar_cliente(colecao):
    nome = input("Nome do Cliente que deseja Deletar: ")
    try:
        resultado = colecao.delete_one({"Cliente": nome})
        if resultado.deleted_count > 0:
            print("Cliente deletado com sucesso!")
        else:
            print("Cliente não encontrado.")
    except pymongo.errors.PyMongoError as e:
        print("Deu ruim no delete:", e)
