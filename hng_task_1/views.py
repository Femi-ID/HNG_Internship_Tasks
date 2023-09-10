from django.views.decorators.http import require_GET
from django.http import JsonResponse
from _datetime import datetime
import pytz


@require_GET
def get_info(request):
    # retrieve request get parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # get current day and time
    current_day = datetime.now().strftime('%A')
    utc_time = datetime.now()
    utc_localize = pytz.utc.localize(utc_time)

    # github repo and file url
    github_repo_url = "https://github.com/Femi-ID/HNG_Internship_Tasks"
    github_file_url = "https://github.com/Femi-ID/HNG_Internship_Tasks/blob/master/hng_tasks_1/views.py"

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_localize,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    response = JsonResponse(data)
    return response




