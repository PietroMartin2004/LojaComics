import pymongo
import pymongo.errors

# conectar banco
def conectar_banco():
    try:
        global conexao
        conexao = pymongo.MongoClient("mongodb+srv://PMART:Abacaxy3560@pmart.xnmtt.mongodb.net/")
    except pymongo.errors.ConnectionError as e:
        print("Deu ruim na conexão:", e)
    return None