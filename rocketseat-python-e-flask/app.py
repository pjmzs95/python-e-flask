# Importação
from flask import Flask

app = Flask(__name__)

# Definir uma rota raiz (pág. inicial) e a função que será executada ao requisitar
@app.route('/teste')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True) # Ativando o modo depuração:  Ajuda a receber mais informações quando requisições forem feitas e ter mais visibilidade do que está acontecendo com o servidor. Modo para Desenvolvimento, não utiizar para Produção(ambiente para vários users)