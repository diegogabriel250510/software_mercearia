from DAO import DAOcategoria, DAOvenda, DAOestoque, DAOfornecedor, DAOpessoa, DAOfuncionario
from Models import Categoria, Estoque, Produto, Fornecedor, Pessoa, Funcionario, Venda
from datetime import datetime

class ControllerCategoria:
   def cadastrarCategoria(self, novaCategoria):
    existe = False
    x = DAOcategoria.ler()
    for i in x:
        if i.categoria == novaCategoria:
            existe = True
   
    if existe == False:
        DAOcategoria.salvar(novaCategoria)
        print('categoria cadastrada com sucesso')
    elif existe == True:
        print("a categoria que deseja cadastrar ja existe")

   def removerCategoria(self, categoriaRemover):
    x = DAOcategoria.ler()
    cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
    if len(cat) <= 0:
        print("a categoria que deseja remover não existe") 
    else:
        for i in range(len(x)):
            if x[i].categoria == categoriaRemover:
                del x[i]
                break
        print('categoria removida com sucesso')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    estoque = DAOestoque.ler()

    estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, "sem categoria", x.produto.preco), x.quantidade)
    if (x.produto.categoria == categoriaRemover) else(x), estoque))

    with open('estoque.txt', "w")as arq:
        for i in estoque:
            arq.writelines(i.produto.nome + "|" + i.produto.categoria + "|" + i.produto.preco + "|" + str(i.quantidade))
            arq.writelines("\n")
   
   def alterarCategoria(self, CategoriaAlterar, CategoriaAlterada):
        x = DAOcategoria.ler()
        
        cat = list(filter(lambda x: x.categoria == CategoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == CategoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(CategoriaAlterada) if(x.categoria == CategoriaAlterar) else(x), x))
                print('categoria foi alterada com sucesso')

                estoque = DAOestoque.ler()

                estoque = list(map(
                    lambda x: Estoque(Produto(x.produto.nome, CategoriaAlterada, x.produto.preco), x.quantidade)
                if (x.produto.categoria == CategoriaAlterar) else(x), estoque))

                with open('estoque.txt', "w") as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.categoria + "|" + i.produto.preco + "|" + str(i.quantidade))
                        arq.writelines("\n")
            
            else:
                print('a categoria para qual deseja alterar ja existe')
        else:
            print('a categoria que deseja alterar não existe')
        
        with open("categoria.txt", "w") as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
   def mostrarCategoria(self):
    categorias = DAOcategoria.ler()
    if len(categorias) == 0:
        print("o arquivo categoria.txt esta vazio")
    else:
        for i in categorias:
            print(f"categoria = {i.categoria}")

class ControllerEstoque:
    def CadastrarProduto(self,nome,preco, categoria, quantidade):
        x = DAOestoque.ler()
        y = DAOcategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria,y))
        est = list(filter(lambda x: x.produto.nome == nome,x))
        if len(h) > 0:
            if len(est) == 0:
                produto = Produto(nome, categoria, preco)
                DAOestoque.salvar(produto, quantidade)
                print("produto cadastrado com sucesso")
            else:
                print("o produto ja existe em estoque")
        else:
            print('categoria inexistente') 

    def RemoverProduto(self, nome):
        x = DAOestoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('produto removido com sucesso')

        else:
            print('o produto que deseja remover não existe')
            
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines("\n")
        
    def AlterarProduto(self, nomealterar, novonome, novopreco, novacategoria, novaquantidade):
        x = DAOestoque.ler()
        y = DAOcategoria.ler()
        h = list(filter(lambda y: y.categoria == novacategoria,y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomealterar,x))
            if len(est) > 0:
                est1 = list(filter(lambda x: x.produto.nome == novonome, x))    
                if len(est1) == 0:
                    x= list(map(lambda x: Estoque(Produto(novonome, novopreco, novacategoria), novaquantidade)if (x.produto.nome == nomealterar) else(x), x))
                    print('o produto foi alterado com suceso')
                else:
                    print('o novo produto ja existe')            
            else:
                print("o produto que voce deseja alterar não existe")
        
            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines('\n')
        else:
            print("a categoria para qual voce deseja alterar não existe")

    def MostrarEstoque(self):
        x = DAOestoque.ler()
        if len(x) == 0:
            print("o estoque esta vazio")
        else:
            for i in x:
                print("==========Produto==========")
                print(f"nome = {i.produto.nome}\n"
                      f"preco = {i.produto.preco}\n"
                      f"categoria = {i.produto.categoria}\n"
                      f"quantidade = {i.quantidade}")

