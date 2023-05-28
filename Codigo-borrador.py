#este codigo es mas para ir probando la compatibilidad entre nuestras partes del trabajo.
#----------------------------------------------------------------------
# Librerias
#----------------------------------------------------------------------
import pygame as PG, sys
#----------------------------------------------------------------------
# Constantes
#----------------------------------------------------------------------
nRES = (800, 500) ; lOk = True
#----------------------------------------------------------------------
# Crear Pantalla
#----------------------------------------------------------------------
def Ventana(nRES):
    PG.init()
    ventana = PG.display.set_mode(nRES)
    nVentana  = PG.display.set_caption('Programa Beta 0.1')
    return ventana
#----------------------------------------------------------------------
ventana = Ventana(nRES)
#----------------------------------------------------------------------
# While principal
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
 PG.display.flip()

PG.quit()
sys.exit()
