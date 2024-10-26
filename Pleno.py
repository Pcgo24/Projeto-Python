class pleno(object):

        def cadastro_P():
            Nome_P = ((input("Insira o nome completo do Funcionário: ")))
            Endereco_P = ((input("Insira o Endereco do Funcionário: ")))
            CPF_P = ((input("Insira o CPF do Funcionário: ")))
            Data_P = ((input("Insira a Data de Admissao do Funcionário: ")))
            while True:
                Horas_P = ((input("Insira quantas horas extras foram trabalhadas: ")))

                try:
                    Horas_P = int (Horas_P)
                    break
                except:
                    print ('Digite apenas números: ')
                    continue

            return Nome_P, Endereco_P, CPF_P, Data_P, Horas_P