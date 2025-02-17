# -*- coding: utf-8 -*-


from django.urls import re_path as url
from django.conf import settings
from .views import RocketChatView


urlpatterns = (
    url(
        r'courses/{}/chat$'.format(
            settings.COURSE_ID_PATTERN,
        ),
        RocketChatView.as_view(),
        name='rocketchat_view',
    ),
)
