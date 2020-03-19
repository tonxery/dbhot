import importlib

path = "settings.Foo"

p,c = path.rsplit('.',maxsplit=1)
m = importlib.import_module(p)
cls = getattr(m,c)
print(cls)
#如果找到这个类
for key in dir(cls):
    if key.isupper():
        print(key,getattr(cls,key))
