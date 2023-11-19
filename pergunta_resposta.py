import csv

def carregar_quiz(arquivo_quiz):
    with open(arquivo_quiz, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        quiz = list(csv_reader)
    return quiz

def exibir_pergunta(pergunta, opcoes_resposta):
    print(pergunta)
    for i, opcao in enumerate(opcoes_resposta, start=1):
        print(f"{chr(96 + i)}. {opcao}")

def coletar_respostas(quiz):
    respostas_usuario = []

    for pergunta, *opcoes_resposta in quiz:
        exibir_pergunta(pergunta, opcoes_resposta)
        resposta_usuario = input("Escolha a resposta (a-e): ").lower()
        respostas_usuario.append(resposta_usuario)

    return respostas_usuario

def salvar_respostas(respostas_usuario, arquivo_saida):
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as result_file:
        csv_writer = csv.writer(result_file)
        csv_writer.writerow(["Resposta do Usuário"])
        csv_writer.writerows(map(lambda x: [x], respostas_usuario))

if __name__ == "__main__":
    arquivo_quiz = 'pesquisahack.csv'
    arquivo_respostas = 'respostas_usuario.csv'

    quiz = carregar_quiz(arquivo_quiz)
    respostas_usuario = coletar_respostas(quiz)
    salvar_respostas(respostas_usuario, arquivo_respostas)

    print("Respostas coletadas e salvas com sucesso.")
