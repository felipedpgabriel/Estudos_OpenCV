#!/usr/bin/env python3


# get_state_field(INT_STATE_FIELDS) -> Retorna informacoes sobre determinado 
#                                      indice do drone (bateria, yaw, pith, ...)
# get_battery() -> get_state_field('bat')

from djitellopy import Tello


tello = Tello()
tello.connect(False)
print("Nível da bateria do Michel: ")
print(tello.get_state_field('bat'))