class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        for s1, t1 in zip(s,t):
            if s1 not in m:
                m[s1] = t1
            elif m[s1] !=t1:
                return False
            # 예를들어 a와 b가 매칭되서 저장되면 a는 어떤 다른것과도 매칭불가 => 중복 허용 x
        return len(set(m.values())) == len(m.values())
