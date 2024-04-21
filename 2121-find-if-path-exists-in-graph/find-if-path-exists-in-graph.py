class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        done=set()
        q=collections.deque()
        adj_list=collections.defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        done.add(source)
        q.append(source)
        while len(q)>0:
            now=q.popleft()
            for v in adj_list[now]:
                if v not in done:
                    done.add(v)
                    q.append(v)
        return destination in done
