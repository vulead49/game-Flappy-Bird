# 2 cái cần có thư viện pygame

import pygame


pygame.init()


# các biến khởi tạo trong game


# hằng trọng lực
p = 0.01
# tọa độ y của con chim
bird_mid_y = 0
# khởi tạo điểm
score = 0
# game play
game_play = True
hscore = 0

# score
game_font = pygame.font.Font('game1\\04B_19.TTF',40)
game_font2 = pygame.font.Font('game1\\04B_19.TTF',20)
def score_view():
    if game_play:
        score_f = game_font.render(f'{int(score)}',True,(255,255,255))
        score_hcn = score_f.get_rect(center = ( 216,100))
        screen.blit(score_f,score_hcn)
    else:
        # điểm chơi vòng hiện tại
        score_f = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_hcn = score_f.get_rect(center = ( 216,100))
        screen.blit(score_f,score_hcn)
        # điểm cao nhất
        hscore_f = game_font2.render(f'High Score: {int(hscore)}',True,(255,255,255))
        hscore_hcn = hscore_f.get_rect(center = ( 350,25))
        screen.blit(hscore_f,hscore_hcn)
        
        
# tiêu đề và icon
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load(r'game1\\assets\\yellowbird-downflap.png')
# đưa background vào
background = pygame.image.load(r'game1\\assets\\background-night.png')
background = pygame.transform.scale2x(background)
# đưa sàn vào
fl = pygame.image.load(r'game1\assets\floor.png')
fl = pygame.transform.scale2x(fl)
fl_x = 0
pygame.display.set_icon(icon)

# cửa sổ game
screen = pygame.display.set_mode((432,768))
# đưa bird vào
bird_mid = pygame.image.load(r'game1\assets\yellowbird-midflap.png')
bird_mid = pygame.transform.scale2x(bird_mid)
bird_mid_hcn = bird_mid.get_rect(center = (100,386))
# màn hình out game
screen_out = pygame.image.load(r'game1\assets\message.png')
screen_out = pygame.transform.scale2x(screen_out)
screen_out_hcn = screen_out.get_rect(center = (216,386))
# hàm check va chạm
def check_vc():
    if bird_mid_hcn.bottom >= 668 or bird_mid_hcn.top <= -65:
        return False
    else:
        return True
# hàm reset game
def reset_game():
    global bird_mid_y, score, game_play
    bird_mid_y = 0
    bird_mid_hcn.center = (100, 386)
    score = 0
    game_play = True

# vòng lặp xử lí game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_play:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_play:
                    bird_mid_y = -2 
                if event.key == pygame.K_UP and game_play:
                    bird_mid_y = -2 
            if  event.type == pygame.MOUSEBUTTONDOWN:
                bird_mid_y = -2
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_out_hcn.collidepoint(event.pos):  # Kiểm tra sự kiện click vào tấm ảnh
                    reset_game()
        
                
    screen.blit(background,(0,0))
    fl_x -= 1
    screen.blit(fl,(fl_x,600))
    screen.blit(fl,(fl_x + 432,600))
    if fl_x == -432:
        fl_x = 0
    
    if game_play == True: 
        # bird
        screen.blit(bird_mid,bird_mid_hcn)
        bird_mid_y += p
        bird_mid_hcn.centery += bird_mid_y
        score += 0.01
        if score>hscore: hscore = score
        score_view()
        game_play = check_vc()
    else:
        # câu lệnh để vẽ màn hình
        screen.blit(screen_out,screen_out_hcn)
        score_view()
    pygame.display.update()
pygame.quit()
            
            
            