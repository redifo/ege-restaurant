from django.db import models



class Email(models.Model):
    """
    model represents individual emails to be sent
    """
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    TEMPLATE_CHOICES = [
        ('APPROVED', 'Approved'),
        ('WAITING_APPROVAL', 'Waiting_approval'),
    ]
    
    template = models.CharField(max_length=50, choices=TEMPLATE_CHOICES)
    class Meta:
        db_table = 'email'

    def __str__(self):
        return f"Email to {self.recipient}"

