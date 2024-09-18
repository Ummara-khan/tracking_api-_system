import random
import string
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TrackingNumber
from rest_framework import status
from django.db import IntegrityError

def generate_tracking_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

class NextTrackingNumber(APIView):
    def get(self, request):
        origin_country_id = request.query_params.get('origin_country_id')
        destination_country_id = request.query_params.get('destination_country_id')
        weight = request.query_params.get('weight')
        created_at = request.query_params.get('created_at', now())
        customer_id = request.query_params.get('customer_id')
        customer_name = request.query_params.get('customer_name')
        customer_slug = request.query_params.get('customer_slug')

        # Validate required fields
        if not all([origin_country_id, destination_country_id, weight, customer_id, customer_name, customer_slug]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Generate unique tracking number
            tracking_number = generate_tracking_number()
            tracking = TrackingNumber.objects.create(
                tracking_number=tracking_number,
                origin_country_id=int(origin_country_id),
                destination_country_id=int(destination_country_id),
                weight=float(weight),
                customer_id=int(customer_id),
                customer_name=customer_name,
                customer_slug=customer_slug
            )

            response_data = {
                "tracking_number": tracking.tracking_number,
                "created_at": tracking.created_at.strftime('%Y-%m-%dT%H:%M:%S%z'),
                "origin_country_id": tracking.origin_country_id,
                "destination_country_id": tracking.destination_country_id,
                "weight": tracking.weight,
                "customer_id": tracking.customer_id,
                "customer_name": tracking.customer_name,
                "customer_slug": tracking.customer_slug
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "Failed to generate unique tracking number"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
