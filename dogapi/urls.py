#dogapi\urls.py
from django.urls import path
from .views import DogList, DogDetail, BreedList, BreedDetail

'''this was probably the more confusing part. It's a URL that points to URLS similar to how we did in ISQA3900
you can point the main application URL to look at the other url.py and use those, or just have ONE huge URL.py'''
urlpatterns = [
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
]
