import pymongo
import pymongo.errors

# atualizar produto
def atualizar_produto(colecao):
    nome = input("Nome Cliente que deseja Atualizar: ")
    produto_existente = colecao.find_one({"Cliente": nome})

    if produto_existente:
        novo_tamanho = input("Novo tamanho (P, M ou G): ")
        nova_cores = input("Novas cor (Azul, Preto ou Branco): ")

        # atualização dos produtos preenchidos
        atualizacao = {}
        if novo_tamanho:
            atualizacao["Tamanho"] = novo_tamanho
        if nova_cores:
            atualizacao["Cor"] = nova_cores.split(",")

        if atualizacao:
            try:
                colecao.update_one({"Cliente": nome}, {"$set": atualizacao})
                print("Produto atualizado com sucesso!")
            except pymongo.errors.PyMongoError as e:
                print("Deu ruim em atualizar o produto: ", e)
        else:
            print("Nenhuma atualização foi realizada.")
    else:
        print("Produto não encontrado.")
