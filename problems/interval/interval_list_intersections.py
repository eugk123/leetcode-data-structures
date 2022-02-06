"""
https://leetcode.com/problems/interval-list-intersections/
"""
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        def captureOverlap(first, second):
            # 0----1                              0----1
            #           0----1          0----1
            if first[1] < second[0] or first[0] > second[1]:
                return None, None     # left, right       
            # 0----------1
            #        0-------1
            elif first[1] >= second[0] and first[0] <= second[0] and first[1] < second[1]:
                return second[0], first[1]
            #        0-------1
            # 0----------1
            elif first[0] >= second[0] and first[0] <= second[1] and first[1] > second[1]:
                return first[0], second[1]
            # 0--------------1
            #      0----1
            elif first[0] <= second[0] and first[1] >= second[1]:
                return second[0], second[1]
            #      0----1
            # 0--------------1
            elif first[0] >= second[0] and first[1] <= second[1]:
                return first[0], first[1]
            
            
        i = 0
        j = 0
        result = []
        
        # continue to iterate until all intervals have been traversed
        # iterate one pointer at a time
        while i < len(firstList) and j < len(secondList):
            
            if i < len(firstList):
                first = firstList[i]
            if j < len(secondList):
                second = secondList[j]
    
            # capture overlap at every move
            left, right = captureOverlap(first, second)
            
            if left >= 0 and right >= 0:
                result.append([left, right])
                
            # move pointers
            if i == len(firstList):
                j += 1
            elif j == len(secondList):
                i += 1
            elif first[1] < second[1]:
                i += 1
            elif first[1] >= second[1]:
                j += 1
            
        return result