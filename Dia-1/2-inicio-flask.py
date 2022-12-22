from flask import Flask


app = Flask(__name__)
# patron de diseño de software (Singleton)

@app.route('/')
def inicio():
    return 'hola desde mi servidor de Flask'

app.run(debug=True)