class Counter:
    count=0

    def __init__(self):
        Counter .count += 1

    @classmethod

    def show_count(cls):
        print(f"Total no. of counts are: {cls.count}")

c1=Counter()
c2=Counter()  

Counter.show_count()
