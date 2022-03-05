import pyautogui as auto
from time import sleep

name = input('Insira Seu Nome Aqui: ')

print(f'Bem Vindo {name} Vamos Começar ')


hotkey_01 = str(input('Deseja Inseriar uma Tecla De Atalho ? Se Sim Digite a Primeira Tecla Aqui: '))

hotkey_02 = str(input('Insira a Segunda Tecla Aqui: '))

auto.hotkey(hotkey_01, hotkey_02)
