import math  # Para cálculos matemáticos

# Listas para armazenar os dados
culturas = []  # Nome das culturas
areas = []  # Áreas das culturas
insumos = []  # Tipos de insumos
taxa_aplicacao = []  # Taxa de aplicação (mL/m²)

while True:
    print("\n------- GESTÃO AGRÍCOLA FARMTECH 2025® -------")
    print("1 - Selecionar Cultura")
    print("2 - Exibir culturas adicionadas")
    print("3 - Atualizar informações")
    print("4 - Excluir dados")
    print("6 - Sair do programa")
    print("----------------------------------")

    opcao = input("\n- Escolha uma opção: ")

    if opcao == "1":
        # Selecionar Cultura
        while True:
            cultura_escolhida = input("Selecione a cultura (A - Arroz, F - Feijão): ").strip().upper()
            if cultura_escolhida == "A":
                cultura = "Arroz"
                break
            elif cultura_escolhida == "F":
                cultura = "Feijão"
                break
            else:
                print("Opção inválida! Escolha A para Arroz ou F para Feijão.")

        print("\nEscolha o formato da área plantada:")
        print("1 - Retângulo")
        print("2 - Círculo")
        print("3 - Trapézio")
        tipo_area = input("Digite o número correspondente: ")

        if tipo_area == "1":  # Retângulo
            largura = float(input("Digite a largura do terreno (m): "))
            comprimento = float(input("Digite o comprimento do terreno (m): "))
            area = largura * comprimento  # Cálculo da área do retângulo
        elif tipo_area == "2":  # Círculo
            raio = float(input("Digite o raio do terreno (m): "))
            area = math.pi * (raio ** 2)  # Cálculo da área do círculo
        elif tipo_area == "3":  # Trapézio
            base_maior = float(input("Digite a base maior (m): "))
            base_menor = float(input("Digite a base menor (m): "))
            altura = float(input("Digite a altura (m): "))
            area = ((base_maior + base_menor) * altura) / 2  # Cálculo da área do trapézio
        else:
            print("Opção inválida! Usando área 0.")
            area = 0  # Caso o usuário escolha uma opção inválida

        # Seleção do insumo
        while True:
            insumo_escolhido = input(
                "Escolha o insumo a ser utilizado (F - Fertilizante, P - Pesticida): ").strip().upper()
            if insumo_escolhido == "F":
                insumo = "Fertilizante"
                aplicacao_por_m2 = 500  # 500 mL/m² para fertilizante
                break
            elif insumo_escolhido == "P":
                insumo = "Pesticida"
                aplicacao_por_m2 = 250  # 250 mL/m² para pesticida
                break
            else:
                print("Opção inválida! Escolha F para Fertilizante ou P para Pesticida.")

        aplicacao_total = area * aplicacao_por_m2  # Cálculo da aplicação total

        # Armazenar os dados nas listas
        culturas.append(cultura)
        areas.append(area)
        insumos.append(insumo)
        taxa_aplicacao.append(aplicacao_total)

        # Mostrar a confirmação com aplicação em litros e a descrição do insumo
        if insumo == "Fertilizante":
            print(
                f"\nCultura {cultura} cadastrada com sucesso! Área: {area:.2f} m², Insumo: {insumo}, Aplicação: {aplicacao_total / 1000:.2f} litros, sendo 500 mL/m²")
        elif insumo == "Pesticida":
            print(
                f"\nCultura {cultura} cadastrada com sucesso! Área: {area:.2f} m², Insumo: {insumo}, Aplicação: {aplicacao_total / 1000:.2f} litros, sendo 250 mL/m²")

    elif opcao == "2":
        # Exibir Dados
        if not culturas:
            print("Nenhuma cultura cadastrada.")
        else:
            print("\nCulturas cadastradas:")
            for i in range(len(culturas)):
                if insumos[i] == "Fertilizante":
                    print(
                        f"{i + 1} - Cultura: {culturas[i]}, Área: {areas[i]:.2f} m², Insumo: {insumos[i]}, Aplicação: {taxa_aplicacao[i] / 1000:.2f} litros, sendo 500 mL/m²")
                elif insumos[i] == "Pesticida":
                    print(
                        f"{i + 1} - Cultura: {culturas[i]}, Área: {areas[i]:.2f} m², Insumo: {insumos[i]}, Aplicação: {taxa_aplicacao[i] / 1000:.2f} litros, sendo 250 mL/m²")

    elif opcao == "3":
        # Atualizar informações
        if not culturas:
            print("Nenhuma cultura cadastrada para atualizar.")
        else:
            print("\nCulturas cadastradas:")
            for i in range(len(culturas)):
                print(f"{i + 1} - Cultura: {culturas[i]}, Área: {areas[i]:.2f} m², Insumo: {insumos[i]}")

            # Escolher a cultura para atualizar
            indice = int(input("Escolha o número da cultura a ser atualizada: ")) - 1

            if 0 <= indice < len(culturas):
                print("\nO que deseja atualizar?")
                print("1 - Atualizar área")
                print("2 - Atualizar insumo")
                opcao_atualizar = input("Digite o número correspondente: ")

                if opcao_atualizar == "1":
                    # Atualizar área
                    tipo_area = input(
                        "Escolha o formato da nova área plantada (1 - Retângulo, 2 - Círculo, 3 - Trapézio): ")
                    if tipo_area == "1":  # Retângulo
                        largura = float(input("Digite a nova largura do terreno (m): "))
                        comprimento = float(input("Digite o novo comprimento do terreno (m): "))
                        area = largura * comprimento  # Cálculo da nova área do retângulo
                    elif tipo_area == "2":  # Círculo
                        raio = float(input("Digite o novo raio do terreno (m): "))
                        area = math.pi * (raio ** 2)  # Cálculo da nova área do círculo
                    elif tipo_area == "3":  # Trapézio
                        base_maior = float(input("Digite a nova base maior (m): "))
                        base_menor = float(input("Digite a nova base menor (m): "))
                        altura = float(input("Digite a nova altura (m): "))
                        area = ((base_maior + base_menor) * altura) / 2  # Cálculo da nova área do trapézio
                    else:
                        print("Opção inválida! Usando área 0.")
                        area = 0  # Caso o usuário escolha uma opção inválida

                    areas[indice] = area  # Atualizando a área na lista
                    aplicacao_total = area * (
                        500 if insumos[indice] == "Fertilizante" else 250)  # Atualizando aplicação
                    taxa_aplicacao[indice] = aplicacao_total  # Atualizando a taxa de aplicação
                    print(f"Área atualizada com sucesso! Nova área: {area:.2f} m².")

                elif opcao_atualizar == "2":
                    # Atualizar insumo
                    while True:
                        insumo_escolhido = input(
                            "Escolha o novo insumo (F - Fertilizante, P - Pesticida): ").strip().upper()
                        if insumo_escolhido == "F":
                            insumo = "Fertilizante"
                            aplicacao_por_m2 = 500  # 500 mL/m² para fertilizante
                            break
                        elif insumo_escolhido == "P":
                            insumo = "Pesticida"
                            aplicacao_por_m2 = 250  # 250 mL/m² para pesticida
                            break
                        else:
                            print("Opção inválida! Escolha F para Fertilizante ou P para Pesticida.")

                    insumos[indice] = insumo  # Atualizando o insumo
                    aplicacao_total = areas[indice] * aplicacao_por_m2  # Atualizando aplicação
                    taxa_aplicacao[indice] = aplicacao_total  # Atualizando a taxa de aplicação
                    print(f"Insumo atualizado com sucesso! Novo insumo: {insumo}.")

    elif opcao == "4":
        # Excluir dados
        if not culturas:
            print("Nenhuma cultura cadastrada para excluir.")
        else:
            print("\nCulturas cadastradas:")
            for i in range(len(culturas)):
                print(f"{i + 1} - Cultura: {culturas[i]}, Área: {areas[i]:.2f} m², Insumo: {insumos[i]}")

            # Escolher a cultura para excluir
            indice = int(input("Escolha o número da cultura a ser excluída: ")) - 1

            if 0 <= indice < len(culturas):
                # Remover o item selecionado
                culturas.pop(indice)
                areas.pop(indice)
                insumos.pop(indice)
                taxa_aplicacao.pop(indice)
                print("Cultura excluída com sucesso.")
            else:
                print("Número inválido! Nenhuma cultura foi excluída.")
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
