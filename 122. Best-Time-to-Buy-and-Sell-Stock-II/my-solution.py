# 2025-09-21 (Sun) 14:23
# 솔루션 안보고 혼자 고민해서 생각보다 빠른 시간 내에 풀어냈다! 
# medium 정도도 잘 고민해서 하면 충분히 풀 수 있다! 자신감을 얻었다.

# -------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+


# *****************************************
# 122. Best Time to Buy and Sell Stock II *
# *****************************************

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

# -------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
# 사고의 흐름
# 일단, price 계열이 나오고 profit이 등장하였기에, return array를 생각해 볼 수 있었다.
# 그 다음, Example 3가지 예시를 통해서 몇가지 확인

# Example 1: positive return과 negative return이 섞여있음
# Example 2: Monotonic increasing returns
# Example 3: Monotonic decreasing returns

# 처음에는 전부 탐색하나 싶었지만 prices.length가 거의 3만인 것을 보고 아니라고 판단
# 문뜩, Example 1에서 positive return의 합이 total profit과 일치하는 것을 확인
# Example 2에서도 같은 식으로 1+1+1+1+1 = 5가 되었다.
# Example 3에서는 모두 negative return이었으므로 0

# 이를 통해서, 시계열을 이미 전부 파악하고 있다는 가정하에, 양의 리턴만을 모두 모아오면 
# 결국 max profit이 된다는 것을 알았다
# 뒤에 같은 날에 사고 판다는 것등이 혼란을 유발할 수 있었지만 결국 제일 이상적인 조건을 부여한 것
# -------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
# 코드 작성
# 1. returns라는 리스트를 만들고 여기다가 리턴 값을 넣을 것이다
# 2. 개선의 여지가 있지만, 첫날을 return이 0이니 returns[0] = 0으로 고정
# 3. 그 다음부터는 i번째 price에서 i-1번째 price를 빼서 i번째 리턴으로 취급
# 4. 얻어진 returns에서 양수만 뽑아서 합산하면 max profit이 된다.

# -------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+



from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # It is natural to introduce a return array
        returns = []
        max_profit = 0
        for i in range(len(prices)):
            if i == 0:
                returns.append(0)
            else:
                returns.append(prices[i]-prices[i-1])
        for j in range(len(returns)):
            if returns[j] > 0:
                max_profit += returns[j]
            
        return max_profit


# 4 ms | Beats 19.64 % (생각보다 효율이 떨어지는 듯)
# 18.94 MB | Beats 29.43 %


