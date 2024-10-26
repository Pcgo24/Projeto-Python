class estagiario(object):

        def cadastro_E():
            Nome_E = ((input("Insira o nome completo do Funcionário: ")))
            Endereco_E = ((input("Insira o Endereco do Funcionário: ")))
            CPF_E = ((input("Insira o CPF do Funcionário: ")))
            Data_E = ((input("Insira a Data de Admissao do Funcionário: ")))
            while True:
                Horas_E = ((input("Insira quantas horas extras foram trabalhadas: ")))

                try:
                    Horas_E = int (Horas_E)
                    break
                except:
                    print ('Digite apenas números: ')
                    continue

            return Nome_E, Endereco_E, CPF_E, Data_E, Horas_E
        