class ControllerVenda:
    def CadastrarVenda(self,nomedoproduto,Vendedor,Comprador,quantidadeVendida):
        x = DAOestoque.ler()
        temp = []
        existe = False
        quantidade = False
        
        for i in x:
            if existe == False:
                if i.produto.nome == nomedoproduto:
                    existe = True
                    if int(i.quantidade) >= int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                    
                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), Vendedor, Comprador, quantidadeVendida)
                        valordacompra = int(quantidadeVendida) * int(i.produto.preco)
                        print("venda realizada com sucesso")
                        DAOvenda.salvar(vendido)
            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])
        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open("estoque.txt", "a") as arq:
                arq.writelines(i[0].nome + "|" + i[0].preco + "|" + i[0].categoria + "|" + str(i[1]))
                arq.writelines("\n")
        if existe == False:
            print("o produto vendido nao existe no estoque")
            return None
        elif not quantidade:
            print("a quantidade vendida nao contem no estoque")
            return None
        else:
            return valordacompra

    def relatorioprodutos(self):
        vendas = DAOvenda.ler()
        produtos = []
        for i in vendas:
            nome = i.ItensVendidos.nome
            quantidade = i.QuantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto' : nome, 'quantidade' : int(x["quantidade"]) + int(quantidade)} if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto' : nome, "quantidade": int(quantidade)})    
            ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse = True)

            print("esses sao os produtos mais vendidos")
            a = 1
            for i in ordenado:
                print(f"==========Produto[{a}]==========")
                print(f"produto: {i['produto']}\n"
                      f"quantidade: {i['quantidade']}\n")
                a += 1

    def mostrarvendas(self,datainicial,datafinal):
        vendas = DAOvenda.ler()
        datainicial1 = datetime.strptime(datainicial, '%d/%m/%Y')
        datafinal1 = datetime.strptime(datafinal, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= datainicial1 and datetime.strptime(x.data, '%d/%m/%Y') <= datafinal1, vendas))

        cont = 1
        total = 0

        for i in vendasSelecionadas:
            print(f"==========venda [{cont}]==========")
            print(f"nome: {i.ItensVendidos.nome}\n"
                  f"categoria: {i.ItensVendidos.categoria}\n"
                  f"data: {i.data}\n"
                  f"quantidade: {i.QuantidadeVendida}\n"
                  f"comprador: {i.comprador}\n"
                  f"vendedor: {i.vendedor}")
            total += int(i.ItensVendidos.preco) * int(i.QuantidadeVendida)     
            cont += 1 
        print(f"preço: {total}")

class ControllerFornecedor:
    def cadastrarfornecedor(self, categoria, nome, cnpj, telefone):
        x = DAOfornecedor.ler()
        listacnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listatelefone = list(filter(lambda x: x.telefone == telefone, x))
        if len(listacnpj) > 0:
            print("o cnpj ja existe")
        elif len(listatelefone) > 0 :
            print("o telefone ja existe")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DAOfornecedor.salvar(Fornecedor(nome,categoria,cnpj,telefone))
                print("fornecedor cadastrado com sucesso")
            else:
                print("digite um cnpj ou um telefone valido")

    def RemoverFornecedor(self,nome):
        x = DAOfornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
                print("o fornecedor foi removido com sucesso")
        else:
            print("o fornecedor que voce deseja remover nao existe")
            return None    

        with open("fornecedores.txt", 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + str(i.categoria) + "|" + i.cnpj + "|" + i.telefone)
                arq.writelines("\n")

    def alterarfornecedor(self,nomealterar, novonome, novocnpj, novotelefone, novacategoria):
        x = DAOfornecedor.ler()
        est = list(filter(lambda x: x.nome == nomealterar, x))
        if len(est) == 0:
            est1 = list(filter(lambda x: x.cnpj == novocnpj, x))
            if len(est1) == 0:
                x = list(map(lambda x: Fornecedor(novonome, novacategoria, novocnpj, novotelefone) if(x.nome == nomealterar) else(x), x))
                print("fornecedor alterado com sucesso")
            else:
                print("o novo cnpj ja existe")
        else:
            print("o fornecedor ja existe")

        with open("fornecedores.txt", "w") as arq:
            for i in x:
               arq.writelines(i.nome + "|" + str(i.categoria) + "|" + i.cnpj + "|" + i.telefone)
               arq.writelines("\n")   

    def mostrarfornecedor(self):
        fornecedores = DAOfornecedor.ler()
        if len(fornecedores) == 0:
            print("lista de fornecedores esta vazia")
        for i in fornecedores:
            print("==========Fornecedor==========")
            print(f"categoria fornecida: {i.categoria}\n"
                  f"nome: {i.nome}\n"
                  f"telefone: {i.telefone}\n"
                  f'cnpj: {i.cnpj}')

