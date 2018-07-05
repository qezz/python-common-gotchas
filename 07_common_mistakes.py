def foo(bar=[]):         # bar is optional and defaults to [] if not specified
    bar.append("baz")    # but this line could be problematic, as we'll see...
    return bar

def fixed_foo(bar = None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar

def fixed_foo2(bar=[]):
    bar = bar.copy()
    bar.append("baz")
    return bar
