from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        target = n * n

        def get_coordinates(square):
            idx = square - 1
            r_from_bottom = idx // n
            r = n - 1 - r_from_bottom
            c = idx % n if r_from_bottom % 2 == 0 else n - 1 - (idx % n)
            return r, c

        queue = deque([(1, 0)])
        visited = set([1])

        while queue:
            curr, rolls = queue.popleft()

            for next_sq in range(curr + 1, min(curr + 6, target) + 1):
                r, c = get_coordinates(next_sq)
                destination = board[r][c] if board[r][c] != -1 else next_sq

                if destination == target:
                    return rolls + 1

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, rolls + 1))

        return -1
