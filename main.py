bl_info = {
    "name": "Batch FBX Exporter", 
    "category": "Object",
    "blender": (2, 80, 0)
}

import bpy

class BatchExporter(bpy.types.Operator):
    """Batch FBX Exporter"""
    bl_idname = "object.batch_fbx_export"
    bl_label = "Batch Export FBX"
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

def register():
    bpy.utils.register_class(BatchExporter)

def unregister():
    bpy.utils.unregister_class(BatchExporter)

if __name__ == "__main__":
    register()
