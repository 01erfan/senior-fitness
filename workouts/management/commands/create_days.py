from django.core.management.base import BaseCommand

from workouts.models import DailyWorkout


class Command(BaseCommand):

    help = "ساخت روزهای ۱ تا ۳۰ برنامه تمرینی"

    def handle(self, *args, **kwargs):

        for day in range(1, 31):

            workout, created = DailyWorkout.objects.get_or_create(
                day=day
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"روز {day} ساخته شد."
                    )
                )
            else:
                self.stdout.write(
                    f"روز {day} از قبل وجود دارد."
                )

        self.stdout.write(
            self.style.SUCCESS(
                "تمام ۳۰ روز آماده شدند."
            )
        )