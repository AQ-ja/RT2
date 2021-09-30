from gl import Raytracer, V3
from obj import *
from figu import *

# Dimensiones
width = 1080
height = 500

# Materiales
# La opaca se intento hacer con un material y textura como un coco. 
coco = Material(diffuse = (0.54,0.29,0.07), spec = 64, ior= 0.5, matType= OPAQUE)
esmeralda = Material(diffuse = (0,0.6,0.45), spec = 64, ior= 0.5, matType= OPAQUE2)
reflectivas = Material( spec = 128, matType = REFLECTIVE)
vidrio = Material(diffuse=(0.68, 0.93, 0.93) ,spec = 64, ior = 1.33, matType = TRANSPARENT)



# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('2k.bmp')

# Luces
rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))

# Objetos
rtx.scene.append( Sphere(V3(-6,2,-8), 1.5, reflectivas ))
rtx.scene.append( Sphere(V3(-2,0,-8), 1.5, vidrio ))
rtx.scene.append( Sphere(V3(2,0,-8), 1.5, vidrio ))
rtx.scene.append( Sphere(V3(6,2,-8), 1.5, reflectivas))
rtx.scene.append( Sphere(V3(-5,-2,-8), 1.5, coco))
rtx.scene.append( Sphere(V3(5,-2, -8), 1.5, esmeralda))




# Terminar
rtx.glRender()
rtx.glFinish('RT2.bmp')

