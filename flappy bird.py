#this code is exactly 100 lines!!!!!!!____________________________________________________________________________________________
import json,pygame,sys,random,time
size = (1000,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.init()
size22 = pygame.font.SysFont('FreeMono,Monospace', 32)
sky,gameover_txt,cactus = pygame.image.load(r"flappy bird\sky.png"),pygame.image.load(r"gameover.png"),pygame.image.load(r"flappy bird\cactus.png")
sky = pygame.transform.scale(sky,(1000,600))
gameover_txt = pygame.transform.scale(gameover_txt,(600,300))
cactus_u = pygame.transform.flip(cactus,False,True)
playagain_txt = size22.render("play again",True,(255,255,255))
jumping,gameover,game_on,running,speed,inc = False,False,True,True,5,False
while game_on:
    g,h,points = 0.5,7,0
    v = h
    cactus_size,bird_pos = (50,600),[30,100]
    bird_pos_r = (bird_pos[0]+50,bird_pos[1]+50)
    x,y = 1000,random.randint(50,400)
    try:
        with open('flappybird_highscore') as highscore1:
            save_data = json.load(highscore1)
        highscore = save_data['highscore']
    except:
        highscore = 0
    while running:
        if v <= 0:
            bird = pygame.image.load(r"flappy bird\bird_fly.png")
        else:
            bird = pygame.image.load(r"flappy bird\bird.png")  
        bird = pygame.transform.scale(bird,(50,50))
        points_txt,high_txt = size22.render('points:'+str(points),True,(255,255,255)),size22.render('highscore:'+str(highscore),True,(0,0,0))
        cactus_location = (x,600-y)
        cactus = pygame.transform.scale(cactus,(100,y))
        cactus_u = pygame.transform.scale(cactus_u,(100,400-y))
        screen.blit(sky,(0,0))
        screen.blit(bird,(bird_pos))
        if not jumping:
            bird_pos[1] += v
            v += g
        if x <= -100:
            x,y,points = 1000,random.randint(50,350),points + 1
        screen.blit(points_txt,(480,10))
        screen.blit(high_txt,(20,20))
        screen.blit(cactus,(x,600-y))
        screen.blit(cactus_u,(x,0))
        if points%5 == 0 and points != 0 and inc == False:
            speed += 1
            inc = True
        if inc == True and points%5 != 0:
            inc = False 
        x -= speed
        pygame.display.update()
        clock.tick(60)    
        for  e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            jumping = True
            v=h
        if jumping:
            bird_pos[1] -= v
            v -= g
            screen.blit(points_txt,(480,10))
            screen.blit(high_txt,(20,20))
            pygame.display.update()          
            if v <= -h:
                jumping,v = False,h
            pygame.display.update()
        if (bird_pos[1] >= 600 or bird_pos[1] < 0) or (bird_pos[0] in range(x,x+100) and bird_pos[1] in range(600-y,600)) or ((bird_pos[0]+50) in range(x,x+100) and (bird_pos[1]+50) in range(600-y,600)) or (bird_pos[0] in range(x,x+100) and bird_pos[1] in range(0,400-y)) or ((bird_pos[0]+50) in range(x,x+100) and (bird_pos[1]+50) in range(0,400-y)): 
            running,gameover = False,True            
            time.sleep(1)
            break
        if points >= highscore:
            highscore = points
            save_data = {'highscore':points}
            with open('flappybird_highscore','w') as highscore1:
                json.dump(save_data,highscore1)
        pygame.display.update()
    while gameover:
        mouse = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        screen.blit(gameover_txt,(170,100))
        screen.blit(playagain_txt,(400,400))
        pygame.draw.rect(screen,(0,255,0),[400,450,80,40])
        pygame.draw.rect(screen,(255,0,0),[500,450,80,40])
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] in range(400,480) and mouse[1] in range(450,490):
                    gameover,points,running,speed = False,0,True,5
                    bird_pos[1] = 0
                if mouse[0] in range(500,580) and mouse[1] in range(450,490):
                    pygame.quit()
                    sys.exit()   