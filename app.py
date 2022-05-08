from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
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

if __name__ == '__main__':
    app.run(debug=True)
