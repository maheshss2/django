from django.http import JsonResponse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        """Initialize the middleware with the next callable response."""
        self.get_response = get_response

    def __call__(self, request):
        """Handle requests and apply role-based access control."""
        # Allow unauthenticated access to specific paths
        if (
            request.path.startswith('/auth/login/') or
            request.path.startswith('/auth/logout/') or
            request.path.startswith('/admin/login/')
        ):
            return self.get_response(request)

        # Allow authenticated users with specific roles
        if request.user.is_authenticated:
            # Check user roles (assuming `is_staff` for admins and `is_student` for students)
            if getattr(request.user, 'is_staff', False):  # Admins
                return self.get_response(request)
            if getattr(request.user, 'is_student', False):  # Students
                return self.get_response(request)

            # Deny access if user role is not authorized
            return JsonResponse({'error': 'Forbidden: Role not authorized'}, status=403)

        # Block unauthenticated users
        return JsonResponse({'error': 'Unauthorized'}, status=401)
