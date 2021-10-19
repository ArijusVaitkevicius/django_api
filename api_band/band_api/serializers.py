from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'band_id']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'album_id']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album_id', 'content', 'score']


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'album_review_id', 'content']


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'user_id', 'album_review_id']

