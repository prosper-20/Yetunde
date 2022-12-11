from rest_framework import serializers
from MAIN.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = "__all__"