class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        import heapq
        visited = {}
        h = [(matrix[0][0],(0,0))]
        if not matrix:
            return 0
        r, c =len(matrix), len(matrix[0])
        kth = 0
        cnt = 0
        res = 0
        while cnt != k:
            res,(x,y) = heapq.heappop(h)
            if x+1 < r and (x+1,y) not in visited:
                heapq.heappush(h,(matrix[x+1][y],(x+1,y)))
                visited[(x+1,y)] = 1
            if y+1 < c and (x,y+1) not in visited:
                heapq.heappush(h,(matrix[x][y+1],(x,y+1)))
                visited[(x,y+1)] = 1
            cnt += 1
        return res