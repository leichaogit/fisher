from app import create_app
from app.models import db

app = create_app()

db.init_app(app)
# 增加上下文管理器，添加入栈
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True, port=5000)

