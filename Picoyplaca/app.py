from flask import Flask, render_template, flash, url_for
from forms.pico_placa_form import PicoPlacaForm
from models.vehicle import Vehicle
from models.day_restriction import DayRestriction
from models.time_restriction import TimeRestriction

app = Flask(__name__)
app.config['SECRET_KEY'] = 'trial1'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PicoPlacaForm()
    if form.validate_on_submit():
        try:
            plate = form.plate.data
            date = form.date.data
            time = form.time.data

            vehicle = Vehicle(plate)
            day_checker = DayRestriction()
            time_checker = TimeRestriction()

            has_day_restriction = day_checker.check_day_restriction(date, plate)
            has_time_restriction = time_checker.check_time_restriction(time)

            if has_day_restriction and has_time_restriction:
                flash('You can not drive at this time', 'error')
            else:
                flash('You can drive with no problem', 'success')

        except ValueError as e:
            flash(str(e), 'error')

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

