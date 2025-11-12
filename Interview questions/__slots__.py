#Instances of classes with __slots__ have no __dict__ by default
class DataPoint:
    __slots__ = ("x", "y", "label")   # no __dict__, only these attrs allowed
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

p = DataPoint(1.0,2.0,"A")
print(p.label)