from flask import Flask, render_template
from forms.pico_placa_form import PicoPlacaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'trial1' 

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PicoPlacaForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

