
import heapq
from collections import deque

class Solution:
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []  # (finish_time, weight, index)
        q = deque()
        ans = [0] * len(tasks)

        time = 0
        j = 0
        m = len(tasks)

        while j < m or q:

            # Add all tasks that have arrived
            while j < m and j <= time:
                q.append(j)
                j += 1

            # Release completed servers
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # Assign waiting tasks to available servers
            while free and q:
                task_idx = q.popleft()
                weight, idx = heapq.heappop(free)

                ans[task_idx] = idx

                heapq.heappush(
                    busy,
                    (time + tasks[task_idx], weight, idx)
                )

            # Advance time
            if q and not free:
                time = busy[0][0]
            else:
                time += 1

        return ans
