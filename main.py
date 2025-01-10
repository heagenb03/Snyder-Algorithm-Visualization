from manim import Scene, VGroup, MathTex, FadeIn, FadeOut, ORIGIN, LEFT, RIGHT
import sys
sys.path.insert(0, 'scenes')

from constants import *
from scenes.scene1 import Scene1
from scenes.scene2 import Scene2
from scenes.scene3 import Scene3
from scenes.scene4 import Scene4

class Snyder(Scene):
    def construct(self):
        scene1 = Scene1()
        scene2 = Scene2()
        scene3 = Scene3()
        scene4 = Scene4()
        
        """
        Scene 1 
            #1. Create Matrix A, B, C
            #2. Move Aij & Bij values to corresponding Cij values / Fadeout Matrix A & B
        """
        
        #1        
        multi_sign = MathTex("\\times")
        equal_sign = MathTex("=")
        
        matrixA_scene1 = scene1.createMatrixA()
        matrixB_scene1 = scene1.createMatrixB()
        matrixC_scene1 = scene1.createMatrixC()
        algorithm_title = scene1.createTitle()
        
        matrices = VGroup(
            matrixC_scene1,
            equal_sign,
            matrixB_scene1,
            multi_sign,
            matrixA_scene1
        ).arrange(LEFT, buff=MATRIX_BUFFER*2)
        
        matrices.move_to(ORIGIN)
        
        self.add(algorithm_title)
        self.play(FadeIn(matrices))
        self.wait(5)
        
        #2
        move_animations = scene1.moveEnteriesToMatrixC(matrixA_scene1, matrixB_scene1, matrixC_scene1)
        self.play(*move_animations)
        self.wait(0.5)
        
        partial_matrixC_scene = scene1.createPartialMatrixC()
        
        self.play(FadeOut(matrices),
                FadeIn(partial_matrixC_scene.shift(RIGHT * scene1.RIGHT_ALINGMENT))
        )
        self.wait(0.5)
        
        """
        Scene 2 
            1. Move Matrix C to center
            2. Realign Matrix C for future animation purposes
        """
        
        #1
        matrixC_scene2 = scene2.createMatrixC()


        move_animations = scene2.moveMatrixCtoCenter(matrixB_scene1, partial_matrixC_scene)
        self.play(*move_animations)
        self.play(FadeOut(partial_matrixC_scene),
                FadeIn(matrixC_scene2.shift(RIGHT * scene2.RIGHT_ALINGMENT))
        )
        
        #2
        adjust_animations = scene2.realignMatrixC(matrixC_scene2)
        self.play(*adjust_animations)
        
        self.wait(1)
        
        """
        Scene 3
            1. Move corresponding Bij values across diagonally to corresponding Bij values
            2. Shift Bij values up/down based on the row
            3. Do intial computation of temp Cij values
            4. Move temp Cij values across right/left and compute final Cij values
        """
        
        #1
        move_animations = scene3.moveBValuesDiagonally(matrixC_scene2)
        
        self.play(*move_animations)
        self.wait(1)
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            scene3.text_c_value_list = []
            scene3.temp_computed_c_values = []
            #2
            if shift_count != 0:
                move_animations = scene3.moveBvaluesUp(matrixC_scene2)
            
                self.play(*move_animations)
                self.wait(1)
            #3
            total_fade_out_animations = []
            intial_fade_in_animations, final_fade_in_animations, intial_move_animations, final_move_animations, intial_fade_out_animations, final_fade_out_animations = scene3.computeTempCValues(matrixC_scene2)
            total_fade_out_animations.extend(final_fade_out_animations)
            
            self.play(*intial_fade_in_animations)
            self.wait(1)
            self.play(*intial_move_animations)
            self.wait(0.15)
            self.play(*final_fade_in_animations,
                    *intial_fade_out_animations)
            self.wait(1)
            self.play(*final_move_animations)
            self.wait(2)
            
            #4
            total_move_animations = []
            total_transform_animations = []
            
            for row in range(MATRIX_ROW_COL_CT):
                col = shift_count + row
                if col >= MATRIX_ROW_COL_CT:
                    col = abs(MATRIX_ROW_COL_CT - col)
                    
                entry_pos = col + (MATRIX_ROW_COL_CT * row)
                if col == 0:
                    move_animations, transform_animations, fade_out_animations = scene3.computeRowForFirstColumn(matrixC_scene2, entry_pos, row)
                    total_move_animations.extend(move_animations)
                    total_transform_animations.extend(transform_animations)
                    total_fade_out_animations.extend(fade_out_animations)
                elif col == MATRIX_ROW_COL_CT - 1:
                    move_animations, transform_animations, fade_out_animations = scene3.computeRowForLastColumn(matrixC_scene2, entry_pos, row)
                    total_move_animations.extend(move_animations)
                    total_transform_animations.extend(transform_animations)
                    total_fade_out_animations.extend(fade_out_animations)
                else:
                    move_animations, transform_animations, fade_out_animations = scene3.computeRowForOtherColumns(matrixC_scene2, entry_pos, row, col)
                    total_move_animations.extend(move_animations)
                    total_transform_animations.extend(transform_animations)
                    total_fade_out_animations.extend(fade_out_animations)
                
            self.play(*total_move_animations, run_time=2)
            self.wait(1)
            self.play(*total_transform_animations,
                    *total_fade_out_animations)
            self.wait(1.5)
                
            shift_count += 1
            
        """
        Scene 4
            1. Display finished Matrix C
            2. Return to intial state of Matrix A, B, C
        """

        #1
        fade_out_animations, move_animations = scene4.fadeOutEntries(matrixC_scene2), scene4.moveCEnteriesToCenter(matrixC_scene2)
        self.play(*fade_out_animations,
                *move_animations)
        self.wait(2)
        
        #2
        move_animations = scene4.moveMatrixCtoOriginalPosition(matrixC_scene1, matrixC_scene2)
        self.play(*move_animations)
        self.wait(1)
        
        matrixB_scene4 = scene1.createMatrixB()
        matrixA_scene4 = scene1.createMatrixA()
        
        matrices = VGroup(
            equal_sign,
            matrixB_scene4,
            multi_sign,
            matrixA_scene4
        ).arrange(LEFT, buff=MATRIX_BUFFER*2)
        matrices.move_to(ORIGIN).shift(LEFT * 1.5)
        
        self.play(FadeIn(matrices))
        self.wait(3)