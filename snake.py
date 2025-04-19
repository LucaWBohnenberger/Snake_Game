import curses
import random
import time


def game_loop(window, difficulty=None):
    if difficulty is None:
        difficulty = intro_animation(window)

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
    

def finish_game(score, window):
    height, width = window.getmaxyx()

    # Animação: preenchendo a tela linha por linha com #
    for i in range(height):
        window.addstr(i, 0, "#" * (width - 1))  # -1 para não estourar
        window.refresh()
        time.sleep(0.02)

    # Mensagem de Game Over
    s = f" GAME OVER! Score: {score} "
    y = height // 2
    x = (width - len(s)) // 2

    window.attron(curses.A_BOLD)
    window.attron(curses.A_REVERSE)
    window.addstr(y, x, s)
    window.attroff(curses.A_REVERSE)
    window.attroff(curses.A_BOLD)

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

def intro_animation(window):
    window.clear()
    curses.curs_set(0)
    height, width = window.getmaxyx()
    window.nodelay(True)

        # Phase 1: Snake ASCII animations
    snake_frames = [
        "oOoOoO~",
        "~oOoOoO",
        "OoOoOo>",
        "<OoOoOo"
    ]
    
    for _ in range(8):
        y = random.randint(2, height - 3)
        direction = random.choice(["left", "right"])
        frame = random.choice(snake_frames)
        length = len(frame)

        if direction == "right":
            for x in range(2, width - length - 2, 2):
                window.addstr(y, x, frame)
                window.refresh()
                time.sleep(0.01)
                window.addstr(y, x, " " * length)
        else:  # left
            for x in reversed(range(2, width - length - 2, 2)):
                window.addstr(y, x, frame)
                window.refresh()
                time.sleep(0.01)
                window.addstr(y, x, " " * length)

    time.sleep(0.5)
    window.clear()


    # Phase 2: Loading bar
    loading_text = "Loading..."
    x_loading = (width - len(loading_text)) // 2
    y_loading = height // 2 - 5
    window.addstr(y_loading, x_loading, loading_text)
    window.refresh()
    time.sleep(0.5)

    for i in range(1, width - 20, 3):
        bar = "[" + "#" * (i // 3) + " " * ((width - 20) // 3 - i // 3) + "]"
        window.addstr(y_loading + 1, (width - len(bar)) // 2, bar)
        window.refresh()
        time.sleep(0.05)

    time.sleep(0.5)
    window.clear()

    # Phase 3: Title with typing effect
    title = ">>> S N A K E   G A M E <<<"
    x_title = (width - len(title)) // 2
    y_title = height // 2 - 5
    for i in range(len(title)):
        window.addstr(y_title, x_title + i, title[i])
        window.refresh()
        time.sleep(0.08)

    # Blinking title effect
    for _ in range(4):
        window.attron(curses.A_BOLD)
        window.addstr(y_title, x_title, title)
        window.attroff(curses.A_BOLD)
        window.refresh()
        time.sleep(0.3)
        window.addstr(y_title, x_title, " " * len(title))
        window.refresh()
        time.sleep(0.2)

    window.addstr(y_title, x_title, title)
    window.refresh()

    # Subtitle in English
    subtitle = "Use ↑ ↓ to select difficulty and press ENTER to start"
    window.attron(curses.A_DIM)
    window.addstr(y_title + 2, (width - len(subtitle)) // 2, subtitle)
    window.attroff(curses.A_DIM)

    # Difficulty options
    difficulties = [
        "Very Easy", "Easy", "Moderate", "Normal", "Challenging",
        "Hard", "Very Hard", "Extreme", "Insane", "Impossible"
    ]
    selected = 3

    while True:
        for i, diff in enumerate(difficulties):
            y = height // 2 + i
            x = (width - 24) // 2
            prefix = ">>" if i == selected else "  "
            suffix = "<<" if i == selected else "  "
            display = f"{prefix} {diff.center(18)} {suffix}"
            if i == selected:
                window.attron(curses.A_REVERSE)
                window.addstr(y, x, display)
                window.attroff(curses.A_REVERSE)
            else:
                window.addstr(y, x, display)
        window.refresh()

        key = window.getch()
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(difficulties) - 1:
            selected += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            break
        time.sleep(0.05)

    # Final dramatic pause before game starts
    window.clear()
    final_msg = f"Starting on: {difficulties[selected]} Mode"
    window.addstr(height // 2, (width - len(final_msg)) // 2, final_msg)
    window.refresh()
    time.sleep(2)

    window.clear()
    window.nodelay(True)
    return selected + 1



        
        
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


if __name__ == "__main__":
    def start(window):
        difficulty = intro_animation(window)
        game_loop(window, difficulty)
    curses.wrapper(start)
