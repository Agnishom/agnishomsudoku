#!/usr/bin/env python
def initiate():
    box.append([0, 1, 2, 9, 10, 11, 18, 19, 20])
    box.append([3, 4, 5, 12, 13, 14, 21, 22, 23])
    box.append([6, 7, 8, 15, 16, 17, 24, 25, 26])
    box.append([27, 28, 29, 36, 37, 38, 45, 46, 47])
    box.append([30, 31, 32, 39, 40, 41, 48, 49, 50])
    box.append([33, 34, 35, 42, 43, 44, 51, 52, 53])
    box.append([54, 55, 56, 63, 64, 65, 72, 73, 74])
    box.append([57, 58, 59, 66, 67, 68, 75, 76, 77])
    box.append([60, 61, 62, 69, 70, 71, 78, 79, 80])
    for i in range(0, 81, 9):
        row.append(range(i, i+9))
    for i in range(9):
        column.append(range(i, 80+i, 9))

def valid(n, pos):
    current_row = pos/9
    current_col = pos%9
    current_box = (current_row/3)*3 + (current_col/3)
    for i in row[current_row]:
        if (grid[i] == n):
            return False
    for i in column[current_col]:
        if (grid[i] == n):
            return False
    for i in box[current_box]:
        if (grid[i] == n):
            return False
    return True

def solve():
    i = 0
    proceed = 1
    diff = 0.0
    while(i < 81):
        if given[i]:
            if proceed:
                    i += 1
            else:
                i -= 1
        else:
            n = grid[i]
            prev = grid[i]
            while(n < 9):
              if (n < 9):
                  n += 1
              if valid(n, i):
                  grid[i] = n
                  proceed = 1
                  break
            if (grid[i] == prev):
               grid[i] = 0
               proceed = 0
            if proceed:
               i += 1
            else:
               i -=1
               diff = diff + 1.0
    return diff
def gotonext():
	global now_selected
	now_selected = (now_selected+1) % 81
def checkall():
	for i in xrange(81):
		if not valid(grid[i],i):
			return False
	return True

grid = [0]*81
given = [False]*81
box = []
row = []
column = []
initiate()
diff = 0.0
import pygame
import sys
pygame.init()
size = 600, 732
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sudoku Solver')
template = pygame.image.load("SUDOKU.jpg")
rect = template.get_rect()
font = pygame.font.Font('Font.ttf', 48)
now_selected = 0
running = True
while running:
    screen.blit(template, rect)
    for i in range(81):
        if grid[i]:
		if given[i]:
			color = (0,0,255)
		else:
			color = (0,0,0)
		text = font.render(str(grid[i]), 1, color)
	        ro = i/9
        	col = i%9
        	textpos = text.get_rect(centerx = col*66 + 33, centery = ro*66 + 33)
        	screen.blit(text, textpos)
    try:
		screen.blit(font.render('_', 1, (150,150,150)), font.render('O', 1, (100,100,100)).get_rect(centerx = (now_selected%9)*66 + 33, centery = (now_selected/9)*66 + 33))
    except:
		pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
		x,y = pygame.mouse.get_pos()
		col_edit = x/66
		ro_edit = y/66
		last_selected = now_selected
		now_selected = ro_edit*9 + col_edit
		if (now_selected > 80):
			gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_KP1) :
            if valid(1,now_selected): grid[now_selected] = 1;given[now_selected]=True;gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_2 or event.key == pygame.K_KP2) :
            if valid(2,now_selected): grid[now_selected] = 2;given[now_selected]=True;gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_3 or event.key == pygame.K_KP3) :            
            if valid(3,now_selected): grid[now_selected] = 3;given[now_selected]=True;gotonext()            
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_4 or event.key == pygame.K_KP4)  :
            if valid(4,now_selected): grid[now_selected] = 4;given[now_selected]=True;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_5 or event.key == pygame.K_KP5) :
            if valid(5,now_selected): grid[now_selected] = 5;given[now_selected]=True;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_6 or event.key == pygame.K_KP6) :
            if valid(6,now_selected): grid[now_selected] = 6;given[now_selected]=True;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_7 or event.key == pygame.K_KP7) :           
            if valid(7,now_selected): grid[now_selected] = 7;given[now_selected]=True;gotonext()         
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_8 or event.key == pygame.K_KP8) :
            if valid(8,now_selected): grid[now_selected] = 8;given[now_selected]=True;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_9 or event.key == pygame.K_KP9) :
            if valid(9,now_selected): grid[now_selected] = 9;given[now_selected]=True;gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_0 or event.key == pygame.K_BACKSPACE) :
            grid[now_selected] = 0;given[now_selected]=False;
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
		now_selected = (now_selected-9) % 81
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
		now_selected = (now_selected+9) % 81
	elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_TAB):
		now_selected = (now_selected+1) % 81
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
		now_selected = (now_selected-1) % 81
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
		for i in xrange(81):
			if not given[i]:
				grid[i]=0
		solve()
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
		grid = [0]*81
		given = [False]*81
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
		running = False
    try:
        pygame.display.update()
    except:
        pass
pygame.quit()
