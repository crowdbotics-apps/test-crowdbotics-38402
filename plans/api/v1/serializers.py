from rest_framework import serializers
from plans.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=5, decimal_places=2, )

    class Meta:
        model = Plan
        fields = "__all__"
