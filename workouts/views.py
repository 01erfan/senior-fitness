from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import DailyWorkout


def home(request):

    days = range(1, 31)

    return render(
        request,
        "workouts/home.html",
        {
            "days": days
        }
    )


def workout_day(request, day):

    workout = get_object_or_404(
        DailyWorkout,
        day=day
    )

    workout_exercises = (
        workout.workout_exercises
        .select_related("exercise")
        .all()
    )

    exercise_data = []

    for item in workout_exercises:

        exercise_data.append({

            "name": item.exercise.name,

            "description": item.exercise.description,

            "duration": item.exercise.duration,

            "repetitions": item.exercise.repetitions,

            "sets": item.exercise.sets,

            "rest": item.exercise.rest,

            "difficulty":
                item.exercise.get_difficulty_display(),

            "image": (
                item.exercise.image.url
                if item.exercise.image
                else ""
            ),

            "video": (
                item.exercise.video.url
                if item.exercise.video
                else ""
            ),

        })

    return render(
        request,
        "workouts/workout_day.html",
        {
            "day": day,
            "exercise_data": exercise_data,
        }
    )


def service_worker(request):

    sw_code = """
const CACHE_NAME = "senior-fitness-v2";

const APP_SHELL = [
    "/",
    "/static/pwa/manifest.json",
    "/static/pwa/icon-192.png",
    "/static/pwa/icon-512.png"
];


// نصب Service Worker
self.addEventListener("install", event => {

    event.waitUntil(

        caches.open(CACHE_NAME)
            .then(cache => {

                return cache.addAll(APP_SHELL);

            })

    );

    self.skipWaiting();

});


// فعال شدن Service Worker
self.addEventListener("activate", event => {

    event.waitUntil(

        caches.keys().then(keys => {

            return Promise.all(

                keys
                    .filter(key => key !== CACHE_NAME)
                    .map(key => caches.delete(key))

            );

        })

    );

    self.clients.claim();

});


// درخواست‌های صفحه و فایل‌ها
self.addEventListener("fetch", event => {

    const request = event.request;

    // فقط درخواست‌های GET
    if (request.method !== "GET") {
        return;
    }


    event.respondWith(

        fetch(request)

            .then(response => {

                // فقط پاسخ معتبر را ذخیره کن
                if (
                    response &&
                    response.status === 200
                ) {

                    const responseClone =
                        response.clone();

                    caches.open(CACHE_NAME)
                        .then(cache => {

                            cache.put(
                                request,
                                responseClone
                            );

                        });

                }

                return response;

            })

            .catch(() => {

                return caches.match(request)
                    .then(cachedResponse => {

                        if (cachedResponse) {

                            return cachedResponse;

                        }

                        // اگر صفحه در کش نبود
                        if (
                            request.mode === "navigate"
                        ) {

                            return caches.match("/");

                        }

                    });

            })

    );

});
"""

    response = HttpResponse(
        sw_code,
        content_type="application/javascript"
    )

    response["Service-Worker-Allowed"] = "/"

    return response

    response = HttpResponse(
        sw_code,
        content_type="application/javascript"
    )

    response["Service-Worker-Allowed"] = "/"

    return response