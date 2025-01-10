from manim import VGroup
from constants import *
from intial import Intial

class Scene1:
    def __init__(self):
        self.intial = Intial()
        self.RIGHT_ALINGMENT = 3.8
    
    def createMatrixA(self):
        """Create Matrix A

        Returns:
            VGroup: Matrix A with two VGroups - one for the box and one for the number
        """
        box_list = []
        matrix = VGroup()
    
        for entry in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createMatrixEntry(MATRIX_A_NUMBERS[entry], MATRIX_A_COLOR))
        
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)

        return matrix

    def createMatrixB(self):
        """Create Matrix B

        Returns:
            VGroup: Matrix B with two VGroups - one for the box and one for the number
        """
        box_list = []
        matrix = VGroup()
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createMatrixEntry(MATRIX_B_NUMBERS[entry], MATRIX_B_COLOR))
        
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        
        return matrix

    def createMatrixC(self):
        """Create Empty Matrix C

        Returns:
            VGroup: Empty Matrix C with two VGroups - one for the box and one for the number
        """
        box_list = []
        matrix = VGroup()
        
        for box in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createBlankMatrixEntries())
        matrix.add(*box_list)
        
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        return matrix
    
    def moveEnteriesToMatrixC(self, matrixA, matrixB, matrixC):
        """Move Matrix A & B enteries to Matrix C

        Args:
            matrixA (VGroup): Matrix A from scene 1
            matrixB (VGroup): Matrix B from scene 2
            matrixC (VGroup): Matrix C from scene 2

        Returns:
            list: list of animations that move each entry to corresponding box in Matrix C
        """
        move_animations = []
        
        for entry in range(MATRIX_ROW_COL_CT**2):
            vgroup = 1
            numbers = matrixA[entry][vgroup]
            move_animations.append(numbers.animate.move_to(self.intial.getTargetPosition(matrixC, entry, vgroup))) 
            
            numbers = matrixB[entry][vgroup]
            move_animations.append(numbers.animate.move_to(self.intial.getTargetPosition(matrixC, entry, vgroup + 1))) 
        
        return move_animations
    
    def createPartialMatrixC(self):
        """Create Matrix C with moved Aij & Bij entries

        Returns:
            Vgroup: Matrix C with only entries Aij & Bij
        """
        box_list = []
        matrix = VGroup()
        
        for box in range(MATRIX_ROW_COL_CT**2):
            box_list.append(self.intial.createMatrixTwoEntries(MATRIX_A_NUMBERS[box], MATRIX_B_NUMBERS[box], MATRIX_A_COLOR, MATRIX_B_COLOR))
            
        matrix.add(*box_list)
        matrix.arrange_in_grid(rows=MATRIX_ROW_COL_CT, cols=MATRIX_ROW_COL_CT, buff=MATRIX_BUFFER)
        return matrix