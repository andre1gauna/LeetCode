class MyHashSet:

    def __init__(self):
        self.size = 10**6 + 1
        self.v = [False] * self.size

    def add(self, key: int) -> None:
        self.v[key] = True

    def remove(self, key: int) -> None:
        self.v[key] = False
        

    def contains(self, key: int) -> bool:
        return self.v[key]
    
#TODO: revisar 11 e 12,  repensar 13 e 14