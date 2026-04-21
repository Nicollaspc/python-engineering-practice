import os
from datetime import date

ARQUIVO_AGENDA = "agenda.txt"
MODO_LER = "r"
MODO_ESCREVER = "w"
MODO_ADICIONAR = "a"
def adicionar_agendamento(text_agendamento):
    horario_desejado = text_agendamento.split(" - ")[0]
    try:
        if os.path.exists(ARQUIVO_AGENDA):
            with open(ARQUIVO_AGENDA,MODO_LER) as arquivo:
                todas_as_linhas = arquivo.readlines()

            for linha in todas_as_linhas:
                horario_ocupado = linha.split(" - ")[0]
                if horario_ocupado == horario_desejado:
                    print(f"Conflito: O horário das {horario_desejado} já está ocupado!")
                    return

        with open(ARQUIVO_AGENDA,MODO_ADICIONAR) as arquivo:
            arquivo.write(text_agendamento + "\n")
        print(f"\033[32mSucesso: '{text_agendamento}' adicionado\033[m")

    except Exception as err:
        print(f"Erro ao salvar agendamento: {err} ")

def ler_agenda():
    try:
        if not os.path.exists(ARQUIVO_AGENDA):
            print("A agenda esta vazia")
            return
        with open(ARQUIVO_AGENDA,MODO_LER) as arquivo:
            conteudo = arquivo.read()
            if not conteudo:
                print()
                print("\033[31mNenhum\033[0m" + " agendamento ativo")
                print()
            else:
                hoje = date.today()
                print(f"--- AGENDA DO DIA {hoje.strftime('%d/%m/%Y')} ---")
                print(conteudo)
                print("--------------------------------------------------")

    except Exception as err:
        print(f"Falha ao tentar ler o arquivo da agenda: {err}")

def cancelar_agendamento(text_cancelamento):
    try:
        with open(ARQUIVO_AGENDA,MODO_LER) as arquivo:
            todos_as_linhas = arquivo.readlines()

        linhas_que_ficam = []
        encontrado = False

        for linha in todos_as_linhas:
            if linha.strip() == text_cancelamento:
                encontrado = True
            else:
                linhas_que_ficam.append(linha)

        with open(ARQUIVO_AGENDA,MODO_ESCREVER) as arquivo:
            for linha in linhas_que_ficam:
                arquivo.write(linha)

        if encontrado:
            print(f"\033[32mSucesso: {text_cancelamento} foi cancelado e removido da agenda\033[m")
        else:
            print(f"Falha: {text_cancelamento} não estava na agenda")

    except Exception as err:
        print(f"Erro inesperado ao tentar cancelar: {err}")

def limpar_agenda():
    try:
        if not os.path.exists(ARQUIVO_AGENDA):
            print("Aviso: O arquivo não foi encontrado ou já está vazio.")
            return

        with open(ARQUIVO_AGENDA, MODO_ESCREVER):
            pass
        print("\033[32mSucesso: A agenda foi totalmente limpa!\033[m")

    except Exception as e:
        print(f"Falha ao tentar limpar o arquivo: {e}")

if __name__ == "__main__":
    print("---------------------------------")
    print('\033[92mIniciando o Sistema do Pet Shop\033[m')
    print("---------------------------------")
    while True:
        print("\033[36m[1] Ver Agenda\033[m")
        print("\033[34m[2] Novo Agendamento\033[m")
        print("\033[35m[3] Cancelar Agendamento\033[m")
        print("\033[33m[4] Limpar Agenda\033[m")
        print("\033[97m[5] Sair\033[m")
        try:
            resposta = int(input("Escolha uma opção: ").strip())
            match resposta:
                case 1:
                    ler_agenda()
                case 2:
                    texto_agendamento = input("Agendar: ")
                    adicionar_agendamento(texto_agendamento)
                case 3:
                    texto_cancelamento = input("Cancelar: ")
                    cancelar_agendamento(texto_cancelamento)
                case 4:
                    limpar_agenda()
                case 5:
                    break
                case _:
                    print("Opção invalida! Por favor, Escolha um numero de 1 a 4.")
        except ValueError:
            print("\033[31mErro: Por favor, digite apenas números letras não são aceitas\033[0m")