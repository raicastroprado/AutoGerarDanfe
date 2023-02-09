import tkinter as tk
import os
import re
import sys
import time
import pyautogui

# funçao que é executada quando clicar  no botao 'iniciar gerador de DANFE'

def start_generator():

    
    time.sleep(1.5)

    path = r"C:\Users\Fiscal4\Desktop\auto buscar danfe\XMLs com erro"

    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            full_path = os.path.join(path, filename)

            with open(full_path, "r", encoding="utf-8") as f:
                xml_file = f.read()
            
            #tempo de espera para repetir o processo para cada XML
            time.sleep(2)

            # Abre o site https://consultadanfe.com/
            pyautogui.hotkey("win", "r")
            pyautogui.typewrite("https://consultadanfe.com/")
            pyautogui.press("enter")

            time.sleep(1)

            # Procura a chave da DANFE no arquivo XML
            chave = re.search(r"<chNFe>(\d+)", xml_file)
            if chave:
                chave = chave.group(1)
            else:
                print("Não foi possível encontrar a chave da DANFE no arquivo", filename)
                sys.exit(1)
    
            time.sleep(2)

            
            # Encontra a imagem da barra de texto para digitar a chave da DANFE

            imagem = 'Busca_Danfe.png'
            text_box = pyautogui.locateOnScreen(imagem, confidence=0.5)
            if text_box:
                text_box_center = pyautogui.center(text_box)
                pyautogui.click(text_box_center)
                pyautogui.typewrite(chave)
            else:
                print("Não foi possível encontrar a barra de texto para digitar a chave da DANFE")
                sys.exit(1)

            time.sleep(2)

            # Encontra a imagem do botão de busca
            search_button = pyautogui.locateOnScreen('Busca_Danfe_XML.png')
            if search_button:
                search_button_center = pyautogui.center(search_button)
                pyautogui.click(search_button_center)
            else:
                print("Não foi possível encontrar o botão de busca")
                sys.exit(1)


            # Espera a página carregar
            time.sleep(3)

            # Encontra a imagem do botão de download
            download_button = pyautogui.locateOnScreen('download_XML.png')
            if download_button:
                download_button_center = pyautogui.center(download_button)
                pyautogui.click(download_button_center)
                            
            else:
                print("Não foi possível encontrar o botão de download")

            time.sleep(2)
            
            # Encontra a imagem do botao de fechar 
            search_button = pyautogui.locateOnScreen('Botao_Fechar.PNG')
            if search_button:
                search_button_center = pyautogui.center(search_button)
                pyautogui.click(search_button_center)
                pyautogui.hotkey('Ctrl', 'w')
            else:
                print("Não foi possivel encontrar o botão de fechar")
                sys.exit(1)
            
            time.sleep(2)
def stop_generator():
    root.quit()

root = tk.Tk()
root.title('Gerador de DANFE')       

# Adiciona o botão 'Iniciar  gerador de DANFE'
start_button = tk.Button(root, text='Iniciar  gerador de DANFE', command=start_generator)
start_button.pack()

# Adiciona o botão 'Parar gerador de DANFE'
stop_button = tk.Button(root, text='Parar gerador de DANFE', command=stop_generator)
stop_button.pack()

#inicia a janela do progrma 
root.mainloop()
sys.exit(1)
