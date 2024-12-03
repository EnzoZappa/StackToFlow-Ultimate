from django.db import models

class Brainstorm(models.Model):
    prompt = models.TextField()
    generated_prompt = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt[:50]