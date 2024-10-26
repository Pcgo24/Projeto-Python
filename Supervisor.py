class supervisor(object):

        def cadastro_SV():
            Nome_SV = ((input("Insira o nome completo do Funcionário: ")))
            Endereco_SV = ((input("Insira o Endereco do Funcionário: ")))
            CPF_SV = ((input("Insira o CPF do Funcionário: ")))
            Data_SV = ((input("Insira a Data de Admissao do Funcionário: ")))
            while True:
                Horas_SV = ((input("Insira quantas horas extras foram trabalhadas: ")))

                try:
                    Horas_SV = int(Horas_SV)
                    break
                except:
                    print ('Digite apenas números: ')
                    continue


            return Nome_SV, Endereco_SV, CPF_SV, Data_SV, Horas_SV