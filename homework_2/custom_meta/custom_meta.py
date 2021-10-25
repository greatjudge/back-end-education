class CustomMeta(type):
    def __new__(mcs, class_name, parents, attributes):
        cls_attrs = {}
        for name, attr in attributes.items():
            if not(name.startswith('__') and name.endswith('__')):
                name = 'custom_' + name
            cls_attrs[name] = attr
        return super().__new__(mcs, class_name, parents, cls_attrs)

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        obj_dict = {}
        for name, attr in obj.__dict__.items():
            if not(name.startswith('__') and name.endswith('__')):
                name = 'custom_' + name
            obj_dict[name] = attr
        obj.__dict__ = obj_dict
        return obj


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __add__(self, other):
        return self.custom_val + other.custom_val