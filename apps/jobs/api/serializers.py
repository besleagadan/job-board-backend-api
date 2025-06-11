from rest_framework import serializers
from apps.jobs.models import Job, JobApplication, JobBookmark

class JobSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)
    job_type = serializers.CharField(source='get_job_type_display', read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['company', 'created_at']


class JobApplicationSerializer(serializers.ModelSerializer):
    candidate = serializers.StringRelatedField(read_only=True)
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())

    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['candidate', 'applied_at']
        
        
class JobBookmarkSerializer(serializers.ModelSerializer):
    candidate = serializers.StringRelatedField(read_only=True)
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())

    class Meta:
        model = JobBookmark
        fields = '__all__'
        read_only_fields = ['candidate', 'bookmarked_at']