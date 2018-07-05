class TestWithClass():
    # should not return `self`
    # so the constructor is not expected

    # called when used in `with TestClass(6) as m`
    def __enter__(self):
        print("Hello")
        print("self.x: ", self.x)
        self.x = 100
        print("self.x: ", self.x)
        return "meow"

    # called when out of scope
    def __exit__(self, exc_type, exc_val, exc_tb):
        # raise Exception
        print("Bye")
