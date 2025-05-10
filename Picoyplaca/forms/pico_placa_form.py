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
    
    def validate_plate(self, field):
        try:
            Vehicle(field.data)
        except ValueError as e:
            raise ValidationError(str(e))

    def validate_date(self, field):
        try:
            Schedule().check_date(field.data)
        except ValueError as e:
            raise ValidationError(str(e))

    def validate_time(self, field):
        try:
            Schedule().check_time(field.data)
        except ValueError as e:
            raise ValidationError(str(e))