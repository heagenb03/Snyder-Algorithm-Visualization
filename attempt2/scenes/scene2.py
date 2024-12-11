from manim import VGroup, LEFT
from constants import *
from intial import Intial

class Scene2:
    def __init__(self):
        self.intial = Intial()
        self.RIGHT_ALINGMENT = 0.30
        
    def createMatrixC(self):
        """Create Matrix C with four entries

        Returns:
            VGroup: Matrix C with two VGroups - one for the number and one for the box
        """
        matrix = VGroup()
        box_list = []
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createMatrixFourEntries(MATRIX_A_NUMBERS[entry], MATRIX_B_NUMBERS[entry], 0, 0, MATRIX_A_COLOR, MATRIX_B_COLOR, C_VALUES_COLOR))
            
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        return matrix
    
    def moveMatrixCtoCenter(self, matrixB, matrixC):
        """Move Matrix C to center of the screen

        Args:
            matrixB (VGroup): Matrix B from scene 1 (for positioning)
            matrixC (VGroup): Matrix C from scene 2

        Returns:
            list: list of animations that move each VGroup part of Matrix C to the center of the screen
        """
        alingmnet = LEFT * 1.5
        move_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            #Matrix C
            boxes = matrixC[entry][MATRIX_C_BOX_VGROUP]
            move_animations.append(boxes.animate.move_to(self.intial.getTargetPosition(matrixB, entry, MATRIX_C_BOX_VGROUP) + alingmnet))
            
            #Enteries A
            numbers = matrixC[entry][MATRIX_C_ENTRY_A_VGROUP]
            move_animations.append(numbers.animate.move_to(self.intial.getTargetPosition(matrixB, entry, MATRIX_C_ENTRY_A_VGROUP) + alingmnet))   
                
            #Enteries B
            numbers = matrixC[entry][MATRIX_C_ENTRY_B_VGROUP]
            move_animations.append(numbers.animate.move_to(self.intial.getTargetPosition(matrixB, entry, MATRIX_C_ENTRY_B_VGROUP) + alingmnet))
            
        return move_animations
    
    def realignMatrixC(self, matrixC):
        """Realign Matrix moved aij entry positioning for future animation purposes

        Args:
            matrixC (VGroup): Matrix C

        Returns:
            list: list of undisplayed/hidden animations that adjust positioning
        """
        adjust_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            numbers = matrixC[entry][MATRIX_C_ENTRY_TEMP_C_VGROUP]
            adjust_animations.append(numbers.animate.move_to(self.intial.getTargetPosition(matrixC, entry, MATRIX_C_ENTRY_TEMP_C_VGROUP)))
            
        return adjust_animations