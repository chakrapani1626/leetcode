"""2402. Meeting Rooms III
Solved
Hard
Topics
Companies
Hint
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b."""


import heapq
class Solution:
    def heappeak(self, heap):
        smallest = heapq.heappop(heap)
        heapq.heappush(heap, smallest)
        return smallest[0]

    def mostBooked(self, n: int, meetings) -> int:
        meetings.sort()
        heap = []
        free_room = []
        room = [0] * n
        for i in range(n):
            heapq.heappush(free_room, (0, n - i - 1))

        for i in range(len(meetings)):
            while heap:
                temp = self.heappeak(heap)
                if temp <= meetings[i][0]:
                    x = heapq.heappop(heap)
                    heapq.heappush(free_room, (0, x[-1]))
                else:
                    break
            if free_room:
                x = heapq.heappop(free_room)
            else:
                x = heapq.heappop(heap)
            if x[0] > meetings[i][0]:
                c = x[0] - meetings[i][0]
            else:
                c = 0
            room[x[-1]] += 1
            heapq.heappush(heap, (c + meetings[i][1], x[-1]))

        return room.index(max(room))


if __name__ == '__main__':
    obj = Solution()
    # obj.mostBooked(2,[[0,10],[1,5],[2,7],[3,4]])
    # obj.mostBooked(3,[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]])
    obj.mostBooked(4, [[18,19],[3,12],[17,19],[2,13],[7,10]])
