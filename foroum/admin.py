from django.contrib import admin
from foroum.models import (
	Room, Post, Comment, Like
)


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

class RoomAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title', )}


admin.site.register(Room, RoomAdmin)