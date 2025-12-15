def draw_tree(height: int):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    print(' ' * (height - 1) + '|')

if __name__ == "__main__":
    try:
        h = int(input("Add meg a fa magasságát: "))
        draw_tree(h)
    except ValueError:
        print("Kérlek egész számot adj meg!")