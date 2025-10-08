from collections import Counter


class Node: #узлы дерева
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.codes = {}
        self.root = None
        self._build_tree()

    def _build_tree(self):
        if not self.text:
            return

        # количество символов в нашем тексте
        col_sim = Counter(self.text)
        nodes = []

        # создаем листья (нужны для каждого символа)
        for char, freq in col_sim.items():
            nodes.append(Node(char, freq))

        # строим дерево хафф.
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            left = nodes.pop(0)
            right = nodes.pop(0)
            # создадим род. узел
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            nodes.append(merged)

        self.root = nodes[0] if nodes else None
        self._generate_codes(self.root, "")

    def _generate_codes(self, node, current_code):
        if node is None:
            return
        # если это листочек, то сохраняем код
        if node.char is not None:
            self.codes[node.char] = current_code
            return
        # рекурсивно обходим детей
        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def _get_tree_height(self, node):
        # вычисляем высоту дерева
        if node is None:
            return 0
        return 1 + max(self._get_tree_height(node.left), self._get_tree_height(node.right))

    def _print_tree(self, node, level=0, pos=0, tree_lines=None, width=80):
        if tree_lines is None:
            height = self._get_tree_height(node)
            # создаем массив для отрисовки дерева
            tree_lines = [[" " for _ in range(width)] for _ in range(height * 2 - 1)]

        if node is None:
            return tree_lines

        # отображаем узел
        if node.char is not None:
            char_display = f"'{node.char}'" if node.char != ' ' else "[ ]"
            label = char_display
        else:
            label = str(node.freq)

        # записываем метку узла
        start = pos - len(label) // 2
        for i, char in enumerate(label):
            if 0 <= start + i < width:
                tree_lines[level * 2][start + i] = char

        # рисуем связи к детям
        if node.left or node.right:
            left_pos = pos - width // (2 ** (level + 2))
            right_pos = pos + width // (2 ** (level + 2))

            # горизонтальные линии
            if node.left:
                for i in range(left_pos + 1, pos):
                    if 0 <= i < width:
                        tree_lines[level * 2 + 1][i] = '─'
                tree_lines[level * 2 + 1][left_pos] = '┌'

            if node.right:
                for i in range(pos + 1, right_pos):
                    if 0 <= i < width:
                        tree_lines[level * 2 + 1][i] = '─'
                tree_lines[level * 2 + 1][right_pos] = '┐'

            # вертикальная линия от родителя
            if node.left and node.right:
                tree_lines[level * 2 + 1][pos] = '┴'
            elif node.left:
                tree_lines[level * 2 + 1][pos] = '└'
            else:
                tree_lines[level * 2 + 1][pos] = '┘'

            # рекурсивно обрабатываем детей
            if node.left:
                self._print_tree(node.left, level + 1, left_pos, tree_lines, width)
            if node.right:
                self._print_tree(node.right, level + 1, right_pos, tree_lines, width)

        return tree_lines

    def print_tree(self):
        if self.root is None:
            print("дерево пустое")
            return
        # выводим дерево
        tree_lines = self._print_tree(self.root, pos=40, width=80)
        for line in tree_lines:
            print(''.join(line).rstrip())

    def print_codes(self):
        print("коды:")
        for char, code in sorted(self.codes.items()):
            if char == ' ':
                print(f"  [пробел]: {code}")
            else:
                print(f"  '{char}': {code}")

    def calculate_bits(self):
        # считаем общее количество бит
        total = 0
        for char in self.text:
            total += len(self.codes[char])
        return total


def main():
    # ввод данных
    alphabet = input("алфавит: ")
    text = input("текст: ")

    # проверки
    if not alphabet or not text:
        print("ошибка: пустой ввод")
        return

    for char in text:
        if char not in alphabet:
            print(f"ошибка: символ '{char}' не в алфавите")
            return

    # создаем дерево и выводим результаты
    huffman = HuffmanTree(text)
    huffman.print_codes()
    print("\nдерево:")
    huffman.print_tree()
    bits = huffman.calculate_bits()
    print(f"\nбит для кодирования: {bits}")

if __name__ == "__main__":
    main()

"""
Тест 1: 
Алфавит: "абв"
Текст: "абабв"
Ожидается:
  Дерево с узлами для 'а', 'б', 'в'
  Коды для каждого символа
  Общее количество бит > 0

=== Тест 2: 
Алфавит: "а"
Текст: "аааа"
Ожидается:
  Дерево из одного узла
  Код: 'а': "0" (или "1")
  Биты: 4

Тест 3: 
Алфавит: "абв"
Текст: ""
Ожидается: ошибка "текст не может быть пустым"

Тест 4: 
Алфавит: ""
Текст: "абв"
Ожидается: ошибка "алфавит не может быть пустым"
"""