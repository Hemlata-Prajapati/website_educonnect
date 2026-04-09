from django.db import models
from accounts.models import User
from faculty.models import Assignment

class AssignmentSubmission(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("submitted", "Submitted"),
        ("graded", "Graded"),
    ]
    answers = models.TextField(null=True, blank=True)

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    file = models.FileField(upload_to='submissions/', null=True, blank=True)

    marks = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    submitted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['student', 'assignment']   # 🔥 VERY IMPORTANT