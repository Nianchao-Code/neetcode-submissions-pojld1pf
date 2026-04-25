class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        cnt = 0

        for c1, c2 in prerequisites:
            indegree[c1] += 1
            adj[c2].append(c1)

        q = deque()
        for i, val in enumerate(indegree):
            if val == 0:
                q.append(i)

        if not q:
            return False

        while q:
            c = q.popleft()
            cnt += 1

            for neighbor in adj[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return cnt == numCourses
