from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_o_flash'

# 🏠 ROTA DA PÁGINA DE LOGIN
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cnpj = request.form.get('cnpj')
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        if cnpj and email and senha:
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Por favor, preencha todos os campos.', 'error')
            
    return render_template('index.html')

# 🟢 ROTA DA PÁGINA SAIBA MAIS
@app.route('/saiba-mais')
def saiba_mais():
    return render_template('saiba_mais.html')

# 🔒 ROTA DA PÁGINA ESQUECI A SENHA
@app.route('/esqueci-senha', methods=['GET', 'POST'])
def esqueci_senha():
    if request.method == 'POST':
        return redirect(url_for('verificar_codigo')) 
    return render_template('esqueci_senha.html')

# 🔢 ROTA: VERIFICAR CÓDIGO
@app.route('/verificar-codigo', methods=['GET', 'POST'])
def verificar_codigo():
    if request.method == 'POST':
        return redirect(url_for('nova_senha')) 
    return render_template('verificar_codigo.html')

# 🔑 ROTA: DEFINIR NOVA SENHA
@app.route('/nova-senha', methods=['GET', 'POST'])
def nova_senha():
    if request.method == 'POST':
        flash('Senha redefinida com sucesso! Faça login com a nova senha.', 'success')
        return redirect(url_for('index')) 
    return render_template('nova_senha.html')

# 📝 ROTA: CADASTRO DE USUÁRIO
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        flash('Conta criada com sucesso! Bem-vindo ao MaxLucro.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('cadastro.html')

