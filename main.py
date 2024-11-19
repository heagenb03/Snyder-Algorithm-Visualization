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
            1. Move Bij values to corresponding Bij values
        """
        
        #1
        move_animations = scene3.moveBValues(matrixC_scene2)
        
        print(scene3.entry_b_values)
        self.play(*move_animations)
        self.wait(1)