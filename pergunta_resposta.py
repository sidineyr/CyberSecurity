import csv
import re

def carregar_quiz(arquivo_quiz):
    """Lê perguntas e alternativas em linhas separadas do arquivo atual."""
    quiz = []
    pergunta = None
    opcoes = []
    with open(arquivo_quiz, 'r', encoding='utf-8') as arquivo:
        for numero, linha in enumerate(arquivo, start=1):
            linha = linha.strip()
            if not linha:
                continue
            marcador = re.search(r'(?<!\w)a\)\s*', linha)
            if marcador and marcador.start() > 0:
                pergunta_nova, linha = linha[:marcador.start()].strip(), linha[marcador.start():]
                if pergunta is not None:
                    if len(opcoes) != 5:
                        raise ValueError(f'Pergunta anterior incompleta antes da linha {numero}')
                    quiz.append((pergunta, opcoes))
                pergunta, opcoes = pergunta_nova, []
            if re.match(r'^[a-e]\)\s*', linha):
                if pergunta is None:
                    raise ValueError(f'Alternativa sem pergunta na linha {numero}')
                esperado = chr(ord('a') + len(opcoes))
                if not linha.startswith(esperado + ')'):
                    raise ValueError(f'Alternativa fora de ordem na linha {numero}')
                opcoes.append(linha)
            else:
                if pergunta is not None:
                    if len(opcoes) != 5:
                        raise ValueError(f'Pergunta anterior incompleta antes da linha {numero}')
                    quiz.append((pergunta, opcoes))
                pergunta, opcoes = linha, []
    if pergunta is not None:
        if len(opcoes) != 5:
            raise ValueError('Última pergunta incompleta')
        quiz.append((pergunta, opcoes))
    return quiz

def exibir_pergunta(pergunta, opcoes_resposta):
    print(pergunta)
    for opcao in opcoes_resposta:
        print(opcao)

def coletar_respostas(quiz):
    respostas_usuario = []

    for pergunta, opcoes_resposta in quiz:
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
