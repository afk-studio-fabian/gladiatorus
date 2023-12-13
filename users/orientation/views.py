from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Orientation, UserOrientation, UserOrientationTracker, UserOrientationLog
from datetime import datetime
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from .utils import switch_user_orientation

# Create your views here.

def set_orientation(request):
    if request.method == "POST":
        selected_orientation_id = request.POST.get('selected_orientation')
        selected_orientation = Orientation.objects.get(id=selected_orientation_id)
        
        switch_user_orientation(request.user, selected_orientation)
        
        return redirect('core:home')
    else:
        orientations = Orientation.objects.all()
        return render(request, 'set_orientation.html', {'orientations': orientations})



class SetOrientationView(View):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        # new_orientation = data.get('orientation')
        
        # # Perform the logic to set the new orientation here.
        # # For example, create or update UserOrientation object, etc.
        
        # return JsonResponse({'success': True, 'message': 'Orientation updated successfully.'})

        new_orientation_id = data.get('selected_orientation')

        # Validate the orientation ID
        try:
            orientation = Orientation.objects.get(pk=new_orientation_id)
        except Orientation.DoesNotExist:
            return HttpResponseBadRequest('Invalid orientation ID.')

        # Update the orientation for the user
        try:
            switch_user_orientation(request.user, orientation)
        except Exception as e:  # Catch any exception that might arise from the helper function
            return JsonResponse({'success': False, 'message': str(e)})

        # Fetch updated UserOrientation
        user_orientation = UserOrientation.objects.get(user=request.user)
        # Return success response
        #return JsonResponse({'success': True, 'message': 'Orientation updated successfully.'})

        return JsonResponse({
            'success': True,
            'message': 'Orientation updated successfully.',
            'name': user_orientation.orientation.name,
            'iconUrl': user_orientation.orientation.icon.url,
            'bannerUrl': user_orientation.orientation.banner_image.url
        })
    
# def set_orientation(request):
#     if request.method == 'POST':
#         role = request.POST.get('role')
#         orientation, created = Orientation.objects.get_or_create(user=request.user)
#         orientation.role = role
#         orientation.save()
#         return redirect('core:home') # Redirect to a suitable view after setting the orientation
    
#     return render(request, 'set_orientation.html', {'roles': Orientation.ROLE_CHOICES})


# @login_required
# def set_orientation(request):
#     if request.method == "POST":
#         # Get the selected orientation
#         selected_orientation_id = request.POST.get('selected_orientation')
#         selected_orientation = Orientation.objects.get(id=selected_orientation_id)
        
#         # Get the user's current orientation and tracker
#         user_orientation = UserOrientation.objects.get(user=request.user)
#         current_tracker = UserOrientationTracker.objects.get(user_orientation=user_orientation, last_session_end__isnull=True)
        
#         # End the current session and update the tracker
#         current_tracker.last_session_end = datetime.now()
#         session_duration = current_tracker.last_session_end - current_tracker.last_session_start
#         current_tracker.total_time_spent += session_duration
#         current_tracker.save()
        
#         # Log the switch in UserOrientationLog
#         orientation_log = UserOrientationLog(user=request.user, from_orientation=user_orientation.orientation, to_orientation=selected_orientation)
#         orientation_log.save()
        
#         # Update UserOrientation and create a new tracker for the new orientation
#         user_orientation.orientation = selected_orientation
#         user_orientation.save()
        
#         new_tracker = UserOrientationTracker(user_orientation=user_orientation)
#         new_tracker.save()
        
#         return redirect('some_view')  # Redirect to a view, possibly a dashboard or a home page
    
#     else:
#         # Display all available orientations
#         orientations = Orientation.objects.all()
#         return render(request, 'set_orientation.html', {'orientations': orientations})