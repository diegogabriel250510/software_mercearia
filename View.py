import Controller
import os.path

def criaArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")


criaArquivos(
    "categoria.txt", "clientes.txt", 
    "estoque.txt", "fornecedores.txt",
    "funcionarios.txt","venda.txt")



if __name__ == "__main__":
    while True:
        local = int(input("digite 1 para acessar ( categorias )\n"
                          "digite 2 para acessar ( estoque )\n"
                          "digite 3 para acessar ( fornecedor )\n"
                          "digite 4 para acessar ( cliente )\n"
                          "digite 5 para acessar ( funcionario )\n"
                          "digite 6 para acessar ( vendas )\n"
                          "digite 7 para ver os produtos mais vendidos\n"
                          "digite 8 para sair\n"))
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("digite 1 para cadastrar uma categoria\n"
                               "digite 2 para remover categoria\n"
                               "digite 3 para alterar uma categoria\n"
                               "digite 4 para mostrar as categorias cadastradas\n"
                               "digite 5 para sair\n"))
                        
                if decidir == 1:
                    categoria = input("digite a categoria que deseja cadastrar\n")
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input("digite a categoria que deseja remover\n")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoriaalterar = input("digite a categoria que voce deseja alterar\n")
                    categoriaalterada = input("digite a categoria ja alterada\n")
                    cat.alterarCategoria(categoriaalterar,categoriaalterada)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break
        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("digite 1 para cadastrar um produto\n"
                                    "digite 2 para remover um produto \n"
                                    "digite 3 para alterar um produto\n"
                                    "digite 4 para ver o estoque\n"
                                    "digite 5 para sair\n"))
                if decidir == 1:
                    produto = input("digite o produto que deseja cadastrar\n")
                    preco = input("digite o preco do produto: \n")
                    categoria = input("digite a categoria do produto: \n")
                    quantidade = input("digite a quantidade que tem no estoque: \n")
                    cat.CadastrarProduto(produto,preco,categoria,quantidade)
                elif decidir == 2:
                    produto = input("digite o produto que deseja remover\n")
                    cat.RemoverProduto(produto)
                elif decidir == 3:
                    produto = input("digite o produto que deseja alterar\n")
                    produtoalterado = input("digite o produto alterado\n")
                    novopreco = input("digite o novo preco do produto\n")
                    novacategoria = input("digite a nova categoria do produto\n")
                    novaquantidade = input("digite a nova quantidade que tem no estoque\n")
                    cat.AlterarProduto(produto,produtoalterado,novopreco,novacategoria,novaquantidade)
                elif decidir == 4:
                    cat.MostrarEstoque()
                else:
                    break
        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("digite 1 para cadastrar um fornecedor\n"
                                    "digite 2 para remover um fornecedor\n"
                                    "digite 3 para alterar um fornecedor\n"
                                    "digite 4 para mostrar os fornecedores\n"
                                    "digite 5 para sair\n"))
                if decidir == 1:
                    fornecedor = input("nome do fornecedor: \n")
                    categoria = input("categoria fornecida: \n")
                    telefone = input("digite o telefone do fornecedor (10 ou 11 carceteres): \n")
                    cnpj = input("digite o cnpj do fornecedor (14 caracteres): \n")
                    cat.cadastrarfornecedor(categoria,fornecedor,cnpj,telefone)
                elif decidir == 2:
                    fornecedor = input("digite o fornecedor que deseja remover: \n")
                    cat.RemoverFornecedor(fornecedor)
                elif decidir == 3:
                    nomealterar = input("digite o fornecedor que deseja alterar: \n")
                    novonome = input("digite o nome do fornecedor alterado: \n")
                    novocnpj = input("digite o novo cnpj (14 caracteres): \n")
                    novotelefone = input("digite o novo telfone (11 ou 10 caracteres): \n")
                    novacategoria = input("digite a nova categoria: \n")
                    cat.alterarfornecedor(nomealterar,novonome,novocnpj,novotelefone, novacategoria)
                elif decidir == 4:
                    cat.mostrarfornecedor()
                else:
                    break
        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input("digite 1 para cadastrar um cliente\n"
                                    "digite 2 para remover um cliente\n"
                                    "digite 3 para alterar um cliente\n"
                                    "digite 4 para mostrar os clientes\n"
                                    "digite 5 para sair\n"))
                if decidir == 1:
                    nome = input("digite o nome do cliente: \n")
                    telefone = input("digite o telefone do cliente(11 ou 10 caracteres): \n")
                    cpf = input("digite o cpf do cliente (11 caracteres): \n")
                    email = input("digite o email do cliente: \n")
                    endereco = input("digite o endereco do cliente: \n")
                    cat.cadastrarcliente(nome,telefone,cpf,email,endereco)
                elif decidir == 2:
                    nome = input("digite o cliente que deseja remover: \n")
                    cat.removercliente(nome)
                elif decidir == 3:
                    nomealterar = input("digite o nome que voce deseja alterar: \n")
                    novonome = input("digite o novo nome do cliente: \n")
                    novotelefone = input("digite o novo telefone (11 ou 10 caracteres): \n")
                    cpf = input("digite o novo cpf (11 caracteres): \n")
                    novoemail = input("digite o novo email: \n")
                    novoendereco = input("digite o novo endereco: \n")
                    cat.alterarcliente(nomealterar,novonome,novotelefone,cpf,novoemail,novoendereco)
                elif decidir == 4:
                    cat.mostrarcliente()
                else:
                    break
        elif local == 5:
            cat = Controller.Controllerfuncionario()
            while True:
                decidir = int(input("digite 1 para cadastrar um funcionario\n"
                                    "digite 2 para remover um funcionario\n"
                                    "digite 3 para alterar um funcionario\n"
                                    "digite 4 para mostrar os funcionarios\n"
                                    "digite 5 para sair\n"))
                if decidir == 1:
                    clt = input("digite o clt do funcionario: \n")
                    nome = input("digite o nome do funcionario: \n")
                    telefone = input("digite o telefone do funcionario(11 ou 10 caracteres): \n")
                    cpf = input("digite o cpf do funcionario(11 caracteres): \n")
                    email = input("digite o email do funcionario: \n")
                    endereco = input("digite o endereco do funcionario: \n")
                    cat.cadastrarfuncionario(clt,nome,telefone,cpf,email,endereco)
                elif decidir == 2:
                    nome = input("digite o funcionario que deseja remover: \n")
                    cat.removerfuncionario(nome)
                elif decidir == 3:
                    nomealterar = input("digite o nome que voce quer alterar: \n")
                    novoclt = input("digite o novo clt do funcionario: \n")
                    novonome = input("digite o novo nome do funcionario: \n")
                    novotelefone = input("digite o novo telefone do funcionario(11 ou 10 caracteres): \n")
                    novocpf = input("digite o novo cpf do funcionario(11 caracteres): \n")
                    novoemail = input("digite o novo email do funcionario: \n")
                    novoendereco = input("digite o novo endereco do funcionario: \n")
                    cat.alterarfuncionario(nomealterar,novoclt,novonome,novotelefone,novocpf,novoemail,novoendereco)
                elif decidir == 4:
                    cat.mostrarfuncionario()
                else:
                    break
        elif local == 6:
            cat = Controller.ControllerVenda()
            decidir = int(input("digite 1 para realizar uma venda\n"
                                "digite 2 para ver as vendas\n"
                                "digite 3 para sair\n"))
            if decidir == 1:
                nomedoproduto = input("digite o nome do produto vendido: \n")
                vendedor = input("digite o vendedor da compra: \n")
                comprador = input("digite quem foi que comprou: \n")
                quantidadevendida = input("diga quantos produtos foi vendidos: \n")
                cat.CadastrarVenda(nomedoproduto,vendedor,comprador,quantidadevendida)
            elif decidir == 2:
                datainicial = input("datainicial: ")
                datafinal = input("datafinal: ")
                cat.mostrarvendas(datainicial, datafinal)
            else:
                break
            

        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioprodutos()
        else:
            break
