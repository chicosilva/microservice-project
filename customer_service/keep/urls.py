
from django.contrib import admin
import django_saml2_auth.views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
        # These are the SAML2 related URLs. You can change "^saml2_auth/" regex to
    # any path you want, like "^sso_auth/", "^sso_login/", etc. (required)
    path(r'^saml2_auth/', include('django_saml2_auth.urls')),

    # The following line will replace the default user login with SAML2 (optional)
    # If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
    # with this view.
    path(r'^accounts/login/$', django_saml2_auth.views.signin),

    # The following line will replace the admin login with SAML2 (optional)
    # If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
    # with this view.
    path(r'^admin/login/$', django_saml2_auth.views.signin),

]
