bl_info = {
    "blender": (2, 91, 2),
    "category": "Object",
    "name": "Batch FBX Exporter"
}

import bpy

class BatchExporter(bpy.types.Operator):
    """Batch Export Selected Objects as FBX"""
    bl_idname = "object.batch_fbx_export"
    bl_label = "Batch Export Selected Objects as FBX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objects = bpy.context.selected_objects

        for obj in objects:
            bpy.ops.object.select_all(action='DESELECT')
            path = bpy.path.abspath("//" + obj.name + ".fbx")
            obj.select_set(True)
            bpy.ops.export_scene.fbx(filepath=path, use_selection=True)

        for obj in objects:
            obj.select_set(True)

        return { 'FINISHED' }

def menu_func(self, context):
    self.layout.operator(BatchExporter.bl_idname)

def register():
    bpy.utils.register_class(BatchExporter)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BatchExporter)

if __name__ == "__main__":
    register()
