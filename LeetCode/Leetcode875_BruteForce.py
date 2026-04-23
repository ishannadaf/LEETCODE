"""

875. Koko Eating Bananas (Brute Force)
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during that hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation: Koko can eat 4 bananas per hour. One way to eat all the bananas in 8 hours is:
- Eat 3 bananas from pile 1, hours = 1
- Eat 4 bananas from pile 2, hours = 2 (2 bananas left)
- Eat 4 bananas from pile 2, hours = 3 (0 bananas left)
- Eat 4 bananas from pile 3, hours = 4 (3 bananas left)
- Eat 4 bananas from pile 3, hours = 5 (0 bananas left)
- Eat 4 bananas from pile 4, hours = 6 (7 bananas left)
- Eat 4 bananas from pile 4, hours = 7 (3 bananas left)
- Eat 4 bananas from pile 4, hours = 8 (0 bananas left)

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: Koko can eat 30 bananas per hour. One way to eat all the bananas in 5 hours is:
- Eat 30 bananas from pile 1, hours = 1 (0 bananas left)
- Eat 30 bananas from pile 2, hours = 2 (0 bananas left)
- Eat 30 bananas from pile 3, hours = 3 (0 bananas left)
- Eat 30 bananas from pile 4, hours = 4 (0 bananas left)
- Eat 30 bananas from pile 5, hours = 5 (0 bananas left)



🧠 Approach 1 — Brute Force
💡 Idea

Try all k from 1 → max(piles)

"""

import math

def minEatingSpeed(piles, h):
    for k in range(1, max(piles) + 1):
        total_hours = 0
        
        for p in piles:
            total_hours += math.ceil(p / k)
        
        if total_hours <= h:
            return k
        
        
        
# Time Complexity: O(n * m) where n is the number of piles and m is the maximum number of bananas in 
# a pile (since we are trying all k from 1 to max(piles))
# Space Complexity: O(1) since we are not using any extra space
