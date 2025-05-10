from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from models.vehicle import Vehicle
from models.schedule import Schedule

class PicoPlacaForm(FlaskForm):
    plate = StringField('License Plate', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    submit = SubmitField('Check Restriction')

    def __init__(self, *args, **kwargs):
        super(PicoPlacaForm, self).__init__(*args, **kwargs)
        self.schedule = Schedule()

    def validate_plate(self, field):
        try:
            vehicle = Vehicle(field.data)
        except ValueError:
            raise ValidationError('Invalid plate format. Must be ABC-1234')

    def validate_date(self, field):
        if not self.schedule.check_date(field.data):
            raise ValidationError('Invalid date format. Must be YYYY-MM-DD')

    def validate_time(self, field):
        if not self.schedule.check_time(field.data):
            raise ValidationError('Invalid time format. Must be HH:MM')