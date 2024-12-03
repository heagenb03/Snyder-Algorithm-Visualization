from manim import Scene, VGroup, MathTex, FadeIn, FadeOut, ORIGIN, LEFT, RIGHT
import sys
sys.path.insert(0, 'scenes')

from constants import *
from scenes.scene1 import Scene1
from scenes.scene2 import Scene2
from scenes.scene3 import Scene3

class Snyder(Scene):
    def construct(self):
        scene1 = Scene1()
        scene2 = Scene2()
        scene3 = Scene3()
        
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
        
        matrices = VGroup(
            matrixC_scene1,
            equal_sign,
            matrixB_scene1,
            multi_sign,
            matrixA_scene1
        ).arrange(LEFT, buff=MATRIX_BUFFER*2)
        
        matrices.move_to(ORIGIN)
        
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
            2. Compute corresponding Cij values
            3. Move Bij values up/down based on the row
        """
        
        #1
        move_animations = scene3.moveBValuesDiagonally(matrixC_scene2)
        
        self.play(*move_animations)
        self.wait(1)
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            total_intial_fade_in_animations = []
            total_final_fade_in_animations = []
            total_intial_move_animations = []
            total_final_move_animations = []
            total_intial_fade_out_animations = []
            total_fade_out_animations = []
            scene3.temp_computed_c_values = []
            scene3.text_c_value_list = []
            
            #2
            for row in range(MATRIX_ROW_COL_CT):
                col = shift_count + row
                
                if col >= MATRIX_ROW_COL_CT:
                    col = abs(MATRIX_ROW_COL_CT - col)

                move_entry_pos = (row * MATRIX_ROW_COL_CT) + col
                row_slice = slice(row * MATRIX_ROW_COL_CT, MATRIX_ROW_COL_CT + (row * MATRIX_ROW_COL_CT))
                
                intial_fade_in_animations, final_fade_in_animations, intial_move_animations, final_move_animations, intial_fade_out_animations, final_fade_out_animations = scene3.computeCValues(matrixC_scene2, move_entry_pos, row_slice)
                total_intial_fade_in_animations.extend(intial_fade_in_animations)
                total_final_fade_in_animations.extend(final_fade_in_animations)
                total_intial_move_animations.extend(intial_move_animations)
                total_final_move_animations.extend(final_move_animations)
                total_intial_fade_out_animations.extend(intial_fade_out_animations)
                total_fade_out_animations.extend(final_fade_out_animations)
                
            self.play(*total_intial_fade_in_animations)
            self.wait(1)
            self.play(*total_intial_move_animations)
            self.wait(0.15)
            self.play(*total_final_fade_in_animations,
                    *total_intial_fade_out_animations)
            self.wait(1)
            self.play(*total_final_move_animations)
            self.wait(2)
            
            #3
            total_intial_move_animations = []
            total_final_move_animations = []
            total_intial_fade_out_animations = []
            total_transform_animations = []
            
            for row in range(MATRIX_ROW_COL_CT):
                col = shift_count + row
                
                if col >= MATRIX_ROW_COL_CT:
                    col = abs(MATRIX_ROW_COL_CT - col)

                move_entry_pos = (row * MATRIX_ROW_COL_CT) + col
                row_slice = slice(row * MATRIX_ROW_COL_CT, MATRIX_ROW_COL_CT + (row * MATRIX_ROW_COL_CT))
                
                if col == 0:
                    intial_move_animations, final_move_animations, transform_animations, fade_out_animations = scene3.moveEnteriesAcrossRightAndCompute(matrixC_scene2, move_entry_pos, row)
                    total_intial_move_animations.extend(intial_move_animations)
                    total_final_move_animations.extend(final_move_animations)
                    total_transform_animations.extend(transform_animations)
                    total_intial_fade_out_animations.extend(fade_out_animations)
                
                
                elif col == MATRIX_ROW_COL_CT - 1:
                    intial_move_animations, final_move_animations, transform_animations, fade_out_animations = scene3.moveEnteriesAcrossLeftAndCompute(matrixC_scene2, move_entry_pos, row)
                    total_intial_move_animations.extend(intial_move_animations)
                    total_final_move_animations.extend(final_move_animations)
                    total_transform_animations.extend(transform_animations)
                    total_intial_fade_out_animations.extend(fade_out_animations)
                
                else:
                    intial_move_animations, final_move_animations, transform_animations, fade_out_animations = scene3.moveEnteriesAcrossRightAndLeftAndCompute(matrixC_scene2, move_entry_pos, col, row)
                    total_intial_move_animations.extend(intial_move_animations)
                    total_final_move_animations.extend(final_move_animations)
                    total_transform_animations.extend(transform_animations)
                    total_intial_fade_out_animations.extend(fade_out_animations)
                
            self.play(*total_intial_move_animations)
            self.wait(1)
            self.play(*total_final_move_animations)
            self.wait(1)
            self.play(*total_transform_animations,
                    *total_intial_fade_out_animations)
            self.wait(1)
            self.play(*total_fade_out_animations)
            self.wait(1)
            
            #4
            move_animations = scene3.moveBvaluesUp(matrixC_scene2, shift_count)
            
            self.play(*move_animations)
            self.wait(1)
            
            shift_count += 1
            