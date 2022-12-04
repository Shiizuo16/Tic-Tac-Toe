from src.menuText import colors
# screen
length = 600 + 1    # to accomodate center alignment of squares
height = length + 70

# menu
menuLength = length
menuHeight = height - length
menuColor = colors.get('kobe')

# board
boardLength = boardHeight = length
rows = 3
cols = 3
rectSize = length//cols
sqSize = rectSize - 1
squareColor = colors.get('mistyRose')#('blanchedAlmond')

# menu screen
m_screen_color = colors.get('ming')
m_xcor = m_ycor = 0
m_length = m_height = boardLength
