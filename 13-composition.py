class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

# Test
if __name__ == "__main__":
    e = Engine()
    c = Car(e)
    c.start()
