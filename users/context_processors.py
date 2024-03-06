

def avatar_context(request):
    avatar_url = None  

   
    if request.user.is_authenticated and hasattr(request.user, 'avatar') and request.user.avatar and request.user.avatar.imagen:
        avatar_url = request.user.avatar.imagen.url

    return {'avatar_url': avatar_url}