# 线程隔离体验
from werkzeug.local import LocalStack
from threading import Thread

thread_local_test = LocalStack()
thread_local_test.push(1)
print("the main thread %s" % thread_local_test.top)
print("the main thread %s" % thread_local_test.top)


def thread_local():
    print("this is a thread test %s" % thread_local_test.top)
    thread_local_test.push(2)
    print("this is a thread test %s" % thread_local_test.top)
    print("this is a thread test %s" % thread_local_test.top)


my_test = Thread(target=thread_local, name="thread_test")
my_test.start()
