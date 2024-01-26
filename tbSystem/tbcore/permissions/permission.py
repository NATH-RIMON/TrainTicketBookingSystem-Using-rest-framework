from rest_framework.permissions import BasePermission
from tbauth.models.models import UserProfile


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        return False
    


class StationMasterUserAccess(BasePermission):
    def has_permission(self, request, view):
        user = request.user  
        if user.is_authenticated:
            profile_obj = UserProfile.objects.filter(user=user).first()
            if profile_obj and profile_obj.role == 'StationMaster':
                return True
        return False




class PassengerUserAccess(BasePermission):
    def has_permission(self, request, view):
        user = request.user  
        if user.is_authenticated:
            profile_obj = UserProfile.objects.filter(user=user).first()
            if profile_obj and profile_obj.role == 'Passenger':
                return True
        return False








