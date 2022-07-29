from django.urls import path
from foroum import views

app_name = 'foroum'

urlpatterns = [
	path(
		'room-list/',
		views.RoomListView.as_view(),
		name='room_list',
	),
	path(
		'room-detail/<pk>/',
		views.RoomDetailView.as_view(),
		name='room_detail',
	),
]

# dar mored view set ha search konid --> dynamic routing