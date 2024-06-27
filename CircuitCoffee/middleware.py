from django.shortcuts import redirect
from django.urls import reverse

class StaffRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in [reverse('account_login'), reverse('account_logout')]:
            return self.get_response(request)
       
        if request.user.is_authenticated and not request.user.is_staff:
            return redirect(reverse('account_logout'))

        response = self.get_response(request)
        return response

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith(reverse('account_login')) and not request.path.startswith(reverse('account_logout')):
            return redirect(reverse('account_login'))

        response = self.get_response(request)
        return response