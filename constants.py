from manim import WHITE, YELLOW, BLACK, RED_E, PURPLE_A, BLUE_E, GREEN_E, GREEN_C, PINK, GOLD_A

#Matrix default intialization:
MATRIX_ROW_COL_CT = 3
MATRIX_BG_COLOR = GREEN_E
MATRIX_BORDER_COLOR = GREEN_C
MATRIX_TEXT_OPACITY = 0.9

#Matrix A intialization

MATRIX_A_COLOR = WHITE
#MATRIX_A_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Self set values

#OR

MATRIX_A_NUMBERS = []
for entry in range(1, MATRIX_ROW_COL_CT**2 + 1): #Increment values from 1 to x
    MATRIX_A_NUMBERS.append(entry)

#Matrix B intialization

MATRIX_B_COLOR = GOLD_A
#MATRIX_B_NUMBERS = [9, 8, 7, 6, 5, 4, 3, 2, 1] #Self set values

#OR

MATRIX_B_NUMBERS = []
for entry in range(MATRIX_ROW_COL_CT**2, 0, -1): #Decrement values from x to 1
    MATRIX_B_NUMBERS.append(entry)


#Computed Cij values intialization
C_VALUES_COLOR = BLACK

#DON"T EDIT
MATRIX_BUFFER = MATRIX_ROW_COL_CT / 36
MATRIX_FONT_SIZE = -MATRIX_ROW_COL_CT + 26.4

MATRIX_C_BOX_VGROUP = 0
MATRIX_C_ENTRY_A_VGROUP = 1
MATRIX_C_ENTRY_B_VGROUP = 2
MATRIX_C_ENTRY_TEMP_C_VGROUP = 3
MATRIX_C_ENTRY_COMPUTED_C_VGROUP = 4