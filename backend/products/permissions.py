from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # taken from the DjangoModelPermissions lib code
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)


#example - but here is a small issue that one permission granted is enough to give
#all the rest permissions
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.add_product"): #'app_name.verb_model_name'
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #         return False
    #     return False

    #If I would track the user
    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user