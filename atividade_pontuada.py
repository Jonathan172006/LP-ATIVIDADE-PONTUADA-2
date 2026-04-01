import os
import time

# ==========================================
# 1. VETORES (LISTAS) COM OS DADOS DO SISTEMA
# ==========================================
codigos_exames = [1, 2, 3, 4, 5, 6, 7]
nomes_exames = [
    "Hemograma Completo",
    "Raio-X",
    "Ultrassonografia",
    "Eletrocardiograma",
    "Tomografia",
    "Ressonância Magnética",
    "Exame de Glicose"
]
precos_exames = [45.00, 120.00, 180.00, 150.00, 750.00, 1300.00, 20.00]

# Vetores para armazenar temporariamente as escolhas do paciente
exames_escolhidos_id = []
exames_escolhidos_nomes = []
subtotal = 0.0

# ==========================================
# 2. LAÇO DE REPETIÇÃO: SELEÇÃO DE EXAMES
# ==========================================
while True:
    # Limpa a tela direto no código 
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Exibe o menu iterando sobre os vetores
    print("=" * 55)
    print(f"{'HOSPITAL VIDA PLENA - AGENDAMENTO':^55}")
    print("=" * 55)
    print(f"{'ID.':<5} | {'NOME DO EXAME':<25} | {'PREÇO':>15}")
    print("-" * 55)
    
    for i in range(len(codigos_exames)):
        print(f"{codigos_exames[i]:<5} | {nomes_exames[i]:<25} | R$ {precos_exames[i]:>12.2f}")
        
    print("-" * 55)
    print("0     | Encerrar Seleção de Exames")
    print("=" * 55)
    
    # Recebe a entrada como texto normal
    entrada_opcao = input("\nDigite o código do exame desejado (ou 0 para finalizar): ")
    
    # Verifica se o texto digitado é exatamente uma das opções válidas antes de converter
    if entrada_opcao in ["0", "1", "2", "3", "4", "5", "6", "7"]:
        opcao = int(entrada_opcao)
    else:
        print("\n[Erro] Código inválido. Por favor, digite um número da lista.")
        time.sleep(2)
        continue

    # Regra de negócio: código "0" encerra o agendamento
    if opcao == 0:
        break
    
    # Validação do exame (agora temos certeza que é um número válido)
    # Encontra a posição do exame nos vetores originais
    indice = codigos_exames.index(opcao)
    
    # Adiciona nos vetores do "carrinho" e acumula o valor
    exames_escolhidos_id.append(codigos_exames[indice])
    exames_escolhidos_nomes.append(nomes_exames[indice])
    subtotal += precos_exames[indice]
    
    print(f"\n[Sucesso] '{nomes_exames[indice]}' adicionado ao agendamento!")
    time.sleep(1.5)
    
    # Regra de negócio: Perguntar se deseja adicionar outro exame
    while True:
        continuar = input("\nDeseja agendar outro exame? (S/N): ").strip().upper()
        if continuar in ['S', 'N']:
            break
        print("[Erro] Digite apenas 'S' para Sim ou 'N' para Não.")
        
    if continuar == 'N':
        break  # Sai do laço principal e vai para pagamento do subtotal acumulado

# ==========================================
# 3. CONDICIONAIS E PAGAMENTO (Apenas se comprou algo)
# ==========================================
if subtotal == 0:
    print("\nNenhum exame foi agendado. Encerrando o sistema...")
    time.sleep(2)
else:
    forma_pagamento = ""
    desconto = 0.0
    acrescimo = 0.0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 55)
        print(f"{'FORMA DE PAGAMENTO':^55}")
        print("=" * 55)
        print(f"Subtotal atual: R$ {subtotal:.2f}\n")
        print("1 - Convênio (Desconto de 15%)")
        print("2 - Particular (Sem desconto ou acréscimo)")
        print("3 - Cartão de Crédito (Acréscimo de 8%)")
        print("=" * 55)
        
        # Recebe a entrada do pagamento como texto
        entrada_pagamento = input("\nEscolha a forma de pagamento (1-3): ")
        
        # Verifica se o texto digitado é "1", "2" ou "3" antes de converter para número
        if entrada_pagamento in ["1", "2", "3"]:
            op_pagamento = int(entrada_pagamento)
        else:
            print("\n[Erro] Digite apenas 1, 2 ou 3.")
            time.sleep(2)
            continue

        # Aplicação das regras de pagamento
        if op_pagamento == 1:
            forma_pagamento = "Convênio"
            desconto = subtotal * 0.15
            break
        elif op_pagamento == 2:
            forma_pagamento = "Particular"
            break
        elif op_pagamento == 3:
            forma_pagamento = "Cartão de Crédito"
            acrescimo = subtotal * 0.08
            break

    # Cálculo do valor definitivo
    valor_final = subtotal - desconto + acrescimo

    # ==========================================
    # 4. EXIBIÇÃO DOS RESULTADOS (RECIBO)
    # ==========================================
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 55)
    print(f"{'RESUMO DO AGENDAMENTO - VIDA PLENA':^55}")
    print("=" * 55)
    print("EXAMES ESCOLHIDOS:")
    
    # Laço iterando os exames escolhidos
    for i in range(len(exames_escolhidos_id)):
        print(f" -> ID [{exames_escolhidos_id[i]:02d}] {exames_escolhidos_nomes[i]}")
    
    print("-" * 55)
    print(f"Subtotal:              R$ {subtotal:10.2f}")
    print(f"Forma de Pagamento:    {forma_pagamento}")
    
    # Valida o que exibir no recibo
    if desconto > 0:
        print(f"Desconto (15%):      - R$ {desconto:10.2f}")
    elif acrescimo > 0:
        print(f"Acréscimo (8%):      + R$ {acrescimo:10.2f}")
    else:
        print("Desconto/Acréscimo:    R$       0.00")
        
    print("=" * 55)
    print(f"VALOR FINAL A PAGAR:   R$ {valor_final:10.2f}")
    print("=" * 55)
    print("\nObrigado por utilizar o sistema do Hospital Vida Plena!")