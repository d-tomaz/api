# Importando os módulos necessários
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

# Criando a instância do aplicativo Flask
app = Flask(__name__)

# Configurando o CORS (Cross-Origin Resource Sharing)
CORS(app)

# Definindo a rota '/buscar' com o método POST
@app.route('/buscar', methods=['POST'])

def buscar_operadoras():
    # Obtendo o termo de busca a partir do corpo da requisição
    termo_busca = request.json.get('termo_busca', '')
    
    # Abrindo o arquivo CSV
    with open('Relatorio_cadop.csv', 'r', encoding='iso-8859-1') as arquivo_csv:
        # Criando um leitor CSV
        leitor_csv = csv.reader(arquivo_csv)
        
        # Lista para armazenar as linhas semelhantes encontradas
        linhas_semelhantes = []

        # Iterando sobre cada linha do arquivo CSV
        for linha in leitor_csv:
            # Normalizando os campos da linha, convertendo para minúsculas e removendo espaços em branco
            linha_normalizada = [campo.lower().strip() for campo in linha]

            # Verificando se o termo de busca está presente em algum campo da linha normalizada
            if any(termo_busca.lower() in campo for campo in linha_normalizada):
                # Se sim, adiciona a linha à lista de linhas semelhantes
                linhas_semelhantes.append(linha)

    # Retorna as linhas semelhantes como resposta em formato JSON
    return jsonify(linhas_semelhantes)
    
# Executa o aplicativo Flask se o arquivo for executado diretamente
if __name__ == '__main__':
    app.run()