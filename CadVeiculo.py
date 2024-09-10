listaVeiculos = []

def cadastrar ():
    print("Digite a marca")
    marca = input()
    print("Digite o modelo")
    modelo = input()
    print("digite a placa:")
    placa = input ()
    veiculoAdd = Veiculo(marca, modelo, placa, ano)
    listaVeiculos.append(veiculoAdd)


def listar():
    if len(listaVeiculos) == 0:
        print ("Não existem veículos cadastrados")
    else:
        i = 1
        for veiculo in listaVeiculos:
            print(f"Veículo: {i}")
            print(f" - {veiculo}")
            i += 1


def excluir():
    listar()
    print("digite a placa que deseja excluir")
    placa = input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo.placa == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
            print("veiculo excluido")
    else:
            print("Veiculo não encontrado")

while True:
    print("escolha uma das opções:")
    print("1 - cadastrar Veiculo")
    print("2 - Listar Veiculos")
    print("3 - excluir veiculo")
    print("0 -SAIR")
    opcao = input()
    try:
        opcao = int(opcao)
    except:
        print("opção invalida")
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opção inválida")