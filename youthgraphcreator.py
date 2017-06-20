import bpy

data = [5.51, 5.75, 4.25]
dates = ['6/7', '6/14', '6/21']

number_of_bars = len(data)
yscale = 10.0

starting_amount = 132.85
total = starting_amount

for i in data:
    total += i
    
goal = 500.0

message_done = ''

if (total >= goal):
    total = goal
    message_done = 'Our goal has\nbeen reached!'
else:
    message_done = 'We still have\n${0:.2f} left\nto go!'.format(round(goal - total, 2))

distance = 6 * (total / goal)

bar_scale = 0.4
bars_extrude = []
locations = []

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.frame_end = 350

bpy.context.scene.world.horizon_color = (0, 0, 0)

for i in range(int(number_of_bars)):
    locations.append((-6 + (11 / number_of_bars) * (i + 1)))
    bars_extrude.append(6 * (data[i] / yscale))

bpy.data.objects['Camera'].location = (0, 0, 20.73)
bpy.data.objects['Camera'].rotation_euler = (0, 0, 0)
bpy.data.cameras['Camera'].lens = 42

bpy.data.lamps['Lamp'].type = 'SUN'
bpy.data.objects['Lamp'].rotation_euler = (0.650328, 0.055217, 3.917027)

bpy.data.objects['Cube'].name = 'xaxis'
bpy.data.objects['xaxis'].scale = (6, 0.1, 0.1)
bpy.data.objects['xaxis'].location = (0, -3, 0)

bpy.ops.mesh.primitive_cube_add()
bpy.data.objects['Cube'].name = 'yaxis'
bpy.data.objects['yaxis'].scale = (0.1, 3, 0.1)
bpy.data.objects['yaxis'].location = (-5.9, 0.1, 0)

count = 1

bpy.context.scene.frame_current = 90

bpy.data.objects['xaxis'].select = True
bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')
bpy.ops.object.select_all(action="TOGGLE")

bpy.context.scene.frame_current = 196

bpy.data.objects['xaxis'].select = True
bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['yaxis'].select = True
bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')
bpy.ops.object.select_all(action='TOGGLE')

