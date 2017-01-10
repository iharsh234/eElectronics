from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Paper
from .models import Likes
from .models import LikeUnlike


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
admin.site.register(Paper)
admin.site.register(Likes)
admin.site.register(LikeUnlike)
