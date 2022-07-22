class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter1 = Counter(arr1)
        res = []
        for e in arr2:
            while counter1[e]:
                res.append(e)
                counter1[e] -= 1
        print(list(counter1.elements()))
        res.extend(sorted(list(counter1.elements())))
        return res