from django.contrib import admin
from user_profile.models import AppUser

class AppUserAdmin(UserAdmin):
	form = CustomUserChangeForm
	add_form = CustomUserCreationForm
	
	list_display = ('username', 'email', 'is_staff','is_superuser')
	list_filter = ('is_superuser')

	fieldsets = (
		(None,{'fields': ('username','email','password','first_name',
			'last_name','group','date_joined_epoch','location')}),
		('Permissions',{'fields':('is_active','is_superuser','is_staff')}),
		)
	search_field = ('email','username')
	ordering = ('email',')
	filter_horizontal = ('groups','user_permissions',)
					
admin.site.register(AppUser,AppUserAdmin) 

