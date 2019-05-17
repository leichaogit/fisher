from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired


class SearchForms(Form):
    q = StringField(validators=[DataRequired(),length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=0, max=500)], default=1)
