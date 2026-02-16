
from django.core.management.base import BaseCommand
from octofit_tracker import models
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        models.Team.objects.all().delete()
        models.User.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Workout.objects.all().delete()
        models.Leaderboard.objects.all().delete()

        # Create teams
        marvel = models.Team.objects.create(name='Team Marvel', description='Marvel superheroes')
        dc = models.Team.objects.create(name='Team DC', description='DC superheroes')

        # Create users (superheroes)
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel, 'is_superhero': True},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel, 'is_superhero': True},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc, 'is_superhero': True},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': dc, 'is_superhero': True},
        ]
        user_objs = []
        for u in users:
            user = models.User.objects.create(**u)
            user_objs.append(user)

        # Create activities
        activities = [
            {'user': user_objs[0], 'activity_type': 'run', 'duration': 30, 'date': date.today()},
            {'user': user_objs[1], 'activity_type': 'cycle', 'duration': 45, 'date': date.today()},
            {'user': user_objs[2], 'activity_type': 'swim', 'duration': 60, 'date': date.today()},
            {'user': user_objs[3], 'activity_type': 'run', 'duration': 25, 'date': date.today()},
        ]
        for a in activities:
            models.Activity.objects.create(**a)

        # Create workouts
        workouts = [
            {'name': 'Morning Cardio', 'description': 'Cardio for all'},
            {'name': 'Strength Training', 'description': 'Strength for all'},
        ]
        for w in workouts:
            models.Workout.objects.create(**w)

        # Create leaderboard (team-based)
        models.Leaderboard.objects.create(team=marvel, total_points=180)
        models.Leaderboard.objects.create(team=dc, total_points=210)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
