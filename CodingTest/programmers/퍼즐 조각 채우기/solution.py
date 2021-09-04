from collections import deque

def get_blanks(n, game_board):
    blanks = []
    for y in range(n):
        for x in range(n):
            if game_board[y][x] == 0:
                blank = []
                queue = deque([(y, x)])
                game_board[y][x] = 1
                while queue:
                    now_y, now_x = queue.pop()
                    blank.append((now_y, now_x))
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if now_x+dx < 0 or now_x+dx >= n or now_y+dy < 0 or now_y+dy >= n:
                            continue
                        elif game_board[now_y+dy][now_x+dx] == 0:
                            queue.append((now_y+dy, now_x+dx))
                            game_board[now_y+dy][now_x+dx] = 1
                blank.sort(key=lambda p:(p[0], p[1]))
                blank = list(map(lambda p:(p[0]-y, p[1]-x), blank))
                blanks.append(blank)
    return blanks

def get_blocks(n, table):
    blocks = []
    for y in range(n):
        for x in range(n):
            if table[y][x] == 1:
                block = []
                queue = deque([(y, x)])
                table[y][x] = 0
                while queue:
                    now_y, now_x = queue.pop()
                    block.append((now_y, now_x))
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if now_x+dx < 0 or now_x+dx >= n or now_y+dy < 0 or now_y+dy >= n:
                            continue
                        elif table[now_y+dy][now_x+dx] == 1:
                            queue.append((now_y+dy, now_x+dx))
                            table[now_y+dy][now_x+dx] = 0
                block.sort(key=lambda p:(p[0], p[1]))
                block = list(map(lambda p:(p[0]-y, p[1]-x), block))
                blocks.append(block)
    return blocks

def solution(game_board, table):
    n = len(game_board)
    blanks = get_blanks(n, game_board)
    blocks = get_blocks(n, table)

    answer = 0
    for block in blocks:
        rotated_blocks = [block]
        for i in range(3):
            if i == 0:
                f = lambda p:(p[1], -1*p[0])
            elif i == 1:
                f = lambda p:(-1*p[0], -1*p[1])
            else:
                f = lambda p:(-1*p[1], p[0])
                
            new_block = sorted(map(f, block), key=lambda p:(p[0], p[1]))
            new_block = list(map(lambda p:(p[0]-new_block[0][0], p[1]-new_block[0][1]), new_block))
            rotated_blocks.append(new_block)

        block_num = len(block)
        for blank in blanks:
            blank_num = len(blank)
            if block_num != blank_num:
                continue
            elif blank in rotated_blocks:
                answer += blank_num
                blanks.remove(blank)
                break
    return answer