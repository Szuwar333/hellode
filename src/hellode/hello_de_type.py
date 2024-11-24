class helo_type:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def test_value(self):
        print("This is a test value")
        return self.value
