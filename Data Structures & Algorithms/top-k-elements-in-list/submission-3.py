class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        tuple_lst = []
        for num, freq in cnt.items():
            tuple_lst.append((freq, num))

        tuple_lst.sort(reverse = True)
        res = []
        for i in range(k):
            res.append(tuple_lst[i][1])
        return res