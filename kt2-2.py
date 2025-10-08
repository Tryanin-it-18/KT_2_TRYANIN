import heapq


class Graph:

    def __init__(self, matrix):

        self.matrix = matrix
        self.n = len(matrix)

    def decst(self, start, end):

        # массив расстояний от start до каждой вершины
        dist = [float('inf')] * self.n
        dist[start] = 0

        queue = [(0, start)]

        while queue:
            # извлекаем вершину с минимальным расстоянием
            cur_dist, cur = heapq.heappop(queue)

            # если дошли до конечной вершины
            if cur == end:
                return cur_dist

            # пропускаем устаревшие расстояния
            if cur_dist > dist[cur]:
                continue

            # проверяем всех соседей текущей вершины
            for neighbor in range(self.n):
                weight = self.matrix[cur][neighbor]
                # если есть ребро
                if weight != 0:
                    new_dist = cur_dist + weight
                    # если нашли более короткий путь
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(queue, (new_dist, neighbor))

        # если путь не найден
        return -1

    def get_vertex_count(self):

        return self.n

    def get_edges(self, vertex):

        edges = []
        for neighbor in range(self.n):
            weight = self.matrix[vertex][neighbor]
            if weight != 0:
                edges.append((neighbor, weight))
        return edges


class GraphP:


    def __init__(self):
        self.graph = None

    def read_input(self):

        start = int(input("K: ")) - 1  # начальная вершина
        end = int(input("M: ")) - 1  # конечная вершина
        n = int(input("N: "))  # количество вершин

        # чтение матрицы смежности
        matrix = []
        print(f"Введите матрицу смежности {n}x{n}:")
        for i in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)

        # создаем объект графа
        self.graph = Graph(matrix)
        return start, end

    def find_shortest_path(self, start, end):
        """Поиск кратчайшего пути между вершинами"""
        if self.graph is None:
            raise ValueError("Граф не инициализирован")

        return self.graph.dijkstra(start, end)

    def display_result(self, start, end, result):
        """Вывод результата"""
        if result == -1:
            print(f"Пути из вершины {start + 1} в вершину {end + 1} не существует")
        else:
            print(f"Длина кратчайшего пути из {start + 1} в {end + 1}: {result}")


def main():
    """Основная функция программы"""
    try:
        # создаем обработчик графа
        processor = GraphP()

        # читаем входные данные
        start, end = processor.read_input()

        # ищем кратчайший путь
        result = processor.find_shortest_path(start, end)

        # выводим результат
        processor.display_result(start, end, result)

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


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
