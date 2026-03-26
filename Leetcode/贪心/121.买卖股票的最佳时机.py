from typing import List


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        # 初始化历史最低价格为无穷大（或者数组第一个元素）
        min_price = float('inf')
        # 初始化最大利润为 0
        max_profit = 0

        for price in prices:
            # 贪心策略 1：如果今天的价格比历史最低还低，更新历史最低
            if price < min_price:
                min_price = price
            # 贪心策略 2：如果今天卖出利润更大，更新最大利润记录
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


if __name__ == "__main__":
    pass
