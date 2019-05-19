from app import create_app

app = create_app()
from werkzeug.local import Local
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=5000)
    # Threading
    # 线程，进程，GIL，多线程，flask线程隔离(采用字典的数据结构，导入werkzeug的Local包)
