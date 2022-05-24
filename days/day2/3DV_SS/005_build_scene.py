import bpy
import random
import os

object_path = "/home/iddb/projects/3dvss_blender/assets/"
base_plane_size = 100
output_dir = "/home/iddb/projects/3dvss_blender/output/"

def move_to_floor(object_name):
    bpy.ops.object.select_all(action='DESELECT')
    obj = bpy.context.scene.objects[object_name]
    # Also move the box to the ground properly
    minz =  min((obj.matrix_world @ v.co)[2] for v in obj.data.vertices)
    obj.location[2] -= minz

def generate_random_name():
    rad = "".join([chr(random.randint(0, 26) + 97)  for ix in range(6)])
    return rad

def load_object(obj_name, location=(0, 0, 0)):
    # Get list of old objects
    old_objects = set(bpy.context.scene.objects)

    # Import the object
    bpy.ops.import_scene.fbx(filepath=object_path + obj_name)

    # Get the new object
    obj = (set(bpy.context.scene.objects) - old_objects).pop()

    # Rename
    assigned_name = "added_{}".format(generate_random_name()) + obj_name
    obj.name = assigned_name

    obj.location = location
    
    return assigned_name


bpy.ops.mesh.primitive_plane_add(size=base_plane_size, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1,1,1))
bpy.context.active_object.name = "base_plane"

objects_avail = ["tree_01.fbx", "tree_02.fbx", "tree_03.fbx",
                "bush_01.fbx", "car_01.fbx", "car_02.fbx", "car_03.fbx"]
for ix in range(5):
    x = random.random()*10
    y = random.random()*10
    tree_name = load_object(random.choice(objects_avail), (x, y, 0))
    move_to_floor(tree_name)


# Add a sun lamp above the grid.
bpy.ops.object.light_add(
    type='SUN',
    radius=1.0,
    location=(0.0, 0.0, 12.5))

bpy.ops.object.camera_add(
    location=(15.0, 15.0, 15.0),
    rotation=(0.8726646304130554, 0.0, 2.1834065914154053))
bpy.context.object.data.lens = 28

bpy.context.scene.camera = bpy.context.object

#bpy.context.scene.render.engine = 'CYCLES'
#bpy.context.scene.cycles.device = 'GPU'
#bpy.context.scene.cycles.use_denoising = True

#bpy.context.scene.render.resolution_x = 1024
#bpy.context.scene.render.resolution_y = 512
#bpy.context.scene.render.filepath = os.path.join(output_dir, ("render_{}.png".format(generate_random_name())))
#bpy.ops.render.render(write_still = True)