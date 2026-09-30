class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        freq_lst = [-f for f in cnt.values()]
        heapq.heapify(freq_lst)
        time = 0

        while freq_lst:
            temp = []
            for _ in range(n + 1):
                if freq_lst:
                    freq = heapq.heappop(freq_lst)
                    temp.append(freq + 1)
            
            for f in temp:
                if f < 0:
                    heapq.heappush(freq_lst, f)

            if freq_lst:
                time += n + 1
            else:
                time += len(temp)

        return time
