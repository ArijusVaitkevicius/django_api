from django.urls import path
from .views import BandList, AlbumList, SongList, AlbumReviewList, AlbumReviewCommentList, AlbumReviewLikeList

urlpatterns = [
    path('band', BandList.as_view()),
    path('album', AlbumList.as_view()),
    path('song', SongList.as_view()),
    path('album_review', AlbumReviewList.as_view()),
    path('album_review_comment', AlbumReviewCommentList.as_view()),
    path('album_review_like', AlbumReviewLikeList.as_view()),
]
