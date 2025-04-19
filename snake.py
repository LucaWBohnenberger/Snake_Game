import curses
import random
import time


def game_loop(window, difficulty):
    direction = curses.KEY_RIGHT
    snake = [
        [10, 14],
        [ 9, 14],
        ]
    
    fruit = get_new_fruit(window=window)
    score = 0
    
    while True:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit, window=window, char=curses.ACS_DIAMOND)
        new_direction = get_new_direction(window=window, timeout=difficulty)
        
        
        if not direction_is_oposite(direction, new_direction) and new_direction is not None:
            direction = new_direction
        
        
            
        move_snake(snake,direction, fruit)
        
        if snake_hit_itself(snake):
            break 
            
        if actor_hit_border(actor=snake[0], window=window):
            break
        
        if snake_hit_fruit(snake=snake, fruit=fruit):
            fruit = get_new_fruit(window=window)
            score += 1
    
    finish_game(score=score, window=window)
    

def finish_game(score,window):
    height, width = window.getmaxyx()
    s = f"Game Over! Score {score}"
    y = int(height/2)
    x = int((width - len(s)) /2)      
    window.addstr(y, x, s)     
    window.refresh()    
    time.sleep(3.5)     
        
        
        
def draw_screen(window):
    window.clear()  
    curses.curs_set(0)
    window.border()
    
def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head, window=window, char="O")
    body = snake[1::]
    for i in body:
        draw_actor(actor=i,window=window, char="o")    
    
def draw_actor(actor,window, char):
    window.addch(actor[0], actor[1], char)
    
def get_new_direction(window, timeout=1000):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        return direction
    return None

def move_actor(actor, direction):
    match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_DOWN:
           actor[0] += 1
        case curses.KEY_LEFT:
            actor[1] -= 2
        case curses.KEY_RIGHT:
            actor[1] += 2
            
def move_snake(snake, direction, fruit):
    head = snake[0].copy()
    move_actor(head, direction)
    snake.insert(0, head)
    if not snake_hit_fruit(snake, fruit):
        snake.pop()
        
        
def snake_hit_itself(snake):
    snake2 = snake.copy()
    head = snake[0].copy()
    snake2 = snake2[1::]
    if head in snake2:
        return True
    return False
        
def direction_is_oposite(direction, new_direction):
    match direction:
        case curses.KEY_UP:
            return new_direction == curses.KEY_DOWN
        case curses.KEY_DOWN:
            return new_direction == curses.KEY_UP
        case curses.KEY_LEFT:
            return new_direction == curses.KEY_RIGHT
        case curses.KEY_RIGHT:
            return new_direction == curses.KEY_LEFT

            
def actor_hit_border(actor, window):
    height, width = window.getmaxyx()
    return (actor[0] <= 0 or actor[0] >= height-1  or actor[1] <= 0 or actor[1] >= width-1)
        
    
def get_new_fruit(window):
    height, width = window.getmaxyx()
    
    w = random.randint(2, width-3)
    
    if (w%2) == 1:
        w += 1
    
    return [random.randint(1, height-2), w]
    
def snake_hit_fruit(snake, fruit):
    return fruit in snake

def select_difficulty():
    conv = {
        1: 1000,
        2: 900,
        3: 700,
        4: 600,
        5: 400,
        6: 300,
        7: 200,
        8: 100,
        9: 150,
        10: 80,
        11: 1,
    }
    
    try:
        diff = int(input("Select your difficulty (1 to 10): "))
    except ValueError:  
        print("Invalid input. Defaulting to 1.")
        diff = 1
    return conv.get(diff, 1000)
    

if __name__ == "__main__":
    curses.wrapper(game_loop, difficulty=select_difficulty())