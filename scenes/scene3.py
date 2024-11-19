from manim import ArcBetweenPoints, MoveAlongPath, PI
import numpy as np
from constants import *
from intial import Intial

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.entry_b_values = MATRIX_B_NUMBERS.copy()
        
    def moveBValues(self, matrix):
        move_animations = []
        
        for row in range(MATRIX_ROW_COL_CT):
            if row == 0:
                for col in range(1, MATRIX_ROW_COL_CT):
                    intial_entry = col
                    final_entry = col * MATRIX_ROW_COL_CT
                    
                    arcpath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcpath))
                    
                    self.entry_b_values[intial_entry], self.entry_b_values[final_entry] = self.entry_b_values[final_entry], self.entry_b_values[intial_entry]
                    
            elif row == MATRIX_ROW_COL_CT - 1:
                for col in range(MATRIX_ROW_COL_CT - 1):
                    intial_entry = col + MATRIX_ROW_COL_CT * row
                    if col == 0:
                        final_entry = int(intial_entry / MATRIX_ROW_COL_CT)
                        self.entry_b_values[intial_entry], self.entry_b_values[final_entry] = self.entry_b_values[final_entry], self.entry_b_values[intial_entry]
                    else:
                        final_entry = intial_entry - (row * (MATRIX_ROW_COL_CT - (col + 1)))

                    arcpath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcpath))
                    
                    self.entry_b_values[intial_entry], self.entry_b_values[final_entry] = self.entry_b_values[final_entry], self.entry_b_values[intial_entry]
            
            else:
                for col in range(MATRIX_ROW_COL_CT):
                    intial_entry = col + MATRIX_ROW_COL_CT * row
                    final_entry = 0
                    
                    if col == 0:
                        final_entry = int(intial_entry / MATRIX_ROW_COL_CT)
                        
                    elif col == MATRIX_ROW_COL_CT - 1:
                        final_entry = intial_entry + (col * (MATRIX_ROW_COL_CT - (row + 1)))
                    
                    if final_entry != 0:
                        arcpath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
                        move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcpath))
                    
        return move_animations
            