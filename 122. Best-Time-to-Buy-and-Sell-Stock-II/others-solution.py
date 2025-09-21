from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

# 접근은 거의 비슷한데, 리스트에 저장하고 양수를 뽑아내는 과정 없이, 
# 단순히 양의 리턴이면 profit을 더하는 식으로 하면 0 ms까지 도달하는 것 같다.