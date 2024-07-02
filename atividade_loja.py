usuarios = [{'nome': 'LOIDI', 'email': 'admin@gmail.com', 'senha': 1425, 'admin': True},{'nome': 'LOIDI', 'email': 'loidi@gmail.com', 'senha': 1425, 'admin': False}] 
produtos = [{'nome': 'ARROZ', 'preco': 30, 'qtd': 10},{'nome': 'FEIJÃO', 'preco': 5, 'qtd': 15}]
carrinho = [{'nome':'ARROZ','qtd':2,'preco_unitario':30,'preco_total':60},{'nome':'FEIJÃO','qtd':3,'preco_unitario':5,'preco_total':15}]
historico_compras = []

def cadastrar_usuario(nome, email, senha, admin=False):
    usuarios.append({'nome': nome, 'email': email, 'senha': senha, 'admin': admin})
    print(f"Usuário {nome} Cadastrado com sucesso!")

def remover_usuario(nome_usuario):
    for user in usuarios:
        if user['nome'] == nome_usuario:
            usuarios.remove(user)
    print(f"Usuário {nome_usuario} Removido!")

def listar_usuario():
    print("Lista Usuários")
    for user in usuarios:
        print(f"Nome: {user['nome']} - Email {user['email']} - Admin: {user['admin']}")

def login(email, senha):
    print(usuarios)
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            return usuario
    return None

def adicionar_produto(usuario, nome, preco, qtd):
    if usuario['admin']:
        produtos.append({'nome': nome, 'preco': preco, 'qtd': qtd})
        print(f"Produto {nome} Cadastrado com sucesso!")
    else:
        print("Acesso negado. Apenas administradores podem adicionar produtos.")

def remover_produto(nome_produto):
    for produto in produtos:
        if produto['nome'] == nome_produto:
            produtos.remove(produto)
    print(f"Produto {nome_produto} Removido!")

def listar_produtos():
    print("Lista Produtos")
    for produto in produtos:
        print(f"Produto: {produto['nome']} - Valor: R$ {produto['preco']} - Qtd Estoque: {produto['qtd']}")

def adicionar_ao_carrinho(nome_produto,qtd):
    for produto in produtos:
        if produto['nome'] == nome_produto:
            total=produto['preco']*qtd
            produtoAdd={'nome':produto['nome'],'qtd':qtd,'preco_unitario':produto['preco'],'preco_total':total}
            carrinho.append(produtoAdd)
    print(f"Produto {nome_produto} Adicionado ao Carrinho!")

def remover_do_carrinho(nome_produto):
    for produto in carrinho:
        if produto['nome'] == nome_produto:
            carrinho.remove(produto)
    print(f"Produto {nome_produto} Removido do Carrinho!")

def visualizar_carrinho():
    print("Visualizar Carrinho")
    total = 0
    for produto in carrinho:
        print(f"produto:{produto['nome']}, qtd:{produto['qtd']}, v.unitario: {produto['preco_unitario']} v.total:{produto['preco_total']}")
        total += produto['preco_total']
    print('Total do Carrinho: R$', total)
    return total

def finalizar_compra(usuario):
    print("Finalizar Compra")
    global carrinho
    total=visualizar_carrinho()
    ver=input("Deseja realmente finalizar a compra dos produtos do carrinho acima? (s/n)")
    if ver == 's':
        formaPagamento=input("Digite a forma de pagamento: credito, debito ou pix: ")
        historico={'usuario':usuario['email'],'valor_transacao':total,'forma_pagamento':formaPagamento,'itens':carrinho}
        historico_compras.append(historico)
        carrinho = []
        print("Compra finalizada com sucesso!")

