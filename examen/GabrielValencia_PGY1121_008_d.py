import numpy as np
import funciones as fn

fn.menu
opciones=fn.validar_menu()
if opciones==1:
    fn.ubicaciones_disponibles()
elif opciones==2:
    fn.personas_asistentes()
elif opciones==3:
    pass
elif opciones ==4:
    fn.comprar_entrada()
else:
    print("gracias por su tiempo")







