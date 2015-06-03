#!/usr/bin/env python
def get_sudoku():
	maxAttempts = 100 #stops the program after 100 attempts
	count = 9999
	solCount = 0

	while count > maxAttempts:
	    solCount +=1
	    # init array
	    puzzle = []
	    for i in range(9):
	        row = []
	        for j in range(9):
	            row.append(0)
	            #print row
	        puzzle.append(row)
	
	    ##for r in puzzle:
	    ##    print r
	
	    # get random value
	    for row in range(9):
	        for col in range(9):
	            thisRow=puzzle[row]
	            thisCol=[]
	            for h in range(9):
	                thisCol.append(puzzle[h][col])
	
	            subCol = int(col/3)
	            subRow = int(row/3)
	            subMat = []
	            for subR in range (3):
	                for subC in range (3):
	                    subMat.append(puzzle[subRow*3 + subR][subCol*3 + subC])
	            randVal = 0
	            count = 0
	            while randVal in thisRow or randVal in thisCol or randVal in subMat:
	                randVal = random.randint(1,9)
	                count+=1
	
	                if count > maxAttempts: break 
	            puzzle[row][col] = randVal
	
	            if count > maxAttempts: break 
	        if count > maxAttempts:
	            break
	
	
		
	
	grid = []
	for r in puzzle:
		for s in r:
			grid.append(s)
	solution = grid[:]
	for i in xrange(81):
		if random.random() < 0.66:
			grid[i]=0
	given = [False]*81
	for i in xrange(81):
		if grid[i]:
			given[i] = True
		else:
			given[i] = False
	return grid, given, solution
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
            	if not i == pos: return False
    for i in column[current_col]:
        if (grid[i] == n):
            if not i == pos: return False
    for i in box[current_box]:
        if (grid[i] == n):
            if not i == pos: return False
    return True

def checkall():
	if grid.count(0):
		return 'incomplete'
	for i in xrange(81):
		if not valid(grid[i],i):
			return 'invalid'
	return 'correct'

def gotonext():
	global now_selected
	while True:
			now_selected = (now_selected+1) % 81
			if not given[now_selected]: break

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


grid = [0]*81
given = [False]*81
box = []
row = []
column = []
initiate()
diff = 0.0
import pygame, random
grid,given, solution = get_sudoku()
pygame.init()
pygame.mixer.init()
sound = [pygame.mixer.Sound('wrong.wav'),pygame.mixer.Sound('correct.wav'),pygame.mixer.Sound('incomplete.wav')]
size = 600, 732
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sudoku')
template = pygame.image.load("Sudoku2.jpg")
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
		if now_selected > 80 and now_selected < 84:
			if checkall() == 'incomplete': 
				sound[2].play()
			elif checkall() == 'correct':
				sound[1].play()
			else:
				sound[0].play()
		elif now_selected > 83 and now_selected < 87:
			for i in xrange(81):
				if not given[i]: grid[i] = 0
		elif now_selected > 86 and now_selected < 90:
			grid,given, solution = get_sudoku()
		elif now_selected > 89 and now_selected < 94:
			grid[last_selected] = solution[last_selected]
		elif now_selected > 94 and now_selected < 99:
			grid = solution[:]
		if (now_selected > 80 or given[now_selected]):
			gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_KP1) and not(given[now_selected]):
            grid[now_selected] = 1;gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_2 or event.key == pygame.K_KP2) and not(given[now_selected]):
            grid[now_selected] = 2;gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_3 or event.key == pygame.K_KP3) and not(given[now_selected]):            
            grid[now_selected] = 3;gotonext()            
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_4 or event.key == pygame.K_KP4)  and not(given[now_selected]):
            grid[now_selected] = 4;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_5 or event.key == pygame.K_KP5) and not(given[now_selected]):
            grid[now_selected] = 5;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_6 or event.key == pygame.K_KP6) and not(given[now_selected]):
            grid[now_selected] = 6;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_7 or event.key == pygame.K_KP7) and not(given[now_selected]):           
            grid[now_selected] = 7;gotonext()         
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_8 or event.key == pygame.K_KP8) and not(given[now_selected]):
            grid[now_selected] = 8;gotonext()           
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_9 or event.key == pygame.K_KP9) and not(given[now_selected]):
            grid[now_selected] = 9;gotonext()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_0 or event.key == pygame.K_BACKSPACE) and not(given[now_selected]):
            grid[now_selected] = 0
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
		while True:
			now_selected = (now_selected-9) % 81
			if not given[now_selected]: break
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
		while True:
			now_selected = (now_selected+9) % 81
			if not given[now_selected]: break
	elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_TAB):
		while True:
			now_selected = (now_selected+1) % 81
			if not given[now_selected]: break
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
		while True:
			now_selected = (now_selected-1) % 81
			if not given[now_selected]: break
        #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            #print checkall()
	#elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
		#solve()
	elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
		running = False
    try:
        pygame.display.update()
    except:
        pass
pygame.quit()
