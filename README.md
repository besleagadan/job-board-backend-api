# job-board-backend-api


🚀 Project Roadmap
✅ Phase 1: Project Setup

    Docker + Docker Compose configured

    PostgreSQL and Redis containers added

    Django project created

    Connected to PostgreSQL

✅ Phase 2: Auth System

    Custom user model with roles: company, candidate

    JWT login and token refresh endpoints

    Register new users by role

✅ Phase 3: Job Posting

    Companies can post, update, delete jobs

    Candidates and visitors can view job listings

    Company ownership is enforced on create/update/delete

    JWT protected endpoints for posting

    Public job listing available

✅ Phase 4: Apply to Jobs

    Candidates can apply to jobs (once per job)

    Companies can view applications to their jobs

    Authenticated access only

    Smart filtering: candidates see theirs, companies see theirs

    Protected via JWT and role permissions

✅ Phase 5: Bookmarking

    Candidates can bookmark jobs

    View all their saved jobs

    Remove bookmarks

    Protected via JWT and candidate-only access

✅ Phase 6: Job Search and Filter

    Filter jobs by location, salary, and job type

    Search jobs by title or description

    Built with django-filter and DRF SearchFilter

    Multiple filters can be combined in a single query

✅ Phase 7: Email Notification with Celery + Redis

    When candidates apply, companies receive an email

    Uses Celery + Redis to run async background task

    Console email for development

    Ready for SMTP setup in production

✅ Phase 8: Testing

    pytest with pytest-django for all tests

    Covers user registration, job posting, application, bookmarks

    Simple, clean, readable test code

    Run via docker-compose exec backend pytest

    Coverage ready
    