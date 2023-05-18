import os
from flask_mail import Mail, Message
from flask import Flask, render_template, request
app = Flask(__name__)
mail = Mail(app)
@app.route('/')
def home():
    return render_template("index.html", title="ViaConte")

@app.route('/quemsomos')
def quemSomos():
    return render_template("quemSomos.html", title="Quem somos")

@app.route('/servicos')
def servicos():
    return render_template("servicos.html", title="Serviços")

@app.route('/blog')
def blog():
    return render_template("blog.html", title="Blog")

@app.route('/entreEmContato')
def entreEmContato():
    return render_template("entreEmContato.html", title="Entre em contato")
@app.route('/handle_data', methods=['POST'])
def enviarEmail():
    print(request.form.get("email"))
    print("jardel")
    return ""

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)

