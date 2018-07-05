import time

missing = object()

class cached_property(object):
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__
        self.__module__ = func.__module__

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, missing)
        if value is missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value

class Post(object):

    def __init__(self, text):
        self.text = text

    @cached_property
    def rendered_text(self):
        # return markdown_to_html(self.text)
        start = time.clock()
        not_cached = self.text
        res = str(fibonacci(1000000))[1:10]
        end = time.clock()
        print("elapsed:", end - start)

        return res + not_cached

def markdown_to_html(text):
    return "html(" + text + ")"
