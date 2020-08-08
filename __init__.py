import bpy

bl_info = {
    'name': 'Bring assets locally',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Pack and unpack assets to have them locally',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-bring-assets/issues'
}


class PACK_OT_bring_locally(bpy.types.Operator):
    """Bring all assets locally"""
    bl_idname = "file.bring_assets_locally"
    bl_label = "Bring assets locally"

    def execute(self, context):
        bpy.ops.file.pack_all()
        bpy.ops.file.unpack_all(method='USE_LOCAL')
        return {'FINISHED'}


def register():
    bpy.utils.register_class(PACK_OT_bring_locally)


def unregister():
    bpy.utils.unregister_class(PACK_OT_bring_locally)


if __name__ == "__main__":
    register()
