"""
Serializers for RECIPE APIUSs
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipes"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serialzier for recipe detail views"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
