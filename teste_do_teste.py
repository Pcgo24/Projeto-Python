# importanddo bibliotecas

import os

# importando classes
from Senior import senior as s
from Junior import junior as j
from Pleno import pleno as p
from Estagiario import estagiario as e
from Supervisor import supervisor as sv

# Estagiário
func_estagiario_nome = []
func_estagiario_endereco = []
func_estagiario_cpf = []
func_estagiario_data = []
func_estagiario_horas = []

# Junior
func_junior_nome = []
func_junior_endereco = []
func_junior_cpf = []
func_junior_data = []
func_junior_horas = []

# Pleno
func_pleno_nome = []
func_pleno_endereco = []
func_pleno_cpf = []
func_pleno_data = []
func_pleno_horas = []

# Senior
func_senior_nome = []
func_senior_endereco = []
func_senior_cpf = []
func_senior_data = []
func_senior_horas = []

# Supervisor
func_supervisor_nome = []
func_supervisor_endereco = []
func_supervisor_cpf = []
func_supervisor_data = []
func_supervisor_horas = []



# definindo funcao para "continuar"
def continuar():
    print ('Pressione qualquer tecla para continuar...')
    input()
    
    return


# definindo funcao para limpar terminal
def limpar():
    os.system("cls")


# definindo arquivo principal
def main():

    # lista de funcionarios
    func_estagiario = ['Pedro', 'Henrique']
    func_junior = ['Luis']
    func_pleno = ['Paulo', 'Ricardo']
    func_senior = ['Vitor']
    func_supervisor = ['Peulo']

    # lista enderecos de funcionarios    
    endereco_estagiario = ['Prudentopolis', 'Guarapuava']
    endereco_junior = ['Guamiranga']
    endereco_pleno = ['Brasília', 'Santa Catarina']
    endereco_senior = ['Irati']
    endereco_supervisor = ['Rocinha']

    # lista de CPF funcionarios
    cpf_estagiario = ['182.921.386-50', '940.871.062-25' ]
    cpf_junior = ['806.289.907-15']
    cpf_pleno = ['827.441.202-86', '141.369.541-82']
    cpf_senior = ['637.896.626-36']
    cpf_supervisor = ['559.311.552-55']

    

    salario_e = 800
    salario_j = 1200
    salario_p = 4000
    salario_s = 8000
    salario_sv = 10000

print ('Olá, Bem Vindo ao sistema da empresa.')

while True:

        # definindo funcao menu
        def menu():
                print("""Selecione uma das opçoes abaixo para prosseguir:
                      
                    1 - Cadastramento de Novo Funcionário
                    2 - Funcionários Cadastrados
                    5 - Promover Funcionário
                    6 - Sair do Sistema 
                    """)
                            
        menu()

        MenuOption = str(input("Insira o numero de acordo com a opcao que deseja selecionar: "))

        if MenuOption != '1' and MenuOption != '2' and MenuOption != '3' and MenuOption != '4' and MenuOption != '5':
            limpar ()
            print ('OPÇÃO INVÁLIDA!!!!!')
            continue 

        limpar()

        if MenuOption == '1':
                while True:
                    print("""Selecione o tipo de funcionário que deseja cadastrar:
                        
                        1 - Estagiário
                        2 - Junior
                        3 - Pleno
                        4 - Senior
                        5 - Supervisor
                        6 - Sair  """)
                    
                    # Adicionando Estagiário

                    Nivel_Option_add = str(input("Insira o numero de acordo com a opcao que deseja selecionar: "))

                    if Nivel_Option_add != '1' and Nivel_Option_add != '2' and Nivel_Option_add != '3' and Nivel_Option_add != '4' and Nivel_Option_add != '5' and Nivel_Option_add != '6':
                        limpar ()
                        print ('OPÇÃO INVÁLIDA!!!!')
                        continue

                    if Nivel_Option_add == '1':
                        limpar()
                        Nome_E, Endereco_E, CPF_E, Data_E, Horas_E = e.cadastro_E()
                        func_estagiario_nome.append(Nome_E)
                        func_estagiario_endereco.append(Endereco_E)
                        func_estagiario_cpf.append(CPF_E)
                        func_estagiario_data.append(Data_E)
                        func_estagiario_horas.append(Horas_E)
                        break

                    if Nivel_Option_add == '2':
                        limpar()
                        Nome_J, Endereco_J, CPF_J, Data_J, Horas_J = j.cadastro_J()
                        func_junior_nome.append (Nome_J)
                        func_junior_endereco.append (Endereco_J)
                        func_junior_cpf.append (CPF_J)
                        func_junior_data.append (Data_J)
                        func_junior_horas.append (Horas_J)
                        break

                    if Nivel_Option_add == '3':
                        limpar()
                        Nome_P, Endereco_P, CPF_P, Data_P, Horas_P = p.cadastro_P()
                        func_pleno_nome.append(Nome_P)
                        func_pleno_endereco.append (Endereco_P)
                        func_pleno_cpf.append (CPF_P)
                        func_pleno_data.append (Data_P)
                        func_pleno_horas.append (Horas_P)
                        break

                    if Nivel_Option_add == '4':
                        limpar()
                        Nome_S, Endereco_S, CPF_S, Data_S, Horas_S = s.cadastro_S()
                        func_senior_nome.append(Nome_S)
                        func_senior_endereco.append (Endereco_S)
                        func_senior_cpf.append (CPF_S)
                        func_senior_data.append (Data_S)
                        func_senior_horas.append (Horas_S)
                        break

                    if Nivel_Option_add == '5':
                        limpar()
                        Nome_SV, Endereco_SV, CPF_SV, Data_SV, Horas_SV = sv.cadastro_SV()
                        func_supervisor_nome.append(Nome_SV)
                        func_supervisor_endereco.append (Endereco_SV)
                        func_supervisor_cpf.append (CPF_SV)
                        func_supervisor_data.append (Data_SV)
                        func_supervisor_horas.append (Horas_SV)  
                        break  

                    if Nivel_Option_add == '6':
                        limpar ()
                        break
                        
                limpar ()

        if MenuOption == '2':
            while True:
                print("""Escolha o nivel que deseja verificar:
                    
                        1 - Estagiário
                        2 - Junior
                        3 - Pleno
                        4 - Senior
                        5 - Supervisor
                        6 - Sair
                    """)
                
                # Funcionários Cadastrados

                Nivel_Option_all = str(input("Insira o numero de acordo com a opcao que deseja selecionar: "))
    
                limpar()
            

                if Nivel_Option_all == '1':
                    if len (func_estagiario_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                    while True:
                        
                        i = 0
                        for _ in func_estagiario_nome:
                            print (f'{i} - {func_estagiario_nome[i]}')

                            i += 1
                        func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja verificar: '))

                        try:
                            func_escolhido = int (func_escolhido)

                            if int(func_escolhido) >= len(func_estagiario_nome):
                                limpar ()
                                print ('NÚMERO INVÁLIDO!!!')
                                continue
                            else:
                                limpar ()
                                break
                        except:
                            limpar ()
                            print ('DIGITE UM NÚMERO!!!!')
                            continue
                        
                    

                    print (f'{func_estagiario_nome[func_escolhido]}')
                    print (f'{func_estagiario_endereco[func_escolhido]}')
                    print (f'{func_estagiario_cpf[func_escolhido]}')
                    print (f'{func_estagiario_data[func_escolhido]}')
                    print (f'{func_estagiario_horas[func_escolhido]}')

                    continuar()
                    limpar()
                    break

                if Nivel_Option_all == '2':
                    if len (func_junior_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                    while True:
                        i = 0
                        for _ in func_junior_nome:
                            print (f'{i} - {func_junior_nome[i]}')

                            i += 1
                        func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja verificar: '))

                        try:
                            func_escolhido = int (func_escolhido)

                            if int(func_escolhido) >= len(func_junior_nome):
                                limpar ()
                                print ('NÚMERO INVÁLIDO!!!')
                                continue
                            else:
                                limpar ()
                                break
                        except:
                            limpar ()
                            print ('DIGITE UM NÚMERO!!!!')
                            continue


                    print (f'{func_junior_nome[func_escolhido]}')
                    print (f'{func_junior_endereco[func_escolhido]}')
                    print (f'{func_junior_cpf[func_escolhido]}')
                    print (f'{func_junior_data[func_escolhido]}')
                    print (f'{func_junior_horas[func_escolhido]}')

                    continuar()
                    limpar()
                    break

                if Nivel_Option_all == '3':
                    if len (func_pleno_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                    while True:
                        i = 0
                        for _ in func_pleno_nome:
                            print (f'{i} - {func_pleno_nome[i]}')

                            i += 1
                        func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja verificar: '))

                        try:
                            func_escolhido = int (func_escolhido)

                            if int(func_escolhido) >= len(func_pleno_nome):
                                limpar ()
                                print ('NÚMERO INVÁLIDO!!!')
                                continue
                            else:
                                limpar ()
                                break
                        except:
                            limpar ()
                            print ('DIGITE UM NÚMERO!!!!')
                            continue


                    print (f'{func_pleno_nome[func_escolhido]}')
                    print (f'{func_pleno_endereco[func_escolhido]}')
                    print (f'{func_pleno_cpf[func_escolhido]}')
                    print (f'{func_pleno_data[func_escolhido]}')
                    print (f'{func_pleno_horas[func_escolhido]}')

                    continuar()
                    limpar()
                    break

                if Nivel_Option_all == '4':
                    if len (func_senior_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                    while True:
                        i = 0
                        for _ in func_senior_nome:
                            print (f'{i} - {func_senior_nome[i]}')

                            i += 1
                        func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja verificar: '))

                        try:
                            func_escolhido = int (func_escolhido)

                            if int(func_escolhido) >= len(func_senior_nome):
                                limpar ()
                                print ('NÚMERO INVÁLIDO!!!')
                                continue
                            else:
                                limpar ()
                                break
                        except:
                            limpar()
                            print ('DIGITE UM NÚMERO!!!!')
                            continue

                    print (f'{func_senior_nome[func_escolhido]}')
                    print (f'{func_senior_endereco[func_escolhido]}')
                    print (f'{func_senior_cpf[func_escolhido]}')
                    print (f'{func_senior_data[func_escolhido]}')
                    print (f'{func_senior_horas[func_escolhido]}')

                    continuar()
                    limpar()
                    break

                if Nivel_Option_all == '5':
                    if len (func_supervisor_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                    while True:
                        i = 0
                        for _ in func_supervisor_nome:
                            print (f'{i} - {func_supervisor_nome[i]}')

                            i += 1
                        func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja verificar: '))

                        try:
                            func_escolhido = int (func_escolhido)

                            if int(func_escolhido) >= len(func_supervisor_nome):
                                limpar()
                                print ('NÚMERO INVÁLIDO!!!')
                                continue
                            else:
                                limpar ()
                                break
                        except:
                            limpar ()
                            print ('DIGITE UM NÚMERO!!!!')
                            continue

                    print (f'{func_supervisor_nome[func_escolhido]}')
                    print (f'{func_supervisor_endereco[func_escolhido]}')
                    print (f'{func_supervisor_cpf[func_escolhido]}')
                    print (f'{func_supervisor_data[func_escolhido]}')
                    print (f'{func_supervisor_horas[func_escolhido]}')

                    continuar() 
                    limpar()
                    break

                if Nivel_Option_all == '6':
                    limpar ()
                    break

                else:
                    limpar()
                    print ('OPÇÃO INVÁLIDA !!!!!')
                    continue
        
        if MenuOption == '5':

            while True:
                    print("""Selecione o tipo de funcionário que deseja promover:
                        
                        1 - Estagiário
                        2 - Junior
                        3 - Pleno
                        4 - Senior
                        5 - Supervisor
                        6 - Sair  """)
                    

                    Nivel_Option_prom = (input("Insira o numero de acordo com a opcao que deseja selecionar: "))

                    if Nivel_Option_prom != '1' and Nivel_Option_prom != '2' and Nivel_Option_prom != '3' and Nivel_Option_prom != '4' and Nivel_Option_prom != '5' and Nivel_Option_prom != '6':
                        limpar ()
                        print ('OPÇÃO INVÁLIDA!!!!')
                        continue

                    if Nivel_Option_prom == '1': # Estagiário
                        if len (func_estagiario_nome) < 1:
                                print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                                continue
                        while True:
                            
                            i = 0
                            for _ in func_estagiario_nome:
                                print (f'{i} - {func_estagiario_nome[i]}')

                                i += 1
                            func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja promover: '))

                            try:
                                func_escolhido = int (func_escolhido)

                                if int(func_escolhido) >= len(func_estagiario_nome):
                                    limpar ()
                                    print ('NÚMERO INVÁLIDO!!!')
                                    continue
                                else:
                                    limpar ()
                                    break
                            except:
                                limpar ()
                                print ('DIGITE UM NÚMERO!!!!')
                                continue

                        print("""Você deseja promover ele para ?
                        
                        1 - Junior
                        2 - Pleno
                        3 - Senior
                        4 - Supervisor
                        5 - Sair  """)

                        prom_to = input ('Digite o número correspondente ao cargo que deseja promover o funcionário: ')

                        if prom_to == '1': # Junior
                            func_junior_nome.append(func_estagiario_nome[func_escolhido])
                            func_junior_endereco.append(func_estagiario_endereco[func_escolhido])
                            func_junior_cpf.append(func_estagiario_cpf[func_escolhido])
                            func_junior_data.append(func_estagiario_data[func_escolhido])
                            func_junior_horas.append(func_estagiario_horas[func_escolhido])

                            del func_estagiario_nome[func_escolhido]
                            del func_estagiario_endereco[func_escolhido]
                            del func_estagiario_cpf[func_escolhido]
                            del func_estagiario_data[func_escolhido]
                            del func_estagiario_horas[func_escolhido]

                            
                        if prom_to == '2': #Pleno
                            func_pleno_nome.append(func_estagiario_nome[func_escolhido])
                            func_pleno_endereco.append(func_estagiario_endereco[func_escolhido])
                            func_pleno_cpf.append(func_estagiario_cpf[func_escolhido])
                            func_pleno_data.append(func_estagiario_data[func_escolhido])
                            func_pleno_horas.append(func_estagiario_horas[func_escolhido])

                            del func_estagiario_nome[func_escolhido]
                            del func_estagiario_endereco[func_escolhido]
                            del func_estagiario_cpf[func_escolhido]
                            del func_estagiario_data[func_escolhido]
                            del func_estagiario_horas[func_escolhido]


                        if prom_to == '3': #Senio
                            func_senior_nome.append(func_estagiario_nome[func_escolhido])
                            func_senior_endereco.append(func_estagiario_endereco[func_escolhido])
                            func_senior_cpf.append(func_estagiario_cpf[func_escolhido])
                            func_senior_data.append(func_estagiario_data[func_escolhido])
                            func_senior_horas.append(func_estagiario_horas[func_escolhido])

                            del func_estagiario_nome[func_escolhido]
                            del func_estagiario_endereco[func_escolhido]
                            del func_estagiario_cpf[func_escolhido]
                            del func_estagiario_data[func_escolhido]
                            del func_estagiario_horas[func_escolhido]


                        if prom_to == '4': #Supervisor
                            func_supervisor_nome.append(func_estagiario_nome[func_escolhido])
                            func_supervisor_endereco.append(func_estagiario_endereco[func_escolhido])
                            func_supervisor_cpf.append(func_estagiario_cpf[func_escolhido])
                            func_supervisor_data.append(func_estagiario_data[func_escolhido])
                            func_supervisor_horas.append(func_estagiario_horas[func_escolhido])

                            del func_estagiario_nome[func_escolhido]
                            del func_estagiario_endereco[func_escolhido]
                            del func_estagiario_cpf[func_escolhido]
                            del func_estagiario_data[func_escolhido]
                            del func_estagiario_horas[func_escolhido]
                            



                        
                        continuar()
                        limpar()
                        break

                    if Nivel_Option_prom == '2': # Junior
                
                        if len (func_junior_nome) < 1:
                                print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                                continue
                        while True:
                            
                            i = 0
                            for _ in func_junior_nome:
                                print (f'{i} - {func_junior_nome[i]}')

                                i += 1
                            func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja promover: '))

                            try:
                                func_escolhido = int (func_escolhido)

                                if int(func_escolhido) >= len(func_junior_nome):
                                    limpar ()
                                    print ('NÚMERO INVÁLIDO!!!')
                                    continue
                                else:
                                    limpar ()
                                    break
                            except:
                                limpar ()
                                print ('DIGITE UM NÚMERO!!!!')
                                continue

                        print("""Você deseja promover ele para ?
                        
                        1 - Estagiário
                        2 - Pleno
                        3 - Senior
                        4 - Supervisor
                        5 - Sair  """)

                        prom_to = input ('Digite o número correspondente ao cargo que deseja promover o funcionário: ')

                        if prom_to == '1': # Estagiário
                            func_estagiario_nome.append(func_junior_nome[func_escolhido])
                            func_estagiario_endereco.append(func_junior_endereco[func_escolhido])
                            func_estagiario_cpf.append(func_junior_cpf[func_escolhido])
                            func_estagiario_data.append(func_junior_data[func_escolhido])
                            func_estagiario_horas.append(func_junior_horas[func_escolhido])

                            del func_junior_nome[func_escolhido]
                            del func_junior_endereco[func_escolhido]
                            del func_junior_cpf[func_escolhido]
                            del func_junior_data[func_escolhido]
                            del func_junior_horas[func_escolhido]

                            
                        if prom_to == '2': #Pleno
                            func_pleno_nome.append(func_junior_nome[func_escolhido])
                            func_pleno_endereco.append(func_junior_endereco[func_escolhido])
                            func_pleno_cpf.append(func_junior_cpf[func_escolhido])
                            func_pleno_data.append(func_junior_data[func_escolhido])
                            func_pleno_horas.append(func_junior_horas[func_escolhido])

                            del func_junior_nome[func_escolhido]
                            del func_junior_endereco[func_escolhido]
                            del func_junior_cpf[func_escolhido]
                            del func_junior_data[func_escolhido]
                            del func_junior_horas[func_escolhido]


                        if prom_to == '3': #Senio
                            func_senior_nome.append(func_junior_nome[func_escolhido])
                            func_senior_endereco.append(func_junior_endereco[func_escolhido])
                            func_senior_cpf.append(func_junior_cpf[func_escolhido])
                            func_senior_data.append(func_junior_data[func_escolhido])
                            func_senior_horas.append(func_junior_horas[func_escolhido])

                            del func_junior_nome[func_escolhido]
                            del func_junior_endereco[func_escolhido]
                            del func_junior_cpf[func_escolhido]
                            del func_junior_data[func_escolhido]
                            del func_junior_horas[func_escolhido]


                        if prom_to == '4': #Supervisor
                            func_supervisor_nome.append(func_junior_nome[func_escolhido])
                            func_supervisor_endereco.append(func_junior_endereco[func_escolhido])
                            func_supervisor_cpf.append(func_junior_cpf[func_escolhido])
                            func_supervisor_data.append(func_junior_data[func_escolhido])
                            func_supervisor_horas.append(func_junior_horas[func_escolhido])

                            del func_junior_nome[func_escolhido]
                            del func_junior_endereco[func_escolhido]
                            del func_junior_cpf[func_escolhido]
                            del func_junior_data[func_escolhido]
                            del func_junior_horas[func_escolhido]
                            


    
                        
                        continuar()
                        limpar()
                        break

                    if Nivel_Option_prom == '3': # Pleno
                        if len (func_pleno_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                        while True:
                            
                            i = 0
                            for _ in func_pleno_nome:
                                print (f'{i} - {func_pleno_nome[i]}')

                                i += 1
                            func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja promover: '))

                            try:
                                func_escolhido = int (func_escolhido)

                                if int(func_escolhido) >= len(func_pleno_nome):
                                    limpar ()
                                    print ('NÚMERO INVÁLIDO!!!')
                                    continue
                                else:
                                    limpar ()
                                    break
                            except:
                                limpar ()
                                print ('DIGITE UM NÚMERO!!!!')
                                continue

                        print("""Você deseja promover ele para ?
                        
                        1 - Estagiário
                        2 - Junior
                        3 - Senior
                        4 - Supervisor
                        5 - Sair  """)

                        prom_to = input ('Digite o número correspondente ao cargo que deseja promover o funcionário: ')

                        if prom_to == '1': # Estagiário
                            func_estagiario_nome.append(func_pleno_nome[func_escolhido])
                            func_estagiario_endereco.append(func_pleno_endereco[func_escolhido])
                            func_estagiario_cpf.append(func_pleno_cpf[func_escolhido])
                            func_estagiario_data.append(func_pleno_data[func_escolhido])
                            func_estagiario_horas.append(func_pleno_horas[func_escolhido])

                            del func_pleno_nome[func_escolhido]
                            del func_pleno_endereco[func_escolhido]
                            del func_pleno_cpf[func_escolhido]
                            del func_pleno_data[func_escolhido]
                            del func_pleno_horas[func_escolhido]

                            
                        if prom_to == '2': #Pleno
                            func_junior_nome.append(func_pleno_nome[func_escolhido])
                            func_junior_endereco.append(func_pleno_endereco[func_escolhido])
                            func_junior_cpf.append(func_pleno_cpf[func_escolhido])
                            func_junior_data.append(func_pleno_data[func_escolhido])
                            func_junior_horas.append(func_pleno_horas[func_escolhido])

                            del func_pleno_nome[func_escolhido]
                            del func_pleno_endereco[func_escolhido]
                            del func_pleno_cpf[func_escolhido]
                            del func_pleno_data[func_escolhido]
                            del func_pleno_horas[func_escolhido]


                        if prom_to == '3': #Senio
                            func_senior_nome.append(func_pleno_nome[func_escolhido])
                            func_senior_endereco.append(func_pleno_endereco[func_escolhido])
                            func_senior_cpf.append(func_pleno_cpf[func_escolhido])
                            func_senior_data.append(func_pleno_data[func_escolhido])
                            func_senior_horas.append(func_pleno_horas[func_escolhido])

                            del func_pleno_nome[func_escolhido]
                            del func_pleno_endereco[func_escolhido]
                            del func_pleno_cpf[func_escolhido]
                            del func_pleno_data[func_escolhido]
                            del func_pleno_horas[func_escolhido]


                        if prom_to == '4': #Supervisor
                            func_supervisor_nome.append(func_pleno_nome[func_escolhido])
                            func_supervisor_endereco.append(func_pleno_endereco[func_escolhido])
                            func_supervisor_cpf.append(func_pleno_cpf[func_escolhido])
                            func_supervisor_data.append(func_pleno_data[func_escolhido])
                            func_supervisor_horas.append(func_pleno_horas[func_escolhido])

                            del func_pleno_nome[func_escolhido]
                            del func_pleno_endereco[func_escolhido]
                            del func_pleno_cpf[func_escolhido]
                            del func_pleno_data[func_escolhido]
                            del func_pleno_horas[func_escolhido]
                    
                    if Nivel_Option_prom == '4': # Senior
                        if len (func_senior_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                        while True:
                            
                            i = 0
                            for _ in func_senior_nome:
                                print (f'{i} - {func_senior_nome[i]}')

                                i += 1
                            func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja promover: '))

                            try:
                                func_escolhido = int (func_escolhido)

                                if int(func_escolhido) >= len(func_senior_nome):
                                    limpar ()
                                    print ('NÚMERO INVÁLIDO!!!')
                                    continue
                                else:
                                    limpar ()
                                    break
                            except:
                                limpar ()
                                print ('DIGITE UM NÚMERO!!!!')
                                continue

                        print("""Você deseja promover ele para ?
                        
                        1 - Estagiário
                        2 - Junior
                        3 - Pleno
                        4 - Supervisor
                        5 - Sair  """)

                        prom_to = input ('Digite o número correspondente ao cargo que deseja promover o funcionário: ')

                        if prom_to == '1': # Estagiário
                            func_estagiario_nome.append(func_senior_nome[func_escolhido])
                            func_estagiario_endereco.append(func_senior_endereco[func_escolhido])
                            func_estagiario_cpf.append(func_senior_cpf[func_escolhido])
                            func_estagiario_data.append(func_senior_data[func_escolhido])
                            func_estagiario_horas.append(func_senior_horas[func_escolhido])

                            del func_senior_nome[func_escolhido]
                            del func_senior_endereco[func_escolhido]
                            del func_senior_cpf[func_escolhido]
                            del func_senior_data[func_escolhido]
                            del func_senior_horas[func_escolhido]
                            

                        if prom_to == '2': #Junior
                            func_junior_nome.append(func_senior_nome[func_escolhido])
                            func_junior_endereco.append(func_senior_endereco[func_escolhido])
                            func_junior_cpf.append(func_senior_cpf[func_escolhido])
                            func_junior_data.append(func_senior_data[func_escolhido])
                            func_junior_horas.append(func_senior_horas[func_escolhido])

                            del func_senior_nome[func_escolhido]
                            del func_senior_endereco[func_escolhido]
                            del func_senior_cpf[func_escolhido]
                            del func_senior_data[func_escolhido]
                            del func_senior_horas[func_escolhido]

                            
                        if prom_to == '3': #Pleno
                            func_pleno_nome.append(func_senior_nome[func_escolhido])
                            func_pleno_endereco.append(func_senior_endereco[func_escolhido])
                            func_pleno_cpf.append(func_senior_cpf[func_escolhido])
                            func_pleno_data.append(func_senior_data[func_escolhido])
                            func_pleno_horas.append(func_senior_horas[func_escolhido])

                            del func_senior_nome[func_escolhido]
                            del func_senior_endereco[func_escolhido]
                            del func_senior_cpf[func_escolhido]
                            del func_senior_data[func_escolhido]
                            del func_senior_horas[func_escolhido]


                        if prom_to == '4': #Supervisor
                            func_supervisor_nome.append(func_senior_nome[func_escolhido])
                            func_supervisor_endereco.append(func_senior_endereco[func_escolhido])
                            func_supervisor_cpf.append(func_senior_cpf[func_escolhido])
                            func_supervisor_data.append(func_senior_data[func_escolhido])
                            func_supervisor_horas.append(func_senior_horas[func_escolhido])

                            del func_senior_nome[func_escolhido]
                            del func_senior_endereco[func_escolhido]
                            del func_senior_cpf[func_escolhido]
                            del func_senior_data[func_escolhido]
                            del func_senior_horas[func_escolhido]

                    if Nivel_Option_prom == '5': # Supervisor
                        if len (func_supervisor_nome) < 1:
                            print ('AINDA NÃO POSSUI NENHUM FUNCIONARIO CADASTRADO!!!')
                            continue
                        while True:
                            
                            i = 0
                            for _ in func_supervisor_nome:
                                print (f'{i} - {func_supervisor_nome[i]}')

                                i += 1
                            func_escolhido = (input ('Digite o número correspondente aos funcionário que deseja promover: '))

                            try:
                                func_escolhido = int (func_escolhido)

                                if int(func_escolhido) >= len(func_supervisor_nome):
                                    limpar ()
                                    print ('NÚMERO INVÁLIDO!!!')
                                    continue
                                else:
                                    limpar ()
                                    break
                            except:
                                limpar ()
                                print ('DIGITE UM NÚMERO!!!!')
                                continue

                        print("""Você deseja promover ele para ?
                        
                        1 - Estagiário
                        2 - Junior
                        3 - Pleno
                        4 - Supervisor
                        5 - Sair  """)

                        prom_to = input ('Digite o número correspondente ao cargo que deseja promover o funcionário: ')

                        if prom_to == '1': # Estagiário
                            func_estagiario_nome.append(func_supervisor_nome[func_escolhido])
                            func_estagiario_endereco.append(func_supervisor_endereco[func_escolhido])
                            func_estagiario_cpf.append(func_supervisor_cpf[func_escolhido])
                            func_estagiario_data.append(func_supervisor_data[func_escolhido])
                            func_estagiario_horas.append(func_supervisor_horas[func_escolhido])

                            del func_supervisor_nome[func_escolhido]
                            del func_supervisor_endereco[func_escolhido]
                            del func_supervisor_cpf[func_escolhido]
                            del func_supervisor_data[func_escolhido]
                            del func_supervisor_horas[func_escolhido]
                            

                        if prom_to == '2': #Junior
                            func_junior_nome.append(func_supervisor_nome[func_escolhido])
                            func_junior_endereco.append(func_supervisor_endereco[func_escolhido])
                            func_junior_cpf.append(func_supervisor_cpf[func_escolhido])
                            func_junior_data.append(func_supervisor_data[func_escolhido])
                            func_junior_horas.append(func_supervisor_horas[func_escolhido])

                            del func_supervisor_nome[func_escolhido]
                            del func_supervisor_endereco[func_escolhido]
                            del func_supervisor_cpf[func_escolhido]
                            del func_supervisor_data[func_escolhido]
                            del func_supervisor_horas[func_escolhido]

                            
                        if prom_to == '3': #Pleno
                            func_pleno_nome.append(func_supervisor_nome[func_escolhido])
                            func_pleno_endereco.append(func_supervisor_endereco[func_escolhido])
                            func_pleno_cpf.append(func_supervisor_cpf[func_escolhido])
                            func_pleno_data.append(func_supervisor_data[func_escolhido])
                            func_pleno_horas.append(func_supervisor_horas[func_escolhido])

                            del func_supervisor_nome[func_escolhido]
                            del func_supervisor_endereco[func_escolhido]
                            del func_supervisor_cpf[func_escolhido]
                            del func_supervisor_data[func_escolhido]
                            del func_supervisor_horas[func_escolhido]


                        if prom_to == '4': #Supervisor
                            func_senior_nome.append(func_supervisor_nome[func_escolhido])
                            func_senior_endereco.append(func_supervisor_endereco[func_escolhido])
                            func_senior_cpf.append(func_supervisor_cpf[func_escolhido])
                            func_senior_data.append(func_supervisor_data[func_escolhido])
                            func_senior_horas.append(func_supervisor_horas[func_escolhido])

                            del func_supervisor_nome[func_escolhido]
                            del func_supervisor_endereco[func_escolhido]
                            del func_supervisor_cpf[func_escolhido]
                            del func_supervisor_data[func_escolhido]
                            del func_supervisor_horas[func_escolhido]

                        if prom_to == '5':
                            limpar ()
                            break



                    if Nivel_Option_prom == '6':
                        limpar ()
                        break
                        
            limpar ()
   
        if MenuOption == '6':
            limpar ()
            break

if __name__ == '__main__':
    main()
