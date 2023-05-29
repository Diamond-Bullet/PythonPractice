class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        seen = [False] * (n * n)

        depth = 1
        queue = [(0, 0)]
        seen[0] = True
        while queue:
            tmp = []
            for x, y in queue:
                for nx, ny in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                    dx, dy = x + nx, y + ny
                    if dx == n - 1 and dy == n - 1:
                        return depth + 1
                    if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == 0 and not seen[dx * n + dy]:
                        seen[dx * n + dy] = True
                        tmp.append((dx, dy))
            queue = tmp

        return -1

if __name__ == "__main__":
    pass