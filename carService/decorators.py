import re

from rest_framework import status
from rest_framework.response import Response

from carService.models import Profile
from carService.models.Organization import Organization


def organization_control(view_func):
    def wrap(request, *args, **kwargs):
        full_path = request.get_full_path()

        '''referer = request.META.get('HTTP_REFERER')
        if not referer:
            return None

        # remove the protocol and split the url at the slashes
        referer = re.sub('^https?:\/\/', '', referer).split('/')
        referer = re.sub('www.', '', referer[0])

        organization = Organization.objects.get(subdomain=referer)

        user = request.user
        profile = Profile.objects.get(user=user)
        if organization and profile.organization == organization:
            return view_func(request, *args, **kwargs)
        else:
            return Response("", status.HTTP_404_NOT_FOUND)'''

    return wrap
