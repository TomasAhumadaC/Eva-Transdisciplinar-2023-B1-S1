#este codigo es mas para ir probando la compatibilidad entre nuestras partes del trabajo.
#----------------------------------------------------------------------
# Librerias
#----------------------------------------------------------------------
import pygame as PG, tkinter as TK, sys
from tkinter import ttk
#----------------------------------------------------------------------
# Constantes
#----------------------------------------------------------------------
nRES = (800, 500) ; lOk = True ; G = 9.8
#----------------------------------------------------------------------
# Coeficientes de roce
#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Crear Pantalla Tkinter
#----------------------------------------------------------------------
win = TK.Tk()
frame = ttk.Frame(win, width=250, height=250)
frame.pack()

#----------------------------------------------------------------------
# Crear Pantalla Pygame
#----------------------------------------------------------------------
def PVentana(nRES):
    PG.init()
    ventana = PG.display.set_mode(nRES)
    nVentana  = PG.display.set_caption('simulacion')
    return ventana
#----------------------------------------------------------------------
# Mostrar por pantalla tkinter
#----------------------------------------------------------------------
def button1_clicked():
    input_text = entry.get()
    output_text = "Iniciando simulacion"
    output_label.config(text=output_text)

def button2_clicked():
    input_text = entry.get()
    output_text = "calculando"
    output_label.config(text=output_text)

button1 = TK.Button(win, text="Iniciar Simulacion", command=button1_clicked)
button1.pack()

button2 = TK.Button(win, text="Calcular Ecuacion", command=button2_clicked)
button2.pack()

#----------------------------------------------------------------------
# Entrada de datos ##por terminar
#----------------------------------------------------------------------
entry = TK.Entry(win)
entry.pack()
#----------------------------------------------------------------------
# caso 1
#----------------------------------------------------------------------
#funcion
#----------------------------------------------------------------------
# caso 2
#----------------------------------------------------------------------
#funcion
#----------------------------------------------------------------------
# caso 3
#----------------------------------------------------------------------
#funcion

#----------------------------------------------------------------------
# While principal
#----------------------------------------------------------------------
ventana = PVentana(nRES)
font = PG.font.Font(None, 36)
clock = PG.time.Clock()
#----------------------------------------------------------------------
while lOk:
 for event in PG.event.get():
  if event.type == PG.QUIT:
     lOk = False
  if event.type == PG.KEYDOWN:
      if event.key == PG.K_ESCAPE:
          lOk = False

 cKey = PG.key.get_pressed()
 if cKey[PG.K_ESCAPE]:
     lOk = False
     
 ventana.fill((0, 255, 0))
 
 text_surface = font.render("simulacion", True, (255, 255, 255))
 text_rect = text_surface.get_rect(center=(nRES[0] // 2, nRES[1] // 2))
 ventana.blit(text_surface, text_rect)
 
 PG.display.flip()
 win.update()
 clock.tick(60)
PG.quit()
sys.exit()
