class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

class C(A):
    def show(self):
        print("C's show")

class D(B, C):
    pass

# Test
if __name__ == "__main__":
    d = D()
    d.show()  # Will follow MRO: D -> B -> C -> A
