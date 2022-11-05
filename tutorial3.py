#Boundary Fill Algorithm
import streamlit as st

def is_valid(screen, m, n, x, y, border_colour, fill_colour):
  if(x<0 or x>=m or y<0 or y>= n or screen[x][y]!= fill_colour or screen [x][y] != border_colour):
    return False
  return True

def boundary_fill(screen, m, n, x, y, border_colour, fill_colour):
  queue = []
  queue.append([x, y])
  screen[x][y] = fill_colour

  while queue:

    current_pixel = queue.pop()
    x_position = current_pixel[0]
    y_position = current_pixel[1]

    if(is_valid(screen, m, n, x_position+1, y_position, border_colour, fill_colour)):
      screen[x_position+1][y_position] = fill_colour
      queue.append([x_position, y_position])

    if(is_valid(screen, m, n, x_position-1, y_position, border_colour, fill_colour)):
      screen[x_position-1][y_position] = fill_colour
      queue.append([x_position-1, y_position])

    if(is_valid(screen, m, n, x_position, y_position+1, border_colour, fill_colour)):
      screen[x_position][y_position+1] = fill_colour
      queue.append([x_position, y_position+1]) 

    if(is_valid(screen, m, n, x_position, y_position-1, border_colour, fill_colour)):
      screen[x_position][y_position+1] = fill_colour
      queue.append([x_position, y_position-1])
    

def main():
  
  st.header("Boundary Fill Algorithm")
  
  screen =[
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 1, 0, 1, 1],
  [1, 2, 2, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 2, 2, 0],
  [1, 1, 1, 1, 1, 2, 1, 1],
  [1, 1, 1, 1, 1, 2, 2, 1],
    ]

  m = len(screen)
  n = len(screen[0])

  x = 4
  y = 4

  border_colour = screen[x][y]
  fill_colour = 3

  boundary_fill(screen, m, n, x, y, border_colour, fill_colour)

  for i in range(m):
    for j in range(n):
      st.write(screen[i][j], end =' ')
    st.write()

main()


