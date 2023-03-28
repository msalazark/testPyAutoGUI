# This is a sample Python script.
import pyautogui as robot
import time
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

lista_canciones = ["take on my","cant't stop"]
google = 174,202
direc = -1910,3
buscar = -1500,122
cancion = -1524,687
exit  = -22,-38
duracion = 2


def abrir(pos, click=1):
    # Use a breakpoint in the code line below to debug your script.
    robot.moveTo(pos)
    robot.click(clicks= click)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    abrir(google, click=2)

    time.sleep(2)
    robot.hotkey("alt","space")
    time.sleep(0.5)
    robot.typewrite("x")

    time.sleep(4)
    abrir(direc)
    robot.typewrite("www.youtube.com")
    robot.hotkey("enter")
    time.sleep(5)

    for elemento in range(len(lista_canciones)):
        print(elemento)
        abrir(buscar)
        robot.typewrite(lista_canciones[elemento])
        robot.hotkey("enter")
        time.sleep(2)
        abrir(cancion)
        time.sleep(duracion)

    abrir(exit)
    print("Proceso terminado")





