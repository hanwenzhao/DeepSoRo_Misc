import os, sys
import bpy

# IMPORT MESH
mesh = bpy.ops.import_mesh.ply(filepath="/home/hanwen/Documents/Github/DeepSoRo_Misc/Colorize_Sphere/105_color.ply")
mesh = bpy.context.active_object
#bpy.ops.object.mode_set(mode = 'VERTEX_PAINT')

# ADD LIGHT
light_data = bpy.data.lights.new('light', type='POINT')
light = bpy.data.objects.new('light', light_data)
bpy.context.collection.objects.link(light)

# ADD CAMERA
cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera', cam_data)
cam.location = (0, -2, 0)
bpy.context.collection.objects.link(cam)

# ADD MATERIAL
mat = bpy.data.materials.new(name='Material')
mat.use_nodes=True
# create two shortcuts for the nodes we need to connect
# Principled BSDF
ps = mat.node_tree.nodes.get('Principled BSDF')
# Vertex Color
vc = mat.node_tree.nodes.new("ShaderNodeVertexColor")
vc.location = (-300, 200)
vc.label = 'vc'
# connect the nodes
mat.node_tree.links.new(vc.outputs[0], ps.inputs[0])
# apply the material
mesh.data.materials.append(mat)

# CREATE A SCENE
scene = bpy.context.scene
scene.camera = cam
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "/home/hanwen/Documents/Github/DeepSoRo_Misc/Colorize_Sphere/105_color.png"

# RENDER
#bpy.ops.render.render(write_still=1)

