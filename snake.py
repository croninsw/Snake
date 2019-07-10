import random
import curses

#                               SNAKE
#            /^\/^\
#          _|__|  O|
# \/     /~     \_/ \
#  \____|__________/  \
#         \_______      \
#                 `\     \                 \
#                   |     |                  \
#                  /      /                    \
#                 /     /                       \\
#               /      /                         \ \
#              /     /                            \  \
#            /     /             _----_            \   \
#           /     /           _-~      ~-_         |   |
#          |      \        _-~    _--_    ~-_     _/   |
#           \      ~-____-~    _-~    ~-_    ~-_-~    /
#             ~-_           _-~          ~-_       _-~
#                ~--______-~                ~-___-~
# Adapted from tutorial by Engineer Man, written for fun by github.com/croninsw


screen = curses.initscr()
curses.curs_set(0)
screenheight, screenwidth = screen.getmaxyx()
window = curses.newwin(screenheight, screenwidth, 0, 0)
window.keypad(1)
window.timeout(100)

# How big is the snake and where is it located when the game starts
snake_x = screenwidth/4
snake_y = screenheight/2
snake = [
   [snake_y, snake_x],
   [snake_y, snake_x-1],
   [snake_y, snake_x-2]
]

# Define the size, location, and image of the food
food = [screenheight/2, screenwidth/2]
window.addch(int(food[0]), int(food[1]), curses.ACS_DIAMOND)

# This is the direction the snake begins moving in
key = curses.KEY_RIGHT
# And this is the current score of the game
score = 0

while key != 27:
   next_key = window.getch()
   prev_key = key
   if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, 27]:
       key = prev_key
   key = key if next_key == -1 else next_key

   if snake[0][0] in [0, screenheight] or snake[0][1] in [0, screenwidth] or snake[0] in snake[1:]: break

# New_head is a little tricky, but essentially: every time the snake changes direction
# a "new head" is created in the direction the user inputs
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

# If the snake eats the food, increment the score by one and randomly generate new food location
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

# Add new food to the window
   window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

# When the game is ended or the escape key is pressed
# Close the window and print the score to console
curses.endwin()
print("\nScore -- " + str(score))
