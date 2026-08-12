from bisect import bisect_right
from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Map each key to a list of (timestamp, value) pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append since timestamps for a key are strictly increasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]  # list of (ts, val), sorted by ts
        # We want the rightmost index where ts <= timestamp.
        # bisect_right on the list of timestamps gives the insertion point to the right,
        # so the candidate is at idx-1 (if idx > 0).
        idx = bisect_right(arr, (timestamp, chr(127)))  # chr(127) to ensure tie-break to the right
        if idx == 0:
            return ""  # all stored timestamps are greater than the query
        return arr[idx - 1][1]
