import keyboard as kb
import time
import pyautogui as auto

bucle = True
start = False
tipo = input('Publicacion (p) , reel(r) o historia(h)? (p/r/h): ')
input_iterations = input('Introducí el max de iteraciones (por defecto = 100): ')
iterations = 100 if input_iterations=='' else int(input_iterations)

def on_q_press(event):
    if event.name == 'q':
        print('finish')
        global bucle
        bucle = False

def on_s_press(event):
    if event.name == 's':
        print('start')
        global start
        start = True

kb.on_press(on_q_press)

kb.on_press(on_s_press)

bucle_number = 0

while bucle:

    if start:
    
        x , y = auto.position()
        auto.click(x,y)
        if tipo == 'p':
            auto.click(x,y)
        time.sleep(1)

        kb.press_and_release('right')
        time.sleep(1)
        
        bucle_number += 1

        if bucle_number > iterations:
            break

    else:
        print('Waiting to start <press "s">, if you leave <press "q">')
        time.sleep(3)