for i in locations:
    bpy.ops.mesh.primitive_plane_add()
    bpy.data.objects['Plane'].location = (i, -3, 0)
    bpy.data.objects['Plane'].rotation_euler = (1.570796, 0, 0)
    bpy.data.objects['Plane'].scale = (bar_scale, 0.08, 1)
    bpy.data.objects['Plane'].name = "Bar{0}".format(count)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, bars_extrude[count-1], 0), "constraint_axis":(False, True, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    bpy.ops.object.editmode_toggle()
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')
    count = count + 1

bpy.context.scene.frame_current = 120

for i in range(number_of_bars):
    bpy.context.scene.objects.active = bpy.data.objects['Bar{0}'.format(i+1)]
    bpy.data.objects['Bar{0}'.format(i+1)].select = True
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')
    bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 100

for i in range(number_of_bars):
    bpy.context.scene.objects.active = bpy.data.objects['Bar{0}'.format(i+1)]
    bpy.context.scene.objects.active.scale[2] = (yscale / data[i])
    bpy.ops.object.select_all(action='TOGGLE')

bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')

bpy.context.scene.frame_current = 90

for i in range(number_of_bars):
    bpy.context.scene.objects.active = bpy.data.objects['Bar{0}'.format(i+1)]
    bpy.context.scene.objects.active.scale[2] = 0
    bpy.data.objects["Bar{0}".format(i+1)].select = True
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')
    bpy.ops.object.select_all(action='TOGGLE')
    
bpy.context.scene.frame_current = 80

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.transform.translate(value=(0, 13, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')

bpy.context.scene.frame_current = 206

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.transform.translate(value=(0, -13, 0))
bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.transform.translate(value=(0, -13, 0))
bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocScale')

bpy.context.scene.frame_current = 120

bpy.ops.object.select_all(action='TOGGLE')

bpy.ops.mesh.primitive_cube_add()
bpy.data.objects['Cube'].name = 'topInc'
bpy.data.objects['topInc'].scale = (0.4, 0.02, 0.11)
bpy.data.objects['topInc'].location = (-5.9, 2.9, 0)
bpy.ops.anim.keyframe_insert_menu(type='Location')
bpy.ops.object.select_all(action='TOGGLE')

bpy.ops.mesh.primitive_cube_add()
bpy.data.objects['Cube'].name = 'midInc'
bpy.data.objects['midInc'].scale = (0.4, 0.02, 0.11)
bpy.data.objects['midInc'].location = (-5.9, 0, 0)
bpy.ops.anim.keyframe_insert_menu(type='Location')
bpy.ops.object.select_all(action='TOGGLE')

bpy.ops.object.text_add()
bpy.data.objects['Text'].name = 'topIncLabel'
bpy.data.curves['Text'].name = 'topIncLabel'
bpy.data.curves['topIncLabel'].align_x = 'RIGHT'
bpy.data.curves['topIncLabel'].align_y = 'CENTER'
bpy.data.objects['topIncLabel'].data.body = "${0:.2f}".format(round(yscale, 2))
bpy.data.objects['topIncLabel'].location = (-6.31, 2.9, 0)
bpy.data.objects['topIncLabel'].rotation_euler = (0, 0, 0.921704)
bpy.data.objects['topIncLabel'].scale = (0.6, 0.6, 0.6)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.ops.object.text_add()
bpy.data.objects['Text'].name = 'midIncLabel'
bpy.data.curves['Text'].name = 'midIncLabel'
bpy.data.curves['midIncLabel'].align_x = 'RIGHT'
bpy.data.curves['midIncLabel'].align_y = 'CENTER'
bpy.data.objects['midIncLabel'].data.body = "${0:.2f}".format(round(yscale / 2, 2))
bpy.data.objects['midIncLabel'].location = (-6.31, 0, 0)
bpy.data.objects['midIncLabel'].rotation_euler = (0, 0, 0.921704)
bpy.data.objects['midIncLabel'].scale = (0.6, 0.6, 0.6)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

for i in range(number_of_bars):
    bpy.ops.object.text_add()
    bpy.data.objects['Text'].name = 'xinc{0}'.format(i+1)
    bpy.data.curves['Text'].name = 'xinc{0}'.format(i+1)
    bpy.data.curves['xinc{0}'.format(i+1)].align_x = 'CENTER'
    bpy.data.curves['xinc{0}'.format(i+1)].align_y = 'CENTER'
    bpy.data.objects['xinc{0}'.format(i+1)].scale = (0.6, 0.6, 0.6)
    bpy.data.objects['xinc{0}'.format(i+1)].location = (bpy.data.objects['Bar{0}'.format(i+1)].location[0], -3.4, 0)
    bpy.data.objects['xinc{0}'.format(i+1)].data.body = dates[i]
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 196

bpy.data.objects['topInc'].select = True
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['midInc'].select = True
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['topIncLabel'].select = True
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['midIncLabel'].select = True
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

for i in range(number_of_bars):
    bpy.data.objects['xinc{0}'.format(i+1)].select = True
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 206

bpy.data.objects['topInc'].select = True
bpy.data.objects['topInc'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['midInc'].select = True
bpy.data.objects['midInc'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['topIncLabel'].select = True
bpy.data.objects['topIncLabel'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['midIncLabel'].select = True
bpy.data.objects['midIncLabel'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

for i in range(number_of_bars):
    bpy.data.objects['xinc{0}'.format(i+1)].select = True
    bpy.data.objects['xinc{0}'.format(i+1)].location[1] = -13
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 110

bpy.data.objects['topInc'].select = True
bpy.data.objects['topInc'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['midInc'].select = True
bpy.data.objects['midInc'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['topIncLabel'].select = True
bpy.data.objects['topIncLabel'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.data.objects['midIncLabel'].select = True
bpy.data.objects['midIncLabel'].location[0] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

for i in range(number_of_bars):
    bpy.data.objects['xinc{0}'.format(i+1)].select = True
    bpy.data.objects['xinc{0}'.format(i+1)].location[0] = -13
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 72

bpy.ops.object.text_add()
bpy.data.objects['Text'].name = 'Title1Text'
bpy.data.curves['Text'].name = 'Title1Text'
bpy.data.curves['Title1Text'].align_x = 'CENTER'
bpy.data.objects['Title1Text'].location = (0, 0.5, 0)
bpy.data.objects['Title1Text'].scale = (3, 3, 3)
bpy.data.objects['Title1Text'].data.body = 'Offerings\nby week'
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 10

bpy.data.objects['Title1Text'].select = True
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 1

bpy.data.objects['Title1Text'].location[1] = 13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 80

bpy.data.objects['Title1Text'].location[1] = -13
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 220

bpy.ops.object.text_add()
bpy.data.objects['Text'].name = 'Title2Text'
bpy.data.curves['Text'].name = 'Title2Text'
bpy.data.objects['Title2Text'].location = (0, 2.7, 0)
bpy.data.objects['Title2Text'].scale = (1.5, 1.5, 1.5)
bpy.data.objects['Title2Text'].data.body = 'Progress'
bpy.data.curves['Title2Text'].align_x = 'CENTER'
bpy.ops.anim.keyframe_insert_menu(type='Location')

bpy.context.scene.frame_current = 210

bpy.data.objects['Title2Text'].location = (0, 13, 0)
bpy.ops.anim.keyframe_insert_menu(type='Location')

bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 220
bpy.ops.mesh.primitive_cube_add()
bpy.data.objects['Cube'].name = 'left'
bpy.data.objects['left'].scale = (0.1, 3, 0.1)
bpy.data.objects['left'].location = (-3, -1, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 210
bpy.data.objects['left'].location = (-13, -1, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 220
bpy.ops.mesh.primitive_cube_add()
bpy.data.objects['Cube'].name = 'bottom'
bpy.data.objects['bottom'].scale = (1.6, 0.1, 0.1)
bpy.data.objects['bottom'].location = (-1.5, -4, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 210
bpy.data.objects['bottom'].location = (-11.5, -4, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 220
bpy.ops.mesh.primitive_cube_add()
bpy.data.objects['Cube'].name = 'right'
bpy.data.objects['right'].scale = (0.1, 3, 0.1)
bpy.data.objects['right'].location = (0, -1, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 210
bpy.data.objects['right'].location = (-10, -1, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 240
bpy.ops.mesh.primitive_cone_add()
bpy.data.objects['Cone'].location = (0, 2, 0)
bpy.data.objects['Cone'].rotation_euler = (0, -1.570796, 0)
bpy.data.objects['Cone'].scale = (0.1, 0.1, 0.4)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 220
bpy.data.objects['Cone'].location = (13, 2, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 250
bpy.ops.mesh.primitive_plane_add()
bpy.data.objects['Plane'].name = 'pbar'
bpy.data.objects['pbar'].location = (-1.5, -4, 0)
bpy.data.objects['pbar'].rotation_euler = (1.570796, 0, 0)
bpy.data.objects['pbar'].scale = (1.4, 0.09, 1)

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, -distance), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.ops.object.editmode_toggle()
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 230
bpy.data.objects['pbar'].scale = (1.4, 0.09, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 220
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 210
bpy.data.objects['pbar'].location[0] = bpy.data.objects['bottom'].location[0]
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 240
bpy.ops.object.text_add()
bpy.data.objects['Text'].name = 'Goal'
bpy.data.curves['Text'].name = 'Goal'
bpy.data.curves['Goal'].align_y = 'CENTER'
bpy.data.objects['Goal'].location = (0.75, 2, 0)
bpy.data.objects['Goal'].data.body = '${0:.2f}'.format(round(goal, 2))
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 220
bpy.data.objects['Goal'].location = (13.75, 2, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
bpy.ops.object.select_all(action='TOGGLE')

bpy.context.scene.frame_current = 270
bpy.ops.object.text_add()
bpy.data.objects['Text'].name = 'Message'
bpy.data.curves['Text'].name = 'Message'
bpy.data.curves['Message'].align_x = 'CENTER'
bpy.data.objects['Message'].location = (3.5, 0, 0)
bpy.data.objects['Message'].data.body = message_done
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

bpy.context.scene.frame_current = 250
bpy.data.objects['Message'].location = (3.5, -13, 0)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

text_t = bpy.data.materials.get('Text')
progress_t = bpy.data.materials.get('ProgressBar')
axes_t = bpy.data.materials.get('Axes')
bars_t = bpy.data.materials.get('Bars')

bpy.data.objects['Title1Text'].data.materials.append(text_t)
bpy.data.objects['yaxis'].data.materials.append(axes_t)
bpy.data.objects['midInc'].data.materials.append(bars_t)
bpy.data.objects['topInc'].data.materials.append(bars_t)
bpy.data.objects['midIncLabel'].data.materials.append(text_t)
bpy.data.objects['topIncLabel'].data.materials.append(text_t)

for i in range(number_of_bars):
    bpy.data.objects['Bar{0}'.format(i+1)].data.materials.append(bars_t)
    bpy.data.objects['xinc{0}'.format(i+1)].data.materials.append(text_t)
    
bpy.data.objects['Title2Text'].data.materials.append(text_t)
bpy.data.objects['left'].data.materials.append(bars_t)
bpy.data.objects['bottom'].data.materials.append(bars_t)
bpy.data.objects['right'].data.materials.append(bars_t)
bpy.data.objects['Cone'].data.materials.append(axes_t)
bpy.data.objects['Goal'].data.materials.append(axes_t)
bpy.data.objects['pbar'].data.materials.append(progress_t)
bpy.data.objects['Message'].data.materials.append(text_t)