import heapq


def dijkstra(g, start, end):
    n = len(g)
    dist = [float('inf')] * n  # расстояния до вершин
    dist[start] = 0  # до старта 0

    # очередь: (расстояние, вершина)
    queue = [(0, start)]

    while queue:
        cur_dist, cur = heapq.heappop(queue)

        # если дошли до конца
        if cur == end:
            return cur_dist

        # если расстояние устарело
        if cur_dist > dist[cur]:
            continue

        # смотрим соседей
        for i in range(n):
            w = g[cur][i]  # вес ребра
            if w != 0:  # если есть ребро
                new_dist = cur_dist + w

                # если нашли короче
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    heapq.heappush(queue, (new_dist, i))

    return dist[end] if dist[end] != float('inf') else -1


def main():
    # ввод данных
    start = int(input("K: ")) - 1  # начало
    end = int(input("M: ")) - 1    # конец
    n = int(input("N: "))          # вершин

    # читаем матрицу
    g = []
    for i in range(n):
        row = list(map(int, input().split()))
        g.append(row)

    # ищем путь
    result = dijkstra(g, start, end)

    # выводим результат
    print(result)


if __name__ == "__main__":
    main()


"""
Тест1: 
1
3
4
0 2 0 1
2 0 3 0
0 3 0 1
1 0 1 0
Вывод: 2

тест2: 
1
4
4
0 2 0 0
0 0 3 0
0 0 0 0
0 0 0 0

Вывод: -1
Нет пути из вершины 1 в вершину 4

ТЕСТ 3:

1
4
4
0 1 0 0
0 0 2 0
0 0 0 3
0 0 0 0

Вывод: 6
"""