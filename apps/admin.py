from django.contrib import admin
from .models import TeamMember,New_Update,Course_Category,Popular_Course,Student_testimonial,Course_gallery,Service,Message,User_Testimonial,Direct_Service,LogoLink


# Register your models here.

admin.site.site_header = "EME Admin Panel"
admin.site.site_title = "Eben-ezerimindeducation"
admin.site.index_title = "Karibu Eben-ezerimindeducation Admin Site"


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation', 'created_at')
    search_fields = ('full_name',)


@admin.register(New_Update)
class NewUpdateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation', 'date')
    list_filter = ('designation',)
    search_fields = ('full_name',)


@admin.register(Course_Category)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('Course_type', 'Total_courses')
    search_fields = ('Course_type',)


@admin.register(Popular_Course)
class PopularCourseAdmin(admin.ModelAdmin):
    list_display = ('Course_name', 'Student_enroll', 'Price')
    search_fields = ('Course_name',)


@admin.register(Student_testimonial)
class StudentTestimonialAdmin(admin.ModelAdmin):
    list_display = ('Student_name', 'Profession')
    search_fields = ('Student_name',)


@admin.register(Course_gallery)
class CourseGalleryAdmin(admin.ModelAdmin):
    list_display = ('image_name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Title',)
    search_fields = ('Title',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject')
    search_fields = ('full_name', 'email')


@admin.register(User_Testimonial)
class UserTestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)


@admin.register(Direct_Service)
class DirectServiceAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'service_type', 'phone_number')
    search_fields = ('full_name', 'email')


@admin.register(LogoLink)
class LogoLinkAdmin(admin.ModelAdmin):
    list_display = ('show_admin_link',)

