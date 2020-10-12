from flask import Flask  # importa a biblioteca flask
from flask.globals import request
from flask.json import jsonify
from flask.templating import render_template

#Teste de pull request
app = Flask(__name__) #inicializa a API

@app.route('/') #cria uma rota 
def main():
  resultado = None
  media     = None
  
  # Parametros inseridos via template html
  primeira = request.args.get('primeira')
  segunda  = request.args.get('segunda')
  
  # Parametros inseridos formato JSON (Postman)
  #primeira = request.json['primeira']
  #segunda  = request.json['segunda']

  if primeira and segunda:
    primeira = float(primeira)
    segunda  = float(segunda)

    media = (primeira + segunda) / 2

    if media >= 7:
      resultado = 'Aprovado'
    elif media >= 4:
      resultado = 'Recuperação' 
    else:
      resultado = 'Reprovado'

  # Cria uma lista
  #  lista = [
  #            {'media': media, 'resultado': resultado},
  #            {'media': media, 'resultado': resultado}
  #          ]
  # Retorna uma lista no formato JSON
  #return jsonify(results = lista)

  # Retorna um resultado em JSON
  #return jsonify({'resultado': resultado, 'media': media})

  # Retorna resultado por um template html
  return render_template('index.html', media=media, resultado=resultado) 


if __name__ == '__main__':
    app.run(debug=True) #executa a aplicação