class ControllerCliente:
    def cadastrarcliente(self, nome, telefone, cpf, email, endereco):
        x = DAOpessoa.ler()

        listacpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listacpf) > 0:
                print("CPF ja existe")
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DAOpessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print("cliente cadastrado com sucesso")
            else:
                print('digite um cpf ou telefone valido')

    def alterarcliente(self, nomealterar, novonome, novotelefone, novocpf, novoemail, novoendereco):
        x = DAOpessoa.ler()

        est = list(filter(lambda x: x.nome == nomealterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novonome,novotelefone,novocpf,novoemail,novoendereco) if(x.nome == nomealterar) else(x), x))
            print("cliente alterado com sucesso")
        else:
            print("o cliente que voce deseja alterar não existe")
        with open("clientes.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")

    def removercliente(self,nome):
        x = DAOpessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("o cliente que deseja remover não existe")
            return None

        with open("clientes.txt","w")as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("cliente removido com sucesso")

    def mostrarcliente(self):
        x = DAOpessoa.ler()
        if len(x) == 0:
            print("a lista de clientes esta vazia")
        else:
            for i in x:
                print("==========Cliente==========")
                print(f"nome : {i.nome}\n"
                      f"telefone: {i.telefone}\n"
                      f"endereco: {i.endereco}\n"
                      f"email: {i.email}\n"
                      f"cpf: {i.cpf}\n") 

class Controllerfuncionario:
    def cadastrarfuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DAOfuncionario.ler()

        listacpf = list(filter(lambda x: x.cpf == cpf, x))
        listaclt = list(filter(lambda x: x.clt == clt, x))

        if len(listacpf) > 0:
            print("o cpf ja existe")
        elif len(listaclt) > 0:
            print("ja existe um funcionario com esse clt")
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DAOfuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print("funcionario cadastrado com sucesso")
            else:
                print("digite um cpf ou telefone valido")

    def alterarfuncionario(self, nomealterar, novoclt, novonome, novotelefone, novocpf, novoemail, novoendereco):
        x = DAOfuncionario.ler()

        est = list(filter(lambda x: x.nome == nomealterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoclt, novonome, novotelefone, novocpf, novoemail, novoendereco) if(x.nome == nomealterar) else(x), x))
            print("funcionario alterado com sucesso")
        else:
            print("o funcionario que voce deseja alterar nao existe")
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")

    def removerfuncionario(self, nome):
        x = DAOfuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("o funcionario que deseja remover nao existe")
            return None
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("funcionario removido com sucesso")

    def mostrarfuncionario(self):
        x = DAOfuncionario.ler()
        if len(x) == 0:
            print('a lista de funcionario esta vazia')
        else:
            for i in x:
                print("==========FUNCIONARIO==========")
                print(f"nome : {i.nome}\n"
                      f"telefone: {i.telefone}\n"
                      f"endereco: {i.endereco}\n"
                      f"email: {i.email}\n"
                      f"cpf: {i.cpf}\n"
                      f"clt: {i.clt}") 