def visualizar_historico(usuario):
    if usuario['admin']:
        print("Historico de Vendas")
        for vendas in historico_compras:
            print(f"User: {vendas['usuario']} - Valor: R$ {vendas['valor_transacao']} - Forma Pag: {vendas['forma_pagamento']}")
            itens_vendas=vendas['itens']
            for itens in itens_vendas:
                print(f"Produto: {itens['nome']} - qtd: {itens['qtd']} - v.unit: {itens['preco_unitario']} - v.total:{itens['preco_total']}")
    else:
        print("Historico de Compras")
        for vendas in historico_compras:
            print(f"User: {vendas['usuario']} - Valor: R$ {vendas['valor_transacao']} - Forma Pag: {vendas['forma_pagamento']}")
            itens_vendas=vendas['itens']
            for itens in itens_vendas:
                print(f"Produto: {itens['nome']} - qtd: {itens['qtd']} - v.unit: {itens['preco_unitario']} - v.total:{itens['preco_total']}")

def atualizar_estoque(usuario, nome_produto, qtd):
    if usuario['admin']:
        for produto in produtos:
            if produto['nome'] == nome_produto:
                produto['qtd'] = qtd
        print(f"Produto {nome_produto} atualizado!")
    else:
        print("Acesso negado. Apenas administradores podem atualizar o estoque.")

usuario_logado = None

while True:
    if not usuario_logado:
        print("")
        print("1. Login")
        print("2. Cadastrar usuário")
        opcao = input("Escolha uma opção: ")
        print("")
        if opcao == '1':
            email = input("Email: ")
            senha = int(input("Senha: "))
            usuario_logado = login(email, senha)
            if usuario_logado:
                print("Login bem sucedido!")
            else:
                print("Falha no login.")
        elif opcao == '2':
            print("Cadastrar Usuário")
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            admin = input("É administrador? (s/n): ").lower() == 's'
            cadastrar_usuario(nome, email, senha, admin)
    else:
        if usuario_logado['admin']:
            print("")
            print("1. Adicionar produto")
            print("2. Remover produtos")
            print("3. Atualizar estoque")
            print("4. Visualizar histórico vendas")
            print("5. Listar produtos")
            print("6. Listar Usuarios")
            print("7. Remover Usuario")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")
            print("")
            if opcao == '1':
                print("Cadastrar Produto")
                nome = input("Nome do produto: ")
                preco = float(input("Preço: "))
                qtd = int(input("qtd: "))
                adicionar_produto(usuario_logado, nome, preco, qtd)
            elif opcao == '2':    
                print("Remover Produto")
                nome = input("Nome do produto: ")
                remover_produto(nome)
            elif opcao == '3':
                print("Atualizar estoque do Produto")
                nome_produto = input("Nome do produto: ")
                quantidade = int(input("Quantidade: "))
                atualizar_estoque(usuario_logado, nome_produto, quantidade)
            elif opcao == '4':
                visualizar_historico(usuario_logado)
            elif opcao == '5':
                listar_produtos()
            elif opcao == '6':
                listar_usuario()
            elif opcao == '7':
                nome = input("Nome do usuário: ")
                remover_usuario(nome)
            elif opcao == '0':
                break
        else:
            print("")
            print("1. Adicionar ao carrinho")
            print("2. Remover do carrinho")
            print("3. Visualizar carrinho")
            print("4. Finalizar compra")
            print("5. Listar produtos")
            print("6. Visualizar histórico compras")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")
            print("")
            if opcao == '1':
                print("Adicionar Produto ao carrinho")
                nome_produto = input("Nome do produto: ")
                quantidade=int(input("Quantidade: "))
                adicionar_ao_carrinho(nome_produto,quantidade)
            elif opcao == '2':
                print("Remover Produto do carrinho")
                nome_produto = input("Nome do produto: ")
                remover_do_carrinho(nome_produto)
            elif opcao == '3':
                visualizar_carrinho()
            elif opcao == '4':
                finalizar_compra(usuario_logado)
            elif opcao == '5':
                listar_produtos()
            elif opcao == '6':
                visualizar_historico(usuario_logado)
            elif opcao == '0':
                break
