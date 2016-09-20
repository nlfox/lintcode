class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        father = [i for i in xrange(n)]
        cnt = n

        def find(n):
            while n != father[n]:
                n = father[n]
            return n

        def union(p, q):
            pRoot, qRoot = find(p), find(q)
            if pRoot == qRoot:
                return False
            father[pRoot] = qRoot
            global cnt
            cnt -= 1
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return False

        for i in xrange(1, n):
            if find(i - 1) != find(i):
                return False
        return True


print Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
