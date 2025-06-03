class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Test
if __name__ == "__main__":
    m = Multiplier(3)
    print("Is m callable?", callable(m))
    print("Calling m(5):", m(5))
