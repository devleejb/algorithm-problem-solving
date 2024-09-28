def calc_moved_figure_set(figure, row_offset, col_offset):
    figure_set = set()

    for i in range(3):
        for j in range(3):
            if figure[i][j] == 1:
                figure_set.add((i + row_offset, j + col_offset))

    return figure_set


def is_filled_line(width, height, figure_set, field_set):
    for i in range(height):
        filled = True
        for j in range(width):
            if not ((i, j) in figure_set or (i, j) in field_set):
                filled = False
                break
        if filled:
            return True

    return False


def sol(field, figure):
    field_set = set()
    height = len(field)
    width = len(field[1])

    for i in range(height):
        for j in range(width):
            if field[i][j] == 1:
                field_set.add((i, j))

    for col_offset in range(0, width - 2):
        prev_moved_figure_set = None
        for row_offset in range(0, height - 2):
            moved_figure_set = calc_moved_figure_set(figure, row_offset, col_offset)

            if field_set.intersection(moved_figure_set):
                if prev_moved_figure_set and is_filled_line(
                    width, height, field_set, prev_moved_figure_set
                ):
                    return col_offset
                break

            if row_offset == height - 3:
                if is_filled_line(width, height, field_set, moved_figure_set):
                    return col_offset
                break

            prev_moved_figure_set = moved_figure_set

    return -1


print(
    sol(
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
        [[0, 0, 1], [0, 1, 1], [0, 0, 1]],
    )
)

print(
    sol(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
        ],
        [[1, 1, 1], [1, 0, 1], [1, 0, 1]],
    )
)

print(
    sol(
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 0, 1]],
        [[1, 1, 0], [1, 0, 0], [1, 0, 0]],
    )
)
