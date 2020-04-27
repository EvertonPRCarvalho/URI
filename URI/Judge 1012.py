entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

area_tri = (A*C)/2
area_circ = 3.14159*(C**2)
area_trap = ((A+B)*C)/2
area_quad = B**2
area_ret = A*B

print("""
TRIANGULO: %.3f
CIRCULO: %.3f
TRAPEZIO: %.3f
QUADRADO: %.3f
RETANGULO: %.3f
"""%(area_tri, area_circ, area_trap, area_quad, area_ret))
