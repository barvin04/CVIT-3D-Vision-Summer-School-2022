import bpy
import random

cube_size = 1
padding = 1.1

for x in range(0, 10, 1):
    for y in range(0, 10, 1):
        loc = (x * padding, y * padding, random.random())
        bpy.ops.mesh.primitive_cube_add(size=cube_size, enter_editmode=False, 
                                        align='WORLD', location=loc, scale=(1, 1, 1))
        
        box = bpy.context.object
        box.data.materials.append(bpy.data.materials["Material.001"])
        