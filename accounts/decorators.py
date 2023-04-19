from django.shortcuts import redirect

# Create your decorators here.

def unauthenticated(view_fucn):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('home')
    else:
      return view_fucn(request, *args, **kwargs)

  return wrapper_func