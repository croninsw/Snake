import random
import curses

screen = curses.initscr()
curses.curs_set(0)
screenheight, screenwidth = screen.getmaxyx()
window = curses.newwin(screenheight, screenwidth, 0, 0)
window.keypad(1)
window.timeout(100)

snake_x = screenwidth/4
snake_y = screenheight/2
snake = [
   [snake_y, snake_x],
   [snake_y, snake_x-1],
   [snake_y, snake_x-2]
]

food = [screenheight/2, screenwidth/2]
window.addch(int(food[0]), int(food[1]), curses.ACS_DIAMOND)

key = curses.KEY_RIGHT
score = 0

while key != 27:
   next_key = window.getch()
   prev_key = key
   if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, 27]:
       key = prev_key
   key = key if next_key == -1 else next_key

   if snake[0][0] in [0, screenheight] or snake[0][1] in [0, screenwidth] or snake[0] in snake[1:]: break
    #    curses.endwin()

    #    quit()         no longer needed if the escape key is how the user exits the game



   new_head = [snake[0][0], snake[0][1]]

   if key == curses.KEY_DOWN:
       new_head[0] += 1
   if key == curses.KEY_UP:
       new_head[0] -= 1
   if key == curses.KEY_LEFT:
       new_head[1] -= 1
   if key == curses.KEY_RIGHT:
       new_head[1] += 1

   snake.insert(0, new_head)

   if snake[0] == food:
       food = None
       score += 1
       while food is None:
           newfood = [
               random.randint(1, screenheight-1),
               random.randint(1, screenwidth-1)
           ]
           food = newfood if newfood not in snake else None
       window.addch(food[0], food[1], curses.ACS_DIAMOND)
   else:
       tail = snake.pop()
       window.addch(int(tail[0]), int(tail[1]), ' ')

   window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

curses.endwin()
print("\nScore -- " + str(score))

