def f(*args, **kwargs):
    print("Named:", args)

def f_(*args, **kwargs):
    print("Named:", kwargs)

f(100, 50, 25)
f_(galleons=100, sickles=50, knuts=25)