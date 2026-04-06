class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res, half = 0, (len(nums1)+len(nums2))//2
        A, B = nums1, nums2

        if len(A) < len(B):
            l, r = 0, len(A)-1
        else:
            A, B = B, A
            l, r = 0, len(A)-1

        while True:
            m = (l + r) // 2
            l2 = half - m - 2

            part1L = A[m] if m >= 0 else float('-inf')
            part1R = A[m+1] if m+1 < len(A) else float('inf')
            part2L = B[l2] if l2 >= 0 else float('-inf')
            part2R = B[l2+1] if l2+1 < len(B) else float('inf')


            if  part1L > part2R:
                r = m-1
            elif part2L > part1R:
                l = m+1
            else:
                break

        if (len(A) + len(B)) % 2 == 0:
            res = (min(part1R, part2R) + max(part1L, part2L)) / 2
        else:
            res = (min(part1R, part2R))

        return res
            

