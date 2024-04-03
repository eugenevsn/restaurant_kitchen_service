from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    """View function for home page"""

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)
