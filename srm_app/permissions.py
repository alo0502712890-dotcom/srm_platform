from .models import Profile

def is_manager(user):
    return (
        user.is_authenticated
        and hasattr(user, 'profile')
        and user.profile.role == Profile.ROLL_MANAGER
    )

def is_employee(user):
    return (
        user.is_authenticated
        and hasattr(user, 'profile')
        and user.profile.role == Profile.ROLL_EMPLOYEE
    )