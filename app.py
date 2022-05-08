from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", title="ViaConte")

@app.route('/quemsomos')
def quemSomos():  # put application's code here
    return render_template("quemSomos.html", title="Quem somos")

@app.route('/servic os')
def servicos():  # put application's code here
    return render_template("servicos.html", title="Serviços")

@app.route('/blog')
def blog():  # put application's code here
    return render_template("blog.html", title="Blog")

@app.route('/entreEmContato')
def entreEmContato():  # put application's code here
    return render_template("entreEmContato.html", title="Entre em contato")

if __name__ == '__main__':
    app.run(debug=True)
