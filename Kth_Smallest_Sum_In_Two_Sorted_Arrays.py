class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        import heapq
        visited = {}
        h = [(A[0]+B[0],(0,0))]
        if not A or not B:
            return 0
        r, c =len(A), len(B)
        cnt = 0
        res = 0
        while cnt != k:
            res,(x,y) = heapq.heappop(h)
            if x+1 < r and (x+1,y) not in visited:
                heapq.heappush(h,(A[x+1]+B[y],(x+1,y)))
                visited[(x+1,y)] = 1
            if y+1 < c and (x,y+1) not in visited:
                heapq.heappush(h,(A[x]+B[y+1],(x,y+1)))
                visited[(x,y+1)] = 1
            cnt += 1
        return res