vlan = int(input("Ingresa el número de VLAN: "))

if 1 <= vlan <= 1005:
    print("VLAN de rango NORMAL")
elif 1006 <= vlan <= 4094:
    print("VLAN de rango EXTENDIDO")
else:
    print("VLAN inválida")
