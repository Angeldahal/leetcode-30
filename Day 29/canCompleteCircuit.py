"""
Problem Description:
    There are N gas stations along a circular route, where the amount of gas at
    station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to
    travel from station i to its next station (i+1). You begin the journey with
    an empty tank at one of the gas stations.

    Return the starting gas station's index if you can travel around the
    circuit once in the clockwise direction, otherwise return -1.

    Note:
        - If there exists a solution, it is guaranteed to be unique.
        - Both input arrays are non-empty and have the same length.
        - Each element in the input arrays is a non-negative integer.

Example:
    Input:
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]

    Output: 3

    Input:
        gas  = [2,3,4]
        cost = [3,4,3]

    Output: -1

"""
# solution:

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1

        tank = idx = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0: tank, idx = 0, i+1
        return idx
    

# Test cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(solution.canCompleteCircuit([2,3,4], [3,4,3]))
    print(solution.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
    print(solution.canCompleteCircuit([3,1,1], [1,2,2]))
    print(solution.canCompleteCircuit([1,2], [2,1]))
    print(solution.canCompleteCircuit([2], [2]))