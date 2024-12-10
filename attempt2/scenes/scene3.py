from manim import ArcBetweenPoints, MoveAlongPath, Text, MathTex, FadeIn, FadeOut, Transform, PI, ORIGIN, RIGHT
import numpy as np
from constants import *
from intial import Intial

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.temp_computed_c_values = []
        self.text_c_value_list = []
        self.computed_c_values = self.intial.returnComputedCAsArray()
        self.entry_b_values = np.array(MATRIX_B_NUMBERS.copy())
        self.entry_a_values = np.array(MATRIX_A_NUMBERS.copy())
        
    def moveBValuesDiagonally(self, matrix):
        move_animations = []
        
        for row in range(MATRIX_ROW_COL_CT):
            if row == 0:
                for col in range(1, MATRIX_ROW_COL_CT):
                    intial_entry = col
                    final_entry = col * MATRIX_ROW_COL_CT
                    
                    arcpath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
                    move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcpath))
                    matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].align_to(matrix[final_entry][MATRIX_C_ENTRY_B_VGROUP].get_center())
                    
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
                    matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].align_to(matrix[final_entry][MATRIX_C_ENTRY_B_VGROUP].get_center())
                    
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
                        matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].align_to(matrix[final_entry][MATRIX_C_ENTRY_B_VGROUP].get_center())
                        
        return move_animations
    
    def moveBvaluesUp(self, matrix):
        """Move Bij values up/down based on the row

        Args:
            matrix (VGroup): Matrix used in the scene

        Return:
            list: List of animations that move the Bij values up/down
        """
        move_animations = []
        temp_b_values = self.entry_b_values.copy()
        
        for row in range(MATRIX_ROW_COL_CT):
            for col in range(MATRIX_ROW_COL_CT):
                intial_entry = col * MATRIX_ROW_COL_CT + row
                intial_entry_b_list = row * MATRIX_ROW_COL_CT + col
                
                if row == 0:
                    final_point_entry = col * MATRIX_ROW_COL_CT + (MATRIX_ROW_COL_CT - 1)
                    final_point_entry_b_list = (MATRIX_ROW_COL_CT - 1) * MATRIX_ROW_COL_CT + col
                else:
                    final_point_entry = col * MATRIX_ROW_COL_CT + (row - 1)
                    final_point_entry_b_list = (row - 1) * MATRIX_ROW_COL_CT + col
                
                arcPath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
                move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcPath))
                
                self.entry_b_values[final_point_entry_b_list] = temp_b_values[intial_entry_b_list]
                
        return move_animations
    
    def computeTempCValues(self, matrix):
        intial_move_animations = []
        final_move_animations = []
        intial_fade_in_animations = []
        final_fade_in_animations = []
        intial_fade_out_animations = []
        final_fade_out_animations = []
        
        self.temp_computed_c_values = self.entry_a_values * self.entry_b_values
        for row in range(MATRIX_ROW_COL_CT):
            for col in range(MATRIX_ROW_COL_CT):
                entry = col + (MATRIX_ROW_COL_CT * row)

                temp_c_value = Text(str(self.temp_computed_c_values[entry]), color=C_VALUES_COLOR, font_size=MATRIX_FONT_SIZE).move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center())
                self.text_c_value_list.append(temp_c_value)
                
                aij_value = Text(str(self.entry_a_values[entry]), color=MATRIX_A_COLOR, font_size=MATRIX_FONT_SIZE).move_to(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center())
                bij_value = Text(str(self.entry_b_values[entry]), color=MATRIX_B_COLOR, font_size=MATRIX_FONT_SIZE).move_to(matrix[entry][MATRIX_C_ENTRY_A_VGROUP].get_center()).shift(RIGHT * 0.5)
                multi_sign = MathTex('\\times', color=MATRIX_A_COLOR).scale(0.65).move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center())
                
                intial_fade_in_animations.append(FadeIn(multi_sign))
                
                intial_move_animations.append(aij_value.animate.move_to(multi_sign.get_center()))
                intial_move_animations.append(bij_value.animate.move_to(multi_sign.get_center()))
                
                final_fade_in_animations.append(FadeIn(temp_c_value))
                
                final_move_animations.append(temp_c_value.animate.move_to(matrix[entry][MATRIX_C_ENTRY_CIJ_MOVED_VGROUP].get_center()))
                
                intial_fade_out_animations.append(FadeOut(multi_sign))
                intial_fade_out_animations.append(FadeOut(aij_value))
                intial_fade_out_animations.append(FadeOut(bij_value))
                    
                final_fade_out_animations.append(FadeOut(temp_c_value))   
        
        return intial_fade_in_animations, final_fade_in_animations, intial_move_animations, final_move_animations, intial_fade_out_animations, final_fade_out_animations
            
    def computeRowForFirstColumn(self, matrix, pos):
        intial_move_animations = []
        final_move_animations = []
        transform_animations = []
        fade_out_animations = []
        
        computed_c_value = matrix[pos][MATRIX_C_ENTRY_CIJ_MOVED_VGROUP]
        for col in range(MATRIX_ROW_COL_CT - 1, 0, -1):
            arcPath = ArcBetweenPoints(self.text_c_value_list[col].get_center(), matrix[pos][MATRIX_C_ENTRY_CIJ_MOVED_VGROUP].get_center(), angle=PI/2)
            intial_move_animations.append(MoveAlongPath(self.text_c_value_list[col], arcPath))
            computed_c_value += self.temp_computed_c_values[col] 
            
            final_move_animations.append(matrix[pos][MATRIX_C_ENTRY_CIJ_MOVED_VGROUP].animate.move_to(matrix[pos][MATRIX_C_ENTRY_COMPUTED_C_VGROUP].get_center()))
            
            fade_out_animations.append(FadeOut(self.text_c_value_list[col]))
            
        transform_animations.append(Transform(matrix[pos][MATRIX_C_ENTRY_CIJ_MOVED_VGROUP], computed_c_value))
            
        return intial_move_animations, final_move_animations, transform_animations, fade_out_animations
            