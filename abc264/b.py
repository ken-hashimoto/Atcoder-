R,C = map(int,input().split())
R -= 1
C -= 1
G = [
  "###############",
  "#.............#",
  "#.###########.#",
  "#.#.........#.#",
  "#.#.#######.#.#",
  "#.#.#.....#.#.#",
  "#.#.#.###.#.#.#",
  "#.#.#.#.#.#.#.#",
  "#.#.#.###.#.#.#",
  "#.#.#.....#.#.#",
  "#.#.#######.#.#",
  "#.#.........#.#",
  "#.###########.#",
  "#.............#",
  "###############",
]
print("black" if G[R][C] == "#" else "white")