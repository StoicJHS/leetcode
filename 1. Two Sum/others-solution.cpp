// 아직 cpp이 익숙하지 않아서 공부용으로 한다.

#include <iostream>
#include <vector>
#include <unordered_map>


class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> pairIdx;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (pairIdx.find(target - num) != pairIdx.end()) {
                return {i, pairIdx[target - num]};      
            }
            pairIdx[num] = i;
        
            }

    return {}; 
    }

};

// 3 ms | Beats 69.89%
// 14.88 MB | Beats 35.99%


// 별해

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.count(complement)) {
                return {map[complement], i};
            }
            map[nums[i]] = i;
        }
        return {};
    }
};