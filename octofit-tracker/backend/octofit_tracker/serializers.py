from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'team']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'type', 'duration', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'points']
