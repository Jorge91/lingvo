# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from django.views.generic import TemplateView



class IndexView(TemplateView):
    '''
    Renders the index page
    '''
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)


class LoginView(TemplateView):
    """
    Renders the login page
    """
    template_name = "login.html"


class LogoutView(View):
    """
    Logout a user and redirect it to the AFTER_LOGOUT_URL
    """

    def get(self, request):
        logout(request)
        return redirect('/')