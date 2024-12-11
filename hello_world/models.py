from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class user(AbstractUser):  # Renamed to PascalCase
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=50)
    cpf = models.CharField(max_length=14, unique=True)  # Brazilian CPF format
    institution = models.CharField(max_length=255, blank=True, null=True)
    titles = models.TextField(blank=True, null=True)
    skillsets = models.TextField(blank=True, null=True)
    rank = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'  # Email will be used as the username
    REQUIRED_FIELDS = ['username', 'nome', 'cpf']
class Project(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_open_source = models.BooleanField(default=False)
    functionalities = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
class Whiteboard(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="whiteboards")
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
class Timer(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE, related_name="timers")
    timer_type = models.CharField(max_length=50, choices=[
        ("Pomodoro", "Pomodoro"), 
        ("Stopwatch", "Stopwatch"), 
        ("Countdown", "Countdown")])
    duration = models.PositiveIntegerField() # devera ser em segundos
    state = models.CharField(max_length=50, choices=[
        ("Running", "Running"), 
        ("Paused", "Paused"), 
        ("Stopped", "Stopped")])
class Reminder(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE, related_name="reminders")
    message = models.TextField()
    timer = models.ForeignKey(Timer, on_delete=models.CASCADE, related_name="timer_reminders")
    reminder_time = models.DateTimeField()
class TaskList(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="task_lists")
    name = models.CharField(max_length=255)
class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=255)  
    is_checked = models.BooleanField(default=False)  
    editable = models.BooleanField(default=True)  
    deletable = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True) #auto now add seleciona o tempo no momento exato