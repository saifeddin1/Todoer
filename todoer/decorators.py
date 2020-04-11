from django.http import HttpResponse
from django.shortcuts import redirect


def unauth_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('app')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func