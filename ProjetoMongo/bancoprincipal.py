import pymongo
import pymongo.errors
import conectarbanco
import inserirprodutos
import listaprodutos
import atualizarproduto
import delete
import buscar


# função menu
def menu():
    conectarbanco.conectar_banco()
    if conectarbanco.conectar_banco is None:
        return

    banco = conectarbanco.conexao ["LojaDoida"]
    colecao = banco["Produtos"]

    while True:
        # exibição do menu
        print("\n=>>= Menu da Loja Doida =<<=")
        print("1. Inserir Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Buscar Produto")
        print("6. Sair")
        opcao = input("Escolha uma opção da Loja Doida: ")

        if opcao == '1':
            inserirprodutos.inserir_produto(colecao)

        elif opcao == '2':
            listaprodutos.listar_produtos(colecao)

        elif opcao == '3':
            atualizarproduto.atualizar_produto(colecao)

        elif opcao == '4':
            delete.deletar_cliente(colecao)

        elif opcao == '5':
            buscar.buscar_produto(colecao)

        elif opcao == '6':
            print("Saindo do programa...")
            break
  
        else:
            print("Opção há essa opção na Loja Doida.")


menu()