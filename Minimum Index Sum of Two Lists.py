class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        h1={list1[i]:i for i in range(len(list1))}
        h2={list2[i]:i for i in range(len(list2))}
        
        index=2001
        for i in h1:
            if(i in h2):
                index=min(index,h1[i]+h2[i])
                
        result=[]
        for i in h1:
            if(i in h2):
                if(h1[i]+h2[i]==index):
                    result.append(i)
                    
        return result
