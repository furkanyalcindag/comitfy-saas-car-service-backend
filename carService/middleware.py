import re

from rest_framework import status
from rest_framework.response import Response

from carService.models import Profile
from carService.models.Organization import Organization


class OrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if re.search('/public-api/', request.path):
            return self.get_response(request)
        else:
            referer = request.META.get('HTTP_REFERER')
            if not referer:
                return None
            # remove the protocol and split the url at the slashes
            referer = re.sub('^https?:\/\/', '', referer).split('/')
            referer = re.sub('www.', '', referer[0])

            organization = Organization.objects.get(subdomain=referer)

            user = request.user
            profile = Profile.objects.get(user=user)
            if organization and profile.organization != organization:
                return Response("", status.HTTP_404_NOT_FOUND)

            response = self.get_response(request)

            # Code to be executed for each request/response after
            # the view is called.

            return response
