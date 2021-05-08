"""Circle views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

# Permissions
from cride.circles.permissions.circles import IsCircleAdmin

# Serializers
from cride.circles.serializers import CircleModelSerializer

# Models
from cride.circles.models import Circle, Membership


class CircleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""

    serializer_class = CircleModelSerializer
    lookup_field = 'slug_name'  

    def get_queryset(self):
        """Restrict list to public-only"""
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def get_permissions(self):
        """Assing permissions based on action"""
        permission = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permission]

    def perform_create(self, serializer):
        """Assing circle admin"""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_inviation=10
        )