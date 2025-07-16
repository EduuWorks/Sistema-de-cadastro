import random
id_aleatorio = random.randint(1000, 9999)  # Gerar um ID entre 1000 e 9999
usuarios = []

# Funções:
def gerar_Id(): # Função para nao repetir nenhum id
    ids_usados = {usuario["id"] for usuario in usuarios}
    while True:
        novo_id = random.randint(1000, 9999)
        if novo_id not in ids_usados:
            return novo_id
def exibir_menu():
    print("-" * 17, "MENU PRINCIPAL", "-" * 17)
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Usuário")
    print("2 - Consultar Usuário(s)")
    print("3 - Remover Usuário")
    print("4 - Sair")

def cadastro(): # Função de cadastro
    nome = input("Digite o nome de usuário: ")
    id_usuario = gerar_Id()
    usuario = {"id": id_usuario, "nome": nome}
    usuarios.append(usuario)
    print(f"O usuário {nome} foi cadastrado com sucesso com o ID {id_usuario}.")

def consultar(): # Função de consultar os usuários
    if not usuarios:
        print("Nenhum usuário foi cadastrado.")
    else:
        print("Usuários cadastrados: ")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. id: {usuario['id']} | nome: {usuario['nome']}")

def remover(): # Remove um usuário
    if not usuarios:
        print("Nenhum usuário para remover.")
    else:
        consultar()
        indice = input("Digite o ID do usuário que deseja remover: ")
        for i, usuario in enumerate(usuarios):
            if indice.isdigit():
                id_int = int(indice)
                if usuario["id"] == id_int:
                    removido = usuarios.pop(i)
                    print(f"Usuário '{removido['nome']}' com o id '{removido['id']}' removido com sucesso.")
            else:
                print("Digite um número válido.")
        
def sair(): # Sair do sistema
    print("Saindo do sistema. Até logo!")

def executar_opcao(opcao):
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        consultar()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        sair()
        return False  # Encerra o loop
    else:
        print("Opção inválida. Tente novamente.")
    return True # Continua o loop

# Inicio

print("Bem Vindo ao sistema")

while True:
    exibir_menu()

    try:
        opcao = int(input("Digite o número escolhido: "))
    except ValueError:
        print("Digite um número válido.")
        continue
    continuar = executar_opcao(opcao)
    if not continuar:
        break