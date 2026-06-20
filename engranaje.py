import bpy
import math

# Limpiar escena de objetos previos para evitar duplicados
objetos_a_borrar = ["Cube", "Fabrizio", "Almeida"]
for nombre in objetos_a_borrar:
    if nombre in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[nombre], do_unlink=True)

# Parámetros comunes de los engranajes
num_teeth = 16
tooth_width = 0.35
helix_angle_deg = 25.0

# --- CREAR PRIMER ENGRANAJE ("Fabrizio" con grabado "FABRIZIO") ---
# 1. Crear base del engranaje
bpy.ops.mesh.primitive_cylinder_add(radius=2.0, depth=0.8, vertices=32, location=(0,0,0))
gear_1 = bpy.context.object
gear_1.name = "Fabrizio"

# 2. Crear dientes rectos mediante operación booleana UNION
for i in range(num_teeth):
    angle = (2 * math.pi / num_teeth) * i
    x = math.cos(angle) * 2.0
    y = math.sin(angle) * 2.0
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(x, y, 0))
    tooth = bpy.context.object
    tooth.scale = (tooth_width, 0.4, 0.8)
    tooth.rotation_euler = (0, 0, angle)
    bool_mod = gear_1.modifiers.new(name=f"Tooth_{i}", type="BOOLEAN")
    bool_mod.operation = "UNION"
    bool_mod.object = tooth
    bpy.context.view_layer.objects.active = gear_1
    bpy.ops.object.modifier_apply(modifier=bool_mod.name)
    bpy.data.objects.remove(tooth, do_unlink=True)

# 3. Aplicar deformación helicoidal (Twist positivo)
twist_mod_1 = gear_1.modifiers.new(name="HelixTwist", type="SIMPLE_DEFORM")
twist_mod_1.deform_method = 'TWIST'
twist_mod_1.deform_axis = 'Z'
twist_mod_1.angle = math.radians(helix_angle_deg)
bpy.context.view_layer.objects.active = gear_1
bpy.ops.object.modifier_apply(modifier=twist_mod_1.name)

# 4. Crear texto 3D para el grabado "FABRIZIO"
bpy.ops.object.text_add(location=(0.0, 1.0, 0.35))
text_obj_1 = bpy.context.object
text_obj_1.data.body = "FABRIZIO"
text_obj_1.data.size = 0.3
text_obj_1.data.extrude = 0.1
text_obj_1.data.align_x = 'CENTER'
text_obj_1.data.align_y = 'CENTER'

# Convertir el texto a malla
bpy.context.view_layer.objects.active = text_obj_1
text_obj_1.select_set(True)
bpy.ops.object.convert(target='MESH')

# Aplicar diferencia booleana para grabar el texto
bool_text_1 = gear_1.modifiers.new(name="EngraveText", type="BOOLEAN")
bool_text_1.operation = "DIFFERENCE"
bool_text_1.object = text_obj_1
bpy.context.view_layer.objects.active = gear_1
bpy.ops.object.modifier_apply(modifier=bool_text_1.name)
bpy.data.objects.remove(text_obj_1, do_unlink=True)

# 5. Agujero del eje central (operación booleana DIFFERENCE)
bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=1.0, vertices=16, location=(0,0,0))
shaft_hole_1 = bpy.context.object
bool_mod_1 = gear_1.modifiers.new(name="ShaftHole", type="BOOLEAN")
bool_mod_1.operation = "DIFFERENCE"
bool_mod_1.object = shaft_hole_1
bpy.context.view_layer.objects.active = gear_1
bpy.ops.object.modifier_apply(modifier=bool_mod_1.name)
bpy.data.objects.remove(shaft_hole_1, do_unlink=True)


# --- CREAR SEGUNDO ENGRANAJE ("Almeida" con grabado "ALMEIDA") ---
# 1. Crear base del engranaje
bpy.ops.mesh.primitive_cylinder_add(radius=2.0, depth=0.8, vertices=32, location=(0,0,0))
gear_2 = bpy.context.object
gear_2.name = "Almeida"

# 2. Crear dientes rectos mediante operación booleana UNION
for i in range(num_teeth):
    angle = (2 * math.pi / num_teeth) * i
    x = math.cos(angle) * 2.0
    y = math.sin(angle) * 2.0
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(x, y, 0))
    tooth = bpy.context.object
    tooth.scale = (tooth_width, 0.4, 0.8)
    tooth.rotation_euler = (0, 0, angle)
    bool_mod = gear_2.modifiers.new(name=f"Tooth_{i}", type="BOOLEAN")
    bool_mod.operation = "UNION"
    bool_mod.object = tooth
    bpy.context.view_layer.objects.active = gear_2
    bpy.ops.object.modifier_apply(modifier=bool_mod.name)
    bpy.data.objects.remove(tooth, do_unlink=True)

# 3. Aplicar deformación helicoidal (Twist negativo)
twist_mod_2 = gear_2.modifiers.new(name="HelixTwist", type="SIMPLE_DEFORM")
twist_mod_2.deform_method = 'TWIST'
twist_mod_2.deform_axis = 'Z'
twist_mod_2.angle = math.radians(-helix_angle_deg)
bpy.context.view_layer.objects.active = gear_2
bpy.ops.object.modifier_apply(modifier=twist_mod_2.name)

# 4. Crear texto 3D para el grabado "ALMEIDA"
bpy.ops.object.text_add(location=(0.0, 1.0, 0.35))
text_obj_2 = bpy.context.object
text_obj_2.data.body = "ALMEIDA"
text_obj_2.data.size = 0.3
text_obj_2.data.extrude = 0.1
text_obj_2.data.align_x = 'CENTER'
text_obj_2.data.align_y = 'CENTER'

# Convertir el texto a malla
bpy.context.view_layer.objects.active = text_obj_2
text_obj_2.select_set(True)
bpy.ops.object.convert(target='MESH')

# Aplicar diferencia booleana para grabar el texto
bool_text_2 = gear_2.modifiers.new(name="EngraveText", type="BOOLEAN")
bool_text_2.operation = "DIFFERENCE"
bool_text_2.object = text_obj_2
bpy.context.view_layer.objects.active = gear_2
bpy.ops.object.modifier_apply(modifier=bool_text_2.name)
bpy.data.objects.remove(text_obj_2, do_unlink=True)

# 5. Agujero del eje central (operación booleana DIFFERENCE)
bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=1.0, vertices=16, location=(0,0,0))
shaft_hole_2 = bpy.context.object
bool_mod_2 = gear_2.modifiers.new(name="ShaftHole", type="BOOLEAN")
bool_mod_2.operation = "DIFFERENCE"
bool_mod_2.object = shaft_hole_2
bpy.context.view_layer.objects.active = gear_2
bpy.ops.object.modifier_apply(modifier=bool_mod_2.name)
bpy.data.objects.remove(shaft_hole_2, do_unlink=True)

# --- ACOPLAMIENTO MECÁNICO Y POSICIONAMIENTO ---
# Distancia entre centros = radio1 + radio2 = 2.0 + 2.0 = 4.0
gear_2.location = (4.0, 0.0, 0.0)

# Desfase de rotación en Z para que los dientes encajen perfectamente
gear_2.rotation_euler = (0.0, 0.0, math.pi + (math.pi / num_teeth))

# Seleccionar ambos objetos en la escena de Blender
for obj in [gear_1, gear_2]:
    obj.select_set(True)
bpy.context.view_layer.objects.active = gear_1

print("Engranajes helicoidales acoplados con grabados 'FABRIZIO' y 'ALMEIDA' creados exitosamente.")
