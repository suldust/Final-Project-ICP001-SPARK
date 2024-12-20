import pygame 
import time
import random
pygame.init()
# Kích thước màn hình
window_width = 600
window_height = 400
# Màu
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# Tốc độ rắn
snake_block = 10
snake_speed = 15
# Tạo màn hình
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')
# Đồng hồ
clock = pygame.time.Clock()
# Font chữ
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
# Điểm số
def your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    window.blit(value, [0, 0])
# Vẽ rắn
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])
# Hiển thị thông báo
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])
# Kết thúc game
def game_loop():
    game_over = False
    game_close = False
    # Tọa độ bắt đầu của rắn
    x1 = window_width / 2
    y1 = window_height / 2
    # Tọa độ di chuyển của rắn
    x1_change = 0
    y1_change = 0
    # Danh sách lưu thân rắn
    snake_list = []
    length_of_snake = 1
    # Vị trí quả táo
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close:
            window.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        # Điều khiển rắn
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # Kiểm tra rắn đi ra khỏi màn hình
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        # Vẽ quả táo
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
        # Thêm thân rắn
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # Kiểm tra rắn cắn thân
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        # Vẽ rắn
        draw_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()
        # Kiểm tra rắn ăn táo
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
# Chạy game
game_loop()
