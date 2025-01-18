def main():
    q = int(input())
    snake = [0]
    top_index = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            snake.append(snake[-1] + query[1])
        elif query[0] == 2:
            top_index += 1
        elif query[0] == 3:
            print(snake[top_index + query[1] -1] - snake[top_index])

if __name__ == '__main__':
    main()