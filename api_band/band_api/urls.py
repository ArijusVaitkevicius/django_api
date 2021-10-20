from django.urls import path
from .views import BandList, AlbumList, SongList, AlbumReviewList, AlbumReviewCommentList, AlbumReviewLikeList, \
    BandDetail, AlbumDetail, SongDetail, AlbumReviewDetail, AlbumReviewCommentDetail, AlbumReviewLikeDetail

urlpatterns = [
    path('band', BandList.as_view()),
    path('album', AlbumList.as_view()),
    path('song', SongList.as_view()),
    path('album/<int:pk>/album_review', AlbumReviewList.as_view()),
    path('album_review_comment', AlbumReviewCommentList.as_view()),
    path('album_review_like', AlbumReviewLikeList.as_view()),
    path('band/<int:pk>', BandDetail.as_view()),
    path('album/<int:pk>', AlbumDetail.as_view()),
    path('song/<int:pk>', SongDetail.as_view()),
    path('album_review/<int:pk>', AlbumReviewDetail.as_view()),
    path('album_review_comment/<int:pk>', AlbumReviewCommentDetail.as_view()),
    path('album_review_like/<int:pk>', AlbumReviewLikeDetail.as_view()),
]
