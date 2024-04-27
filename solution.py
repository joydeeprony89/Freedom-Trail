#https://leetcode.com/problems/freedom-trail/description/
#https://www.youtube.com/watch?v=NOgnlTXidSs

class solution(object):
    def findRotateSteps(self, ring, key):

        cache = {}
        def helper(r, k):
            if(k == len(key)):
                return 0
            if (r, k) in cache:
                return cache[(r, k)]
            res = float("inf")
            for i, c in enumerate(ring):
                if c == key[k]:
                    min_dist = min(
                                    abs(r - i), #clockwise
                                    len(ring) - abs(r - i) #anticlockwise
                                    )
                    res = min(
                                res,
                                min_dist + 1 + helper(i, k + 1)
                            )
            cache[(r, k)] = res
            return res
        return helper(0, 0)
    
sol = solution()
ans = sol.findRotateSteps("godding", "goddin")
print(ans)