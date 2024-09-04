from django.shortcuts import render, get_object_or_404
from projects.models import (Profile,
                             Project,
                             Certificate,
                             CertifyingInstitution)
from projects.serializer import (ProfileSerializer,
                                 ProjectSerializer,
                                 CertificateSerializer,
                                 CertifyingInstitutionSerializer)
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
        certificates = Certificate.objects.filter(
            profiles=profile).select_related('certifying_institution')
        projects = profile.projects.all()

        context = {
            'profile': profile,
            'certificates': certificates,
            'projects': projects,
        }

        return render(request, 'profile_detail.html',
                      context)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
