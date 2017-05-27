from django.conf.urls import url

from user import views


urlpatterns = [
    url(
        r'^profile/$',
        views.UpdateProfile.as_view(
            template_name="user/edit_profile.html",
        ),
        name='edit_profile'
    ),

    url(
        r'^validate-email/$',
        views.ValidateEmail.as_view(),
        name='auth_validate_email',
    ),

    url(
        r'^check-email/$',
        views.CheckEmail.as_view(),
        name='auth_check_email',
    ),
]
