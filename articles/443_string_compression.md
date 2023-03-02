# 443 - String Compression

## Problem Description

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string s. For each group of **consecutive repeating characters** in `chars`:

* If the group's length is `1`, append the character to `s`.
* Otherwise, append the character followed by the group's length.
The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array**, return the new length of the array.

You must write an algorithm that uses only constant extra space.

### Example

```text
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
```

> [Link to the problem](https://leetcode.com/problems/string-compression)

## Concept

To find all the groups of consecutive repeating characters, we use a pointer and a variable to check current charater and the next charater. If the next character is the same as the current character, we increment the counter. If the next character is different, we append the current character and the counter to the result array. We also reset the counter to 1. To also modify the input array, we use a second pointer to keep track of the index of the result array.

## Solution

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        
        cur_count = 1
        idx = j = 0

        while idx < len(chars):
            cur_count = 1

            while idx < len(chars) - 1 and chars[idx] == chars[idx + 1]:
                idx += 1
                cur_count += 1

            chars[j] = chars[idx]
            j += 1

            if cur_count > 1:
                for count in str(cur_count):
                    chars[j] = count
                    j += 1
            
            idx += 1

        return j
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$
