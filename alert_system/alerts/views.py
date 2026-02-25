from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

from .models import Alert
from .serializers import AlertSerializer


class AlertViewSet(viewsets.ModelViewSet):

    queryset = Alert.objects.all()

    serializer_class = AlertSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Alert.objects.filter(
            tenant=self.request.user.tenant
        )

        severity = self.request.query_params.get('severity')
        status_param = self.request.query_params.get('status')

        if severity:
            queryset = queryset.filter(severity=severity)

        if status_param:
            queryset = queryset.filter(status=status_param)

        return queryset

    def perform_create(self, serializer):

        serializer.save(
            tenant=self.request.user.tenant
        )

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):

        alert = self.get_object()

        new_status = request.data.get('status')

        if new_status not in ['Open', 'In Progress', 'Closed']:
            return Response(
                {"error": "Invalid status"},
                status=400
            )

        alert.status = new_status
        alert.save()

        return Response(
            {"message": "Status updated successfully"}
        )


class DashboardViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):

        tenant = request.user.tenant

        alerts = Alert.objects.filter(tenant=tenant)

        total = alerts.count()

        severity_counts = alerts.values('severity').annotate(
            count=Count('severity')
        )

        return Response({
            "total_alerts": total,
            "severity_breakdown": severity_counts
        })