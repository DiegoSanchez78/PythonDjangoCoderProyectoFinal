# from .models import Avatar

# def avatar_context(request):
#     avatar_url = None

#     if request.user.is_authenticated:
#         try:
#             avatar_url = request.user.avatar.imagen.url
#         except Avatar.DoesNotExist:
#             pass
#     print("Avatar URL:", avatar_url)
#     return {'avatar_url': avatar_url}

def avatar_context(request):
    avatar_url = None  # Set a default value

    # Check if the user is authenticated and has an avatar
    if request.user.is_authenticated and hasattr(request.user, 'avatar') and request.user.avatar and request.user.avatar.imagen:
        avatar_url = request.user.avatar.imagen.url

    return {'avatar_url': avatar_url}