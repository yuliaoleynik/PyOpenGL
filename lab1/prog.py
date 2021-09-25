import glfw
from OpenGL.GL import *

import math as m
import sys


def Argument(*argv):
    if len(argv) == 0:
        print("NO ARGUMENTS")
    else:
        print(*argv[1:])

def main():
    print('Hello OpenGL!')
    Argument(*sys.argv)

    if not glfw.init():
        print('Ошиба при инициализации GLFW \n')
        exit()

    glfw.window_hint(glfw.SAMPLES, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3) 
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(640, 480, "Lesson 01 - RAINBOW - Oleynik Yulia PA-19-1", None, None)
    if not window:
        glfw.terminate()
        print('Невозможно открыть окно')
        exit()
    
    glfw.make_context_current(window)

    glfw.set_input_mode(window, glfw.STICKY_KEYS, GL_TRUE)

    colorRGB = 0.0
    while glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and glfw.window_should_close(window) == 0:
        glClearColor(m.sin(colorRGB * m.pi / 180), m.fabs(m.cos(colorRGB * m.pi / 180)), m.fabs(m.sin(colorRGB * m.pi / 180) + \
         m.cos(colorRGB * m.pi / 180)), 1.0)

        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

        if colorRGB <= 180:
            colorRGB += 0.1
        else:
            colorRGB = 0

    glfw.terminate()

main()

