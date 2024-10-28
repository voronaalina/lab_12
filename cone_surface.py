import cone_module

radius = float(input("радіус конуса: "))
height = float(input("висота конуса: "))

volume = cone_module.cone_volume(radius, height)
volume = round(volume, 1)
surf_area = cone_module.surface_area(radius, height)
surf_area = round(surf_area, 1)
print("об'єм конуса: ", volume)
print("площа поверхні конуса: ", surf_area)
