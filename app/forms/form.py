from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, DataRequired, NumberRange


class SearchForms(Form):
    q = StringField(DataRequired, validators=[length(min=1, max=30)])
    page = IntegerField(NumberRange(min=0, max=500))
