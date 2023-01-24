from Models import *

class DAOcategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', "a") as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("categoria.txt", "r") as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ""), cls.categoria))
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat

class DAOvenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', "a") as arq:
            arq.writelines(venda.ItensVendidos.nome + "|" + venda.ItensVendidos.preco + "|" + venda.ItensVendidos.categoria + "|" + venda.vendedor + "|" + venda.comprador + "|" + str(venda.QuantidadeVendida) + "|" + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("venda.txt", "r") as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ""), cls.venda))
        cls.venda = list(map(lambda x: x.split("|"), cls.venda))
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5]))
            
        return vend

class DAOestoque:
    @classmethod
    def salvar(cls, produto:Produto, quantidade):
        with open('estoque.txt', "a") as arq:
            arq.writelines(produto.nome + "|" + produto.categoria + "|" + produto.preco + "|" + str(quantidade))
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("estoque.txt", "r") as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ""), cls.estoque))
        cls.estoque = list(map(lambda x: x.split("|"), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:       
                est.append(Estoque(Produto(i[0],i[1], i[2]), i[3]))
        return est
    
class DAOfornecedor:    
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', "a") as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.categoria + "|" + fornecedor.cnpj + "|" + fornecedor.telefone)
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("fornecedores.txt", "r") as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ""), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split("|"), cls.fornecedores))
        forn = []
        for i in cls.fornecedores:       
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn

class DAOpessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', "a") as arq:
            arq.writelines(pessoa.nome + "|" + pessoa.telefone + "|" + pessoa.cpf + "|" + pessoa.email + "|" + pessoa.endereco)
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("clientes.txt", "r") as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ""), cls.clientes))
        cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))
        client = []
        for i in cls.clientes:       
                client.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return client

class DAOfuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', "a") as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone + "|" + funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("funcionarios.txt", "r") as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ""), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split("|"), cls.funcionarios))
        
        funcionario = []
        for i in cls.funcionarios:       
                funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        
        return funcionario

