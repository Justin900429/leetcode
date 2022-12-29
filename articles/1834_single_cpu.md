# 1834 - Single-Threaded CPU

## Description
You are given `n`​​​​​​ tasks labeled from `0` to `n - 1` represented by a 2D integer array tasks, where $\text{tasks}[i]$ = `[enqueueTimei, processingTimei]` means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

### Example
```text
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
```

## Concept
This problem requires us to pick the sortest available tasks at each time. We can first sort the original tasks to get the first task. Later, we can maintain a min heap to decide which task will be processed. Note that if there are still some tasks but not in the candidate list, we should fill the time gap by moving the first element from `tasks` to the candidate array.


## Solution
```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [task + [idx] for idx, task in enumerate(tasks)]
        tasks = deque(sorted(tasks))
        temp = []

        cur_time = tasks[0][0] + tasks[0][1]
        res = [tasks.popleft()[-1]]

        while temp or tasks:
            while tasks and tasks[0][0] <= cur_time:
                out = tasks.popleft()
                heapq.heappush(temp, out[1:])
            
            # Fill the gap if no candiadate in temp
            if not temp:
                cur_time = tasks[0][0] + tasks[0][1]
                heapq.heappush(temp, tasks.popleft()[1:])
           
            res.append(temp[0][-1])
            cur_time += temp[0][0]
            heapq.heappop(temp)

        return res
```

> Time complexity: $O(n \log n)$ \
> Space complexity: $O(n)$
