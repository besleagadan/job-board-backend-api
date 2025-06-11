from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_application_email(company_email, candidate_name, job_title):
    subject = f"New application for {job_title}"
    message = f"{candidate_name} has applied to your job: {job_title}"
    send_mail(subject, message, 'no-reply@jobboard.com', [company_email])
