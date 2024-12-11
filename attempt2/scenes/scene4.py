from manim import FadeOut, RIGHT
from constants import *
from intial import Intial
from scene3 import Scene3

class Scene4:
    def __init__(self):
        self.intial = Intial()
        self.scene3 = Scene3()
        
    def fadeOutEntries(self, matrix):
        """Fade out Aij & Bij entries

        Args:
            matrix (VGroup): matrix used in the scene

        Returns:
            list: list of animations that fade out Aij and Bij VGroups
        """
        fade_out_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            fade_out_animations.append(FadeOut(matrix[entry][MATRIX_C_ENTRY_A_VGROUP]))
            fade_out_animations.append(FadeOut(matrix[entry][MATRIX_C_ENTRY_B_VGROUP]))
            
        return fade_out_animations
    
    def moveCEnteriesToCenter(self, matrix):
        """Move Matrix Cij values to center of their respective boxes

        Args:
            matrix (VGroup): matrix used in the scene

        Returns:
            list: list of animations that move each Cij value to the center of their respective box
        """
        move_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            numbers = matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP]
            move_animations.append(numbers.animate.move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center()))
            
        return move_animations
    
    def moveMatrixCtoOriginalPosition(self, matrixPos, matrixC):
        """Move Matrix C to original position from scene 1

        Args:
            matrixPos (VGroup): matrix used as reference for positioning
            matrixC (VGroup): matrix being moved

        Returns:
            list: list of animations that move each VGroup part of Matrix C to the original position
        """
        alingment = RIGHT * 0.15
        move_animations = []
        for entry in range(MATRIX_ROW_COL_CT**2):
            #Matrix C Boxes
            boxes = matrixC[entry][MATRIX_C_BOX_VGROUP]
            move_animations.append(boxes.animate.move_to(self.intial.getTargetPosition(matrixPos, entry, MATRIX_C_BOX_VGROUP) + alingment))
            
            #Enteries C
            numbers = matrixC[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP]
            move_animations.append(numbers.animate.move_to(self.intial.getTargetPosition(matrixPos, entry, MATRIX_C_BOX_VGROUP) + alingment))   
                
        return move_animations