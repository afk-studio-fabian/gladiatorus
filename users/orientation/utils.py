from datetime import datetime
from .models import UserOrientation, UserOrientationTracker, UserOrientationLog
from django.utils import timezone

def switch_user_orientation(user, new_orientation):
    # Try to get the existing UserOrientation, if it doesn't exist, create a new one
    user_orientation, created = UserOrientation.objects.get_or_create(user=user, defaults={'orientation': new_orientation})
    
    # If UserOrientation was not created, that means it already exists, so handle switching
    if not created:
        # Handle the existing tracker
        try:
            current_tracker = UserOrientationTracker.objects.get(user_orientation=user_orientation, last_session_end__isnull=True)
            current_tracker.last_session_end = timezone.now()
            session_duration = current_tracker.last_session_end - current_tracker.last_session_start
            current_tracker.total_time_spent += session_duration
            current_tracker.save()
        except UserOrientationTracker.DoesNotExist:
            pass  # Handle this scenario appropriately, maybe log a warning or an error
        
        # Log the switch in UserOrientationLog
        orientation_log = UserOrientationLog(user=user, from_orientation=user_orientation.orientation, to_orientation=new_orientation)
        orientation_log.save()
        
        # Update UserOrientation to the new orientation
        user_orientation.orientation = new_orientation
        user_orientation.save()
        
    # Create a new tracker for the new or existing orientation
    new_tracker = UserOrientationTracker(user_orientation=user_orientation)
    new_tracker.save()

# def switch_user_orientation(user, new_orientation):
#     # Get the user's current orientation and tracker
#     try:
#         user_orientation = UserOrientation.objects.get(user=user)
#     except UserOrientation.DoesNotExist:
#         user_orientation = None  # Or handle it in some other appropriate way
#         user_orientation = UserOrientation.objects.create(user=user, orientation=new_orientation)
    
    
    
#     current_tracker = UserOrientationTracker.objects.get(user_orientation=user_orientation, last_session_end__isnull=True)
    
#     # End the current session and update the tracker
#     current_tracker.last_session_end = datetime.now()
#     session_duration = current_tracker.last_session_end - current_tracker.last_session_start
#     current_tracker.total_time_spent += session_duration
#     current_tracker.save()
    
#     # Log the switch in UserOrientationLog
#     orientation_log = UserOrientationLog(user=user, from_orientation=user_orientation.orientation, to_orientation=new_orientation)
#     orientation_log.save()
    
#     # Update UserOrientation and create a new tracker for the new orientation
#     user_orientation.orientation = new_orientation
#     user_orientation.save()
    
#     new_tracker = UserOrientationTracker(user_orientation=user_orientation)
#     new_tracker.save()
