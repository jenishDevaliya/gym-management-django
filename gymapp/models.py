from django.db import models


from django.contrib.auth.models import AbstractUser
# Import AbstractUser for custom user model
from django.utils import timezone
# Import timezone for date fields
from django.conf import settings 
# Import settings to access AUTH_USER_MODEL

class User(AbstractUser): #username, email, password, first_name, last_name are inherited from AbstractUser
    # Custom user model extending AbstractUser
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MEMBER', 'Member'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='MEMBER')

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    duration_months = models.PositiveIntegerField() #e.g., 1, 3, 6, 12 monts
    fee = models.DecimalField(max_digits=6, decimal_places=2) #e.g., 4549.99
    description = models.TextField(blank=True)
   

    def __str__(self):
        return f"{self.name} - {self.duration_months} months - ${self.fee}"
    
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    # mobile = models.BigIntegerField()
    specialization = models.CharField(max_length=200)
    shift_timing = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name} - {self.specialization}" 

# 11 fields
class MemberProfile(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, # Delete profile if user is deleted
        related_name='member_profile' # Access prlofile via user.member_profile
    )

    full_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.TextField(blank=True)
    join_date = models.DateField(default=timezone.now)
    
    plan = models.ForeignKey(
        MembershipPlan, on_delete=models.SET_NULL, # If plan is deleted, set to null
        null=True, blank=True, 
        related_name='members'  # Access members via plan.members 
        ) 
    trainer = models.ForeignKey(
        Trainer, on_delete=models.SET_NULL, # If trainer is deleted, set to null
        null=True, blank=True, 
        related_name='members'  # Access members via trainer.members 
        )
    membership_start = models.DateField(null=True, blank=True)
    membership_end = models.DateField(null=True, blank=True)

def __str__(self):
    return f"{self.full_name} - {self.user.username}"

# 5 fields 
class Equipment(models.Model):
    name = models.CharField(max_length=100) #e.g., Treadmill, Dumbbells, etc.
    units = models.PositiveIntegerField(default=1) # e.g., 5 treadmills, 10 dumbbells, etc.
    price = models.DecimalField(max_digits=8, decimal_places=2) # e.g., 1500.00
    purchase_date = models.DateField(default=timezone.now) # Date when equipment was purchased
    is_active = models.BooleanField(default=True) # if removed/sold, mark as inactive instead of deleting record
    
    
    def __str__(self):
        return f"{self.name} (Units: {self.units})"

# 7 fields

class Payment(models.Model):
    PAYMENT_MODE_CHOICES = (
        ('CASH', 'Cash'),
        ('ONLINE', 'Online'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('PAID', 'Paid'),
        ('PENDING', 'Pending'),
    )
    member = models.ForeignKey(
        MemberProfile,on_delete=models.CASCADE, # If member is deleted, delete payment records
        related_name='payments' # Access payments via member.payments

    ) 
    plan = models.ForeignKey(
        MembershipPlan, on_delete=models.SET_NULL, # If plan is deleted, set to null
        null=True, blank=True, 
        related_name='payments'  # Access payments via plan.payments 
        )
    amount = models.DecimalField(max_digits=8, decimal_places=2) # e.g., 4549.99
    payment_date = models.DateField(default=timezone.now) # Date when payment was made
    mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES) # e.g., Credit Card, Cash, etc.
    status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)
    notes = models.TextField(blank=True) # Optional field for any additional notes about the payment

    def __str__(self):
        return f"Payment of ${self.amount} by {self.member.full_name} on {self.payment_date}" 
    
# 3 fields
class Attendance(models.Model):
    member = models.ForeignKey(
        MemberProfile, on_delete=models.CASCADE, # If member is deleted, delete attendance records
        related_name='attendances' # Access attendance via member.attendance_records
    )
    date = models.DateField(default=timezone.now) # Date of attendance
    time_in = models.TimeField(null=True, blank=True) # Time when member checked in

    class Meta:
        unique_together = ('member', 'date') # Ensure one attendance record per member per day

    def __str__(self):
        return f"Attendance for {self.member.full_name} on {self.date}: {self.time_in}"  

# 6 fields
class Enquiry(models.Model):
    ENQUIRY_STATUS_CHOICES = (
        ('NEW', 'New'),
        ('SEEN', 'Seen'),
        ('RESOLVED', 'Resolved'),
    )
    status = models.CharField(max_length=20, choices=ENQUIRY_STATUS_CHOICES, default='PENDING')

    name = models.CharField(max_length=100) # Name of the person making the enquiry
    email = models.EmailField() # Email address of the enquirer
    mobile = models.BigIntegerField() # Mobile number of the enquirer
    message = models.TextField() # The enquiry message
    created_at = models.DateTimeField(auto_now_add=True) # Date and time when the enquiry was made
    status = models.CharField(max_length=20, choices=ENQUIRY_STATUS_CHOICES, default='NEW') # Status of the enquiry (e.g., New, Seen, Resolved)

def __str__(self):
    return f"Enquiry from {self.name} - {self.email} - Status: {self.status}"  
    
# 4 fields
class WorkoutPlan(models.Model):
    
    member = models.ForeignKey(
        MemberProfile, on_delete=models.CASCADE, # If member is deleted, delete workout plans
        related_name='workout_plans' # Access workout plans via member.workout_plans
    )
    title = models.CharField(max_length=100) # Name of the workout plan (e.g., "Beginner Full Body", "Advanced Cardio", etc.)
    description = models.TextField(blank=True) # Description of the workout plan
    created_at = models.DateTimeField(auto_now_add=True) # Date and time when the workout plan was created
   

    def __str__(self):
        return f"{self.title} - Created at: {self.created_at}"   
    
class Feedback(models.Model):
    member = models.ForeignKey(
        MemberProfile, on_delete=models.CASCADE, # If member is deleted, delete feedback records
        related_name='feedbacks' # Access feedback via member.feedbacks
    )
    message = models.TextField() # Feedback message from the member
    created_at = models.DateTimeField(auto_now_add=True) # Date and time when the feedback was submitted

    def __str__(self):
        return f"Feedback from {self.member.full_name} - Created at: {self.created_at}"    
