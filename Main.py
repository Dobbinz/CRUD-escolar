import json


def main_menu():
    print('====== MENU PRINCIPAL ======')
    print()
    print('[1] - Gerenciar estudantes.')
    print('[2] - Gerenciar professores.')
    print('[3] - Gerenciar disciplinas.')
    print('[4] - Gerenciar turmas.')
    print('[5] - Gerenciar matrículas.')
    print('[9] - Sair.')
    print()
    return input('Informe a opção desejada: ')


def sub_menu():
    print()
    print('*** Menu de operações ***')
    print()
    print('[1] - Incluir.')
    print('[2] - Listar.')
    print('[3] - Atualizar.')
    print('[4] - Excluir.')
    print('[9] - Voltar ao menu principal.')
    print()
    return input('Informe a opção desejada: ')


def codigo_existente(lista, codigo):
    return any(item['codigo'] == codigo for item in lista)


def cpf_existente(lista, cpf):
    return any(item['cpf'] == cpf for item in lista)


def gerenciar_estudantes(lista_estudante):
    lista_estudante = ler_arquivo('estudantes.json')

    while True:
        opcao = sub_menu()
        if opcao == '1':
            while True:
                while True:
                    try:
                        codigo = int(input('Por favor, digite o código do estudante: '))
                        if codigo_existente(lista_estudante, codigo):
                            print('Código já existente. Tente outro código.')
                            continue
                        break
                    except ValueError:
                        print('Digite apenas números.')

                while True:
                    cpf = input('Por favor, digite o CPF do estudante: ')
                    if cpf_existente(lista_estudante, cpf):
                        print('CPF já existente. Tente outro CPF.')
                        continue
                    break

                nome = input('Por favor, digite o nome do estudante: ')

                dados_estudante = {'codigo': codigo, 'nome': nome, 'cpf': cpf}
                lista_estudante.append(dados_estudante)
                salvar_arquivo(lista_estudante, 'estudantes.json')
                print('Estudante registrado.')
                print()
                while True:
                    outro_cadastro = input('Deseja registrar outro estudante?\n(1)SIM\n(2)NÃO\nDigite uma opção: ')
                    if outro_cadastro == '1':
                        break
                    elif outro_cadastro == '2':
                        break
                    else:
                        print('Opção inválida.')
                        print()
                if outro_cadastro == '2':
                    break
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '2':
            if lista_estudante:
                print('Estudantes registrados:')
                for dados_estudante in lista_estudante:
                    print(dados_estudante)
            else:
                print()
                print('Nenhum estudante registrado.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '3':
            print()
            print('*** Editar dados do estudante ***')
            print()
            while True:
                try:
                    codigo_editar = int(input('Por favor, digite o código do estudante: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            estudante_editar = None
            for elemento in lista_estudante:
                if elemento['codigo'] == codigo_editar:
                    estudante_editar = elemento
                    break
            if estudante_editar is None:
                print(f'Estudante de código {codigo_editar}, não foi encontrado.')
            else:
                alterar_codigo = input(f'Deseja alterar o código {codigo_editar}? (s/n): ')
                if alterar_codigo.lower() == 's':
                    while True:
                        novo_codigo = int(input('Por favor, digite o novo código: '))
                        if codigo_existente(lista_estudante, novo_codigo):
                            print('Código já existente. Tente outro.')
                        else:
                            estudante_editar['codigo'] = novo_codigo
                            break

                alterar_nome = input('Deseja alterar o nome? (s/n): ')
                if alterar_nome.lower() == 's':
                    estudante_editar['nome'] = input('Por favor, digite o novo nome: ')

                alterar_cpf = input('Deseja alterar o CPF? (s/n): ')
                if alterar_cpf.lower() == 's':
                    while True:
                        novo_cpf = input('Por favor, digite o novo CPF: ')
                        if cpf_existente(lista_estudante, novo_cpf):
                            print('CPF já existente. Tente outro.')
                        else:
                            estudante_editar['cpf'] = novo_cpf
                            break

                salvar_arquivo(lista_estudante, 'estudantes.json')
                print('Estudante atualizado.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '4':
            print()
            print('*** Excluir dados do estudante ***')
            print()
            while True:
                try:
                    codigo_digitado_para_excluir = int(input('Por favor, digite o código do estudante: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            estudante_para_remover = None
            for dados_estudante in lista_estudante:
                if dados_estudante['codigo'] == codigo_digitado_para_excluir:
                    estudante_para_remover = dados_estudante
                    break
            if estudante_para_remover is None:
                print(f'Estudante de código {codigo_digitado_para_excluir}, não foi encontrado.')
            else:
                lista_estudante.remove(estudante_para_remover)
                salvar_arquivo(lista_estudante, 'estudantes.json')
                print(f'Estudante de código {codigo_digitado_para_excluir} removido com sucesso.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '9':
            print()
            print('Voltando ao menu principal...')
            print()
            break
        else:
            print('Opção inválida, tente novamente.')

    return lista_estudante


def gerenciar_professores(lista_professor):
    lista_professor = ler_arquivo('professores.json')

    while True:
        opcao = sub_menu()
        if opcao == '1':
            while True:
                while True:
                    try:
                        codigo = int(input('Por favor, digite o código do professor: '))
                        if codigo_existente(lista_professor, codigo):
                            print('Código já existente. Tente outro código.')
                            continue
                        break
                    except ValueError:
                        print('Digite apenas números.')

                while True:
                    cpf = input('Por favor, digite o CPF do professor: ')
                    if cpf_existente(lista_professor, cpf):
                        print('CPF já existente. Tente outro CPF.')
                        continue
                    break

                nome = input('Por favor, digite o nome do professor: ')

                dados_professor = {'codigo': codigo, 'nome': nome, 'cpf': cpf}
                lista_professor.append(dados_professor)
                salvar_arquivo(lista_professor, 'professores.json')
                print('Professor registrado.')
                print()
                while True:
                    outro_cadastro = input('Deseja registrar outro professor?\n(1)SIM\n(2)NÃO\nDigite uma opção: ')
                    if outro_cadastro == '1':
                        break
                    elif outro_cadastro == '2':
                        break
                    else:
                        print('Opção inválida.')
                        print()
                if outro_cadastro == '2':
                    break
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '2':
            if lista_professor:
                print('Professores registrados.')
                for dados_professor in lista_professor:
                    print(dados_professor)
            else:
                print()
                print('Nenhum Professor registrado.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '3':
            print()
            print('*** Editar dados Professor ***')
            print()
            while True:
                try:
                    editar_professor = int(input('Por favor, digite o código do Professor: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            professor_atualizar = None
            for elemento in lista_professor:
                if elemento['codigo'] == editar_professor:
                    professor_atualizar = elemento
                    break
            if professor_atualizar is None:
                print(f'Professor de código {editar_professor}, não foi encontrado.')
            else:
                alterar_codigo = input(f'Deseja alterar o código {editar_professor}? (s/n): ')
                if alterar_codigo.lower() == 's':
                    while True:
                        novo_codigo = int(input('Digite o novo código: '))
                        if codigo_existente(lista_professor, novo_codigo):
                            print('Código já existente. Tente outro.')
                        else:
                            professor_atualizar['codigo'] = novo_codigo
                            break

                alterar_nome = input('Deseja alterar o nome? (s/n): ')
                if alterar_nome.lower() == 's':
                    professor_atualizar['nome'] = input('Digite o novo nome: ')

                alterar_cpf = input('Deseja alterar o CPF? (s/n): ')
                if alterar_cpf.lower() == 's':
                    while True:
                        novo_cpf = input('Digite o novo CPF: ')
                        if cpf_existente(lista_professor, novo_cpf):
                            print('CPF já existente. Tente outro.')
                        else:
                            professor_atualizar['cpf'] = novo_cpf
                            break

                salvar_arquivo(lista_professor, 'professores.json')
                print('Professor atualizado.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '4':
            print()
            print('*** Excluir dados do Professor ***')
            print()
            while True:
                try:
                    codigo_para_excluir = int(input('Por favor, digite o código do professor: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            professor_para_remover = None
            for dados_professor in lista_professor:
                if dados_professor['codigo'] == codigo_para_excluir:
                    professor_para_remover = dados_professor
                    break
            if professor_para_remover is None:
                print(f'Professor de código {codigo_para_excluir}, não foi encontrado.')
            else:
                lista_professor.remove(professor_para_remover)
                salvar_arquivo(lista_professor, 'professores.json')
                print(f'Professor de código {codigo_para_excluir}, removido com sucesso.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '9':
            print()
            print('Voltando ao menu principal...')
            print()
            break
        else:
            print('Opção inválida, tente novamente.')

    return lista_professor


def gerenciar_disciplinas(lista_disciplina):
    lista_disciplina = ler_arquivo('disciplinas.json')

    while True:
        opcao = sub_menu()
        if opcao == '1':
            while True:
                while True:
                    try:
                        codigo = int(input('Por favor, digite o código da disciplina: '))
                        if codigo_existente(lista_disciplina, codigo):
                            print('Código já existente. Tente outro código.')
                            continue
                        break
                    except ValueError:
                        print('Digite apenas números.')

                nome = input('Por favor, digite o nome da disciplina: ')

                dados_disciplina = {'codigo': codigo, 'nome': nome}
                lista_disciplina.append(dados_disciplina)
                salvar_arquivo(lista_disciplina, 'disciplinas.json')
                print('Disciplina registrada.')
                print()
                while True:
                    outro_cadastro = input('Deseja registrar outra disciplina?\n(1)SIM\n(2)NÃO\nDigite uma opção: ')
                    if outro_cadastro == '1':
                        break
                    elif outro_cadastro == '2':
                        break
                    else:
                        print('Opção inválida.')
                        print()
                if outro_cadastro == '2':
                    break
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '2':
            if lista_disciplina:
                print('Disciplinas registradas:')
                for dados_disciplina in lista_disciplina:
                    print(dados_disciplina)
            else:
                print()
                print('Nenhuma disciplina registrada.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '3':
            print()
            print('*** Editar dados da disciplina ***')
            print()
            while True:
                try:
                    editar_disciplina = int(input('Por favor, digite o código da disciplina: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            disciplina_atualizar = None
            for elemento in lista_disciplina:
                if elemento['codigo'] == editar_disciplina:
                    disciplina_atualizar = elemento
                    break
            if disciplina_atualizar is None:
                print(f'Disciplina de código {editar_disciplina}, não foi encontrada.')
            else:
                alterar_codigo = input(f'Deseja alterar o código {editar_disciplina}? (s/n): ')
                if alterar_codigo.lower() == 's':
                    while True:
                        novo_codigo = int(input('Digite o novo código: '))
                        if codigo_existente(lista_disciplina, novo_codigo):
                            print('Código já existente. Tente outro.')
                        else:
                            disciplina_atualizar['codigo'] = novo_codigo
                            break

                alterar_nome = input('Deseja alterar o nome? (s/n): ')
                if alterar_nome.lower() == 's':
                    disciplina_atualizar['nome'] = input('Digite o novo nome: ')

                salvar_arquivo(lista_disciplina, 'disciplinas.json')
                print('Disciplina atualizada.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '4':
            print()
            print('*** Excluir dados da disciplina ***')
            print()
            while True:
                try:
                    codigo_para_excluir = int(input('Por favor, digite o código da disciplina: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            disciplina_para_remover = None
            for dados_disciplina in lista_disciplina:
                if dados_disciplina['codigo'] == codigo_para_excluir:
                    disciplina_para_remover = dados_disciplina
                    break
            if disciplina_para_remover is None:
                print(f'Disciplina de código {codigo_para_excluir}, não foi encontrada.')
            else:
                lista_disciplina.remove(disciplina_para_remover)
                salvar_arquivo(lista_disciplina, 'disciplinas.json')
                print(f'Disciplina de código {codigo_para_excluir}, removida com sucesso.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '9':
            print()
            print('Voltando ao menu principal...')
            print()
            break
        else:
            print('Opção inválida, tente novamente.')

    return lista_disciplina


def gerenciar_turmas(lista_turma):
    lista_turma = ler_arquivo('turmas.json')

    while True:
        opcao = sub_menu()
        if opcao == '1':
            while True:
                while True:
                    try:
                        codigo = int(input('Por favor, digite o código da turma: '))
                        if codigo_existente(lista_turma, codigo):
                            print('Código já existente. Tente outro código.')
                            continue
                        break
                    except ValueError:
                        print('Digite apenas números.')

                nome = input('Por favor, digite o nome da turma: ')

                dados_turma = {'codigo': codigo, 'nome': nome}
                lista_turma.append(dados_turma)
                salvar_arquivo(lista_turma, 'turmas.json')
                print('Turma registrada.')
                print()
                while True:
                    outro_cadastro = input('Deseja registrar outra turma?\n(1)SIM\n(2)NÃO\nDigite uma opção: ')
                    if outro_cadastro == '1':
                        break
                    elif outro_cadastro == '2':
                        break
                    else:
                        print('Opção inválida.')
                        print()
                if outro_cadastro == '2':
                    break
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '2':
            if lista_turma:
                print('Turmas registradas:')
                for dados_turma in lista_turma:
                    print(dados_turma)
            else:
                print()
                print('Nenhuma turma registrada.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '3':
            print()
            print('*** Editar dados da turma ***')
            print()
            while True:
                try:
                    editar_turma = int(input('Por favor, digite o código da turma: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            turma_atualizar = None
            for elemento in lista_turma:
                if elemento['codigo'] == editar_turma:
                    turma_atualizar = elemento
                    break
            if turma_atualizar is None:
                print(f'Turma de código {editar_turma}, não foi encontrada.')
            else:
                alterar_codigo = input(f'Deseja alterar o código {editar_turma}? (s/n): ')
                if alterar_codigo.lower() == 's':
                    while True:
                        novo_codigo = int(input('Digite o novo código: '))
                        if codigo_existente(lista_turma, novo_codigo):
                            print('Código já existente. Tente outro.')
                        else:
                            turma_atualizar['codigo'] = novo_codigo
                            break

                alterar_nome = input('Deseja alterar o nome? (s/n): ')
                if alterar_nome.lower() == 's':
                    turma_atualizar['nome'] = input('Digite o novo nome: ')

                salvar_arquivo(lista_turma, 'turmas.json')
                print('Turma atualizada.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '4':
            print()
            print('*** Excluir dados da turma ***')
            print()
            while True:
                try:
                    codigo_para_excluir = int(input('Por favor, digite o código da turma: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            turma_para_remover = None
            for dados_turma in lista_turma:
                if dados_turma['codigo'] == codigo_para_excluir:
                    turma_para_remover = dados_turma
                    break
            if turma_para_remover is None:
                print(f'Turma de código {codigo_para_excluir}, não foi encontrada.')
            else:
                lista_turma.remove(turma_para_remover)
                salvar_arquivo(lista_turma, 'turmas.json')
                print(f'Turma de código {codigo_para_excluir}, removida com sucesso.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '9':
            print()
            print('Voltando ao menu principal...')
            print()
            break
        else:
            print('Opção inválida, tente novamente.')

    return lista_turma


def gerenciar_matriculas(lista_matricula):
    lista_matricula = ler_arquivo('matriculas.json')

    while True:
        opcao = sub_menu()
        if opcao == '1':
            while True:
                while True:
                    try:
                        codigo = int(input('Por favor, digite o código da matrícula: '))
                        if codigo_existente(lista_matricula, codigo):
                            print('Código já existente. Tente outro código.')
                            continue
                        break
                    except ValueError:
                        print('Digite apenas números.')

                estudante_codigo = int(input('Por favor, digite o código do estudante: '))
                turma_codigo = int(input('Por favor, digite o código da turma: '))

                dados_matricula = {'codigo': codigo, 'estudante_codigo': estudante_codigo, 'turma_codigo': turma_codigo}
                lista_matricula.append(dados_matricula)
                salvar_arquivo(lista_matricula, 'matriculas.json')
                print('Matrícula registrada.')
                print()
                while True:
                    outra_matricula = input('Deseja registrar outra matrícula?\n(1)SIM\n(2)NÃO\nDigite uma opção: ')
                    if outra_matricula == '1':
                        break
                    elif outra_matricula == '2':
                        break
                    else:
                        print('Opção inválida.')
                        print()
                if outra_matricula == '2':
                    break
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '2':
            if lista_matricula:
                print('Matrículas registradas:')
                for dados_matricula in lista_matricula:
                    print(dados_matricula)
            else:
                print()
                print('Nenhuma matrícula registrada.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '3':
            print()
            print('*** Editar dados da matrícula ***')
            print()
            while True:
                try:
                    editar_matricula = int(input('Por favor, digite o código da matrícula: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            matricula_atualizar = None
            for elemento in lista_matricula:
                if elemento['codigo'] == editar_matricula:
                    matricula_atualizar = elemento
                    break
            if matricula_atualizar is None:
                print(f'Matrícula de código {editar_matricula}, não foi encontrada.')
            else:
                alterar_codigo = input(f'Deseja alterar o código {editar_matricula}? (s/n): ')
                if alterar_codigo.lower() == 's':
                    while True:
                        novo_codigo = int(input('Digite o novo código: '))
                        if codigo_existente(lista_matricula, novo_codigo):
                            print('Código já existente. Tente outro.')
                        else:
                            matricula_atualizar['codigo'] = novo_codigo
                            break

                alterar_estudante_codigo = input('Deseja alterar o código do estudante? (s/n): ')
                if alterar_estudante_codigo.lower() == 's':
                    matricula_atualizar['estudante_codigo'] = int(input('Digite o novo código do estudante: '))

                alterar_turma_codigo = input('Deseja alterar o código da turma? (s/n): ')
                if alterar_turma_codigo.lower() == 's':
                    matricula_atualizar['turma_codigo'] = int(input('Digite o novo código da turma: '))

                salvar_arquivo(lista_matricula, 'matriculas.json')
                print('Matrícula atualizada.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '4':
            print()
            print('*** Excluir dados da matrícula ***')
            print()
            while True:
                try:
                    codigo_para_excluir = int(input('Por favor, digite o código da matrícula: '))
                    break
                except ValueError:
                    print('Digite apenas números.')

            matricula_para_remover = None
            for dados_matricula in lista_matricula:
                if dados_matricula['codigo'] == codigo_para_excluir:
                    matricula_para_remover = dados_matricula
                    break
            if matricula_para_remover is None:
                print(f'Matrícula de código {codigo_para_excluir}, não foi encontrada.')
            else:
                lista_matricula.remove(matricula_para_remover)
                salvar_arquivo(lista_matricula, 'matriculas.json')
                print(f'Matrícula de código {codigo_para_excluir}, removida com sucesso.')
# -------------------------------------------------------------------------------------------------------------------- #
        elif opcao == '9':
            print()
            print('Voltando ao menu principal...')
            print()
            break
        else:
            print('Opção inválida, tente novamente.')

    return lista_matricula


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo, indent=4)


def main():
    lista_estudante = []
    lista_professor = []
    lista_disciplina = []
    lista_turma = []
    lista_matricula = []

    while True:
        opcao = main_menu()

        if opcao == '1':
            lista_estudante = gerenciar_estudantes(lista_estudante)
        elif opcao == '2':
            lista_professor = gerenciar_professores(lista_professor)
        elif opcao == '3':
            lista_disciplina = gerenciar_disciplinas(lista_disciplina)
        elif opcao == '4':
            lista_turma = gerenciar_turmas(lista_turma)
        elif opcao == '5':
            lista_matricula = gerenciar_matriculas(lista_matricula)
        elif opcao == '9':
            print()
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida, tente novamente.')


main()
