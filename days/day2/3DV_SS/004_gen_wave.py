import bpy
from math import sin, tau

# clear meshes in the scene
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)

# animation variables
total_frames = 150
theta = 0.0

# define a one hundred frame timeline
bpy.context.scene.frame_end = total_frames
bpy.context.scene.frame_start = 0

for x in range(10):
    # generate a grid of boxes
    for y in range(10):
        box = bpy.ops.mesh.primitive_cube_add()
        box = bpy.context.object
        box.name = 'box-{}-{}'.format(x, y)
        box.location[0] = x * 2
        box.location[1] = y * 2
        # add keyframes to each box
        for frame in range(0, total_frames):
            bpy.context.scene.frame_set(frame)
            box.location.z = sin(theta + x) * 2 - 1
            box.keyframe_insert(data_path='location')
            scale = sin(theta + y)
            box.scale = (scale, scale, scale)
            box.keyframe_insert(data_path='scale')
            theta += tau / total_frames