from django.urls import path

from .views import (
    home,
    workout_day,
    service_worker
)


urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "day/<int:day>/",
        workout_day,
        name="workout_day"
    ),

    path(
        "service-worker.js",
        service_worker,
        name="service_worker"
    ),

]