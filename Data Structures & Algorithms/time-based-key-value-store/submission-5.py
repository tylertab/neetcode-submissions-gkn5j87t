class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.mp.get(key, None) is None:
            self.mp[key] = [(timestamp, value)]
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.mp.get(key, None) is None:
            return ""
        entries = self.mp[key]
        l = 0
        r = len(entries) - 1
        out = ""
        while l <= r:
            mid = (l + r) // 2
            prev_timestamp, value = entries[mid]
            if prev_timestamp == timestamp:
                return value
            if prev_timestamp > timestamp:
                r = mid - 1
            else:
                out = value
                l = mid + 1

        return out


