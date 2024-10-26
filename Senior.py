class senior(object):

        def cadastro_S():
            Nome_S = ((input("Insira o nome completo do Funcionário: ")))
            Endereco_S = ((input("Insira o Endereco do Funcionário: ")))
            CPF_S = ((input("Insira o CPF do Funcionário: ")))
            Data_S = ((input("Insira a Data de Admissao do Funcionário: ")))
            while True:
                Horas_S = ((input("Insira quantas horas extras foram trabalhadas: ")))

                try:
                    Horas_S = int (Horas_S)
                    break
                except:
                    print ('Digite apenas números: ')
                    continue                    

            return Nome_S, Endereco_S, CPF_S, Data_S, Horas_S