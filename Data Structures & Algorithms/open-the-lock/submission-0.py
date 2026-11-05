class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        q = deque([("0000", 0)])
        down = lambda x: str((int(x) - 1) % 10)
        up = lambda x: str((int(x) + 1) % 10)
        while len(q) > 0:
            combo, turns = q.popleft()
            if combo == target:
                return turns
            neighbors = [
                down(combo[0]) + combo[1:],
                up(combo[0]) + combo[1:],
                combo[:1] + down(combo[1]) + combo[2:],
                combo[:1] + up(combo[1]) + combo[2:],
                combo[:2] + down(combo[2]) + combo[3:],
                combo[:2] + up(combo[2]) + combo[3:],
                combo[:3] + down(combo[3]),
                combo[:3] + up(combo[3]),
            ]
            for node in neighbors:
                if node not in visited:
                    visited.add(node)
                    q.append((node, turns + 1))
        return -1


