from werkzeug.routing import ValidationError
from wtforms import Form, StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, length, Email

from app.models.user import User


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), length(8, 64),
                                    Email(message="电子邮箱不符合规范")])
    password = PasswordField(validators=[
        DataRequired(message="密码不能为空,请输入您的密码"), length(6, 32)])


class RegisterForm(LoginForm):
    nickname = StringField(validators=[
        DataRequired(), length(2, 10, message="昵称最少需要两个字符，最多10个字符")])

    password = PasswordField(validators=[
        DataRequired(message="密码不能为空,请输入您的密码"), length(6, 32)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("电子邮箱已经被注册")

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError("电子邮箱已经被注册")

