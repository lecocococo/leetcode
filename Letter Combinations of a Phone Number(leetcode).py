from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        num = []
        num.append([None])
        num.append([None])
        num.append(["a","b","c"])
        num.append(["d","e","f"])
        num.append(["g","h","i"])
        num.append(["j","k","l"])
        num.append(["m","n","o"])
        num.append(["p","q","r","s"])
        num.append(["t","u","v"])
        num.append(["w","x","y","z"])

        digit_list = list(digits)
        items = []
        for i in digit_list:
            items.append(num[int(i)])
        temp = list(product(*items))
        
        result = []
        for i in temp:
            result.append("".join(i))
            
        return result
