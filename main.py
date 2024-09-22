import re

def calcular_itens_essenciais(num_convidados, duracao, tipo_evento):
    print("\n🎉 Planejador de Eventos 🎉")
    print(f"Para o seu {tipo_evento} com {num_convidados} convidados e duração de {duracao} horas:")

   
    carne = 0.4 * num_convidados if tipo_evento.lower() == "churrasco" else 0.2 * num_convidados
    bebidas = 1.5 * num_convidados * duracao 
    acompanhamentos = 2 * num_convidados 

   
    print(f"- Carne necessária: {carne:.2f} kg")
    print(f"- Bebidas: {bebidas:.2f} litros")
    print(f"- Acompanhamentos: {acompanhamentos} porções")
    print("\n🥳 Aproveite seu evento!")

def obter_input_usuario():
    while True:
        try:
            num_convidados = int(input("Digite o número de convidados: "))
            if num_convidados <= 0:
                raise ValueError
        except ValueError:
            print("Valor inválido. Apenas números são permitidos.")
            continue

        try:
            duracao = int(input("Digite a duração do evento em horas: "))
            if duracao <= 0:
                raise ValueError
        except ValueError:
            print("Valor inválido. Apenas números são permitidos.")
            continue

        tipo_evento = input("Digite o tipo de evento (churrasco, festa, etc.): ").strip()

       
        if not re.match("^[A-Za-z\s]+$", tipo_evento):
            print("Valor inválido. Apenas letras são permitidas.")
            continue

        return num_convidados, duracao, tipo_evento

def interagir_usuario():
    print("👋 Olá! Bem-vindo ao Planejador de Eventos!")
    continuar = 's'
    while continuar.lower() == 's':
        num_convidados, duracao, tipo_evento = obter_input_usuario()
        calcular_itens_essenciais(num_convidados, duracao, tipo_evento)
        continuar = input("\nGostaria de planejar outro evento? (s/n): ")

    print("\n🙏 Obrigado por usar o Planejador de Eventos! Até a próxima!")


interagir_usuario()
