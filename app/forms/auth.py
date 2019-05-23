from wtforms import Form, StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, length, Email


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), length(8, 64),
                                    Email(message="电子邮箱不符合规范")])
    nickname = StringField(validators=[
        DataRequired(), length(2, 10, message="昵称最少需要两个字符，最多10个字符")])
    password = PasswordField(validators=[
        DataRequired(message="密码不能为空,请输入您的密码"), length(6, 32)])


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), length(8, 64),
                                    Email(message="电子邮箱不符合规范")])
    password = PasswordField(validators=[
        DataRequired(message="密码不能为空,请输入您的密码"), length(6, 32)])
