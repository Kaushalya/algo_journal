from typing import List, Set, Dict
from collections import defaultdict
import heapq

def avoidFlood(rains: List[int]) -> List[int]:
    flood:Dict[int, int] = dict()
    lake_days = []
    ans = [-1]*len(rains)

    lakes: Set[int] = set()
    for i, lake in enumerate(rains):
        if lake > 0:
            if lake in lakes:
                lake_days.append((i, lake))
            else:
                lakes.add(lake)
    heapq.heapify(lake_days)
    for i, lake in enumerate(rains):
        if lake > 0:
            if lake not in flood:
                flood[lake] = 1
            else:
                flood[lake] += 1

                if flood[lake] > 1:
                    return []
        else:
            if len(lake_days)==0:
                ans[i] = 1
            else:
                temp = []
                next_flood = heapq.heappop(lake_days)
                while (next_flood[1] not in flood) or (flood[next_flood[1]]==0):
                    temp.append(next_flood)
                    if len(lake_days)==0:
                        break
                    next_flood = heapq.heappop(lake_days)
                ans[i] = next_flood[1]
                if len(temp) > 0:
                    lake_days.extend(temp)
                    heapq.heapify(lake_days)

            flood[ans[i]] = 0

        if len(lake_days)>0:
            return []

    return ans

if __name__ == "__main__":
    rains = [1,2,0,0,2,1]
    rains2 = [1,2,0,1,2]
    rains3 = [0,0,0,28663,0,0,0,0,0,0,0,0,95827,0,0,85637,0,0,0,45506,95827,85637,0,0,45506,0,0,0,28663,0,0,0,0,60812,0,0,0,0,60812,0,0,0,0,0,0,0,0]
    print(avoidFlood(rains2))
