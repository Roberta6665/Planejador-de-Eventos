import re

def sugerir_menu(tipo_evento):
    menus = {
        "churrasco": [
            "Carne de boi",
            "Barriga",
            "Tulipa",
            "Coração",
            "Linguiça",
            "Vinagrete",
            "Arroz",
            "Pão de alho"
        ],
        "aniversário": ["Bolo", "Doces", "Salgados", "Refrigerantes"],
        "casamento": ["Buffet completo", "Bolo de casamento", "Vinhos"]
    }

    print("\nSugestões de Menu:")
    for item in menus[tipo_evento.lower()]:
        print(f"- {item}")

def calcular_itens_essenciais(num_convidados, duracao, tipo_evento):
    print("\n🎉 Planejador de Eventos 🎉")
    print(f"Para o seu {tipo_evento} com {num_convidados} convidados e duração de {duracao} horas:")

    if tipo_evento.lower() == "churrasco":
        custo_carne = (250 / 5) * (num_convidados / 5) 
    else:
        custo_carne = (380 / 5) * (num_convidados / 5) 

    custo_bebidas = 150 * duracao  
    acompanhamentos = 2 * num_convidados 
    custo_acompanhamentos = 20 * acompanhamentos  

    print(f"- Carne necessária: {num_convidados * (0.4 if tipo_evento.lower() == 'churrasco' else 0.2):.2f} kg")
    print(f"- Bebidas: {1.5 * num_convidados * duracao:.2f} litros")
    print(f"- Acompanhamentos: {acompanhamentos} porções")

    sugerir_menu(tipo_evento)

    custo_estimado = custo_carne + custo_bebidas + custo_acompanhamentos
    print(f"\n💰 Custo estimado: R$ {custo_estimado:.2f}")

    contato = input("Por favor, digite seu número de telefone: ")
    while not re.match(r'^\+?[0-9]{10,15}$', contato):
        print("Número de telefone inválido. Insira um número válido (10 a 15 dígitos).")
        contato = input("Por favor, digite seu número de telefone: ")

    email = input("Por favor, digite seu email: ")
    while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Email inválido. Insira um email válido.")
        email = input("Por favor, digite seu email: ")

    print("Obrigada pelas informações, entraremos em contato o mais breve possível.")
    return contato, email

def obter_input_usuario():
    while True:
        try:
            num_convidados = int(input("Digite o número de convidados: "))
            if num_convidados <= 0:
                print("Valor inválido. O número deve ser maior que zero.")
                continue
        except ValueError:
            print("Valor inválido. Apenas números são permitidos.")
            continue

        while True:
            try:
                duracao = int(input("Digite a duração do evento em horas: "))
                if duracao <= 0:
                    print("Valor inválido. A duração deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Valor inválido. Apenas números são permitidos.")

        while True:
            tipo_evento = input("Digite o tipo de evento (churrasco, aniversário, casamento): ").strip().lower()
            if tipo_evento not in ["churrasco", "aniversário", "casamento"]:
                print("Valor inválido. Escolha entre churrasco, aniversário ou casamento.")
                continue
            break

        return num_convidados, duracao, tipo_evento

def interagir_usuario():
    print("👋 Olá! Bem-vindo ao Planejador de Eventos!")
    continuar = 's'
    while continuar.lower() == 's':
        num_convidados, duracao, tipo_evento = obter_input_usuario()
        contato, email = calcular_itens_essenciais(num_convidados, duracao, tipo_evento)
        continuar = input("\nGostaria de planejar outro evento? (s/n): ")

    print("\n🙏 Obrigado por usar o Planejador de Eventos! Até a próxima!")

interagir_usuario()

