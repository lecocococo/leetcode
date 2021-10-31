class RandomizedSet:

#     def __init__(self):
#         self.dict = {}

#     def insert(self, val: int) -> bool:
#         if self.dict.get(val):
#             return False
#         else:
#             self.dict[val] = 1
#             return True

#     def remove(self, val: int) -> bool:
#         if self.dict.get(val):
#             self.dict.pop(val)
#             return True
#         return False

#     def getRandom(self) -> int:
        
#         return random.choice(list(self.dict.keys()))

    def __init__(self):
      self.dict = {}
      self.nums = []
        
    def insert(self, val):
        if val not in self.dict or self.dict[val] == 0:
            self.nums.append(val)
            self.dict[val] = 1
            return True
        return False
    
    def remove(self, val):
        if val not in self.dict or self.dict[val] == 0:
            return False
        self.dict[val] = 0
        index = self.nums.index(val)
        if index!=len(self.nums)-1:
            temp = self.nums[-1]
            self.nums[-1] = val
            self.nums[index]=temp
        self.nums.pop()
        return True
    
    def getRandom(self):
        return random.choice(self.nums)
