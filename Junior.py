class junior(object):

    def cadastro_J():
        Nome_J = ((input("Insira o nome completo do Funcionário: ")))
        Endereco_J = ((input("Insira o Endereco do Funcionário: ")))
        CPF_J = ((input("Insira o CPF do Funcionário: ")))
        Data_J = ((input("Insira a Data de Admissao do Funcionário: ")))
        while True:
            Horas_E = ((input("Insira quantas horas extras foram trabalhadas: ")))

            try:
                Horas_E = int (Horas_E)
                break
            except:
                print ('Digite apenas números: ')
                continue

        return Nome_J, Endereco_J, CPF_J, Data_J, Horas_E
    