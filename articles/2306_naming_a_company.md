# 2306 - Naming a Company

## Problme Description

You are given an array of strings `ideas` that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from `ideas`, call them `ideaA` and `ideaB`.
Swap the first letters of `ideaA` and `ideaB` with each other.
If both of the new names are not found in the original `ideas`, then the name `ideaA ideaB` (the concatenation of `ideaA` and `ideaB`, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

### Example

```text
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
```

## Concept

We group the words by the first letter, the rest of the letters are saved into the hash set. We only have to compute the number of same letters within two set. The different combination of two sets can be found by the formula: `2 * (len(set1) - num_same) * (len(set2) - num_same)`

## Solution

```python
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        exist=  [set() for _ in range(26)]
        for idea in ideas:
            exist[ord(idea[0]) - ord('a')].add(idea[1:])

        answer = 0
        for idx in range(25):
            for idy in range(idx + 1, 26):
                num_the_same = len(exist[idx] & exist[idy])
                answer += 2 * (len(exist[idx]) - num_the_same) * (len(exist[idy]) - num_the_same)

        return answer
```

$n$ is the length of the array. $m$ is the maximum length (or average) of the string.

> Time complexity: $O(mn)$ \
> Space complexity: $O(mn)$

Note that building the hash set requires $O(nm)$ time because each string needs to be hashed according to its length. In each iteration, we use $O(nm)$ to find the same suffix letters, and we have total $26 * 25$ iterations. Therefore, the total time complexity is $O(mn)$.
