from django.contrib import admin

from .models import Students

# Most of us already have registered the models so for them just use decorators like @admin.register(ModelName)

# TODO: Let's add list_display , search fields and filter fields in our admin models


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    """this allows the admin to see the data instead of the object

    removing this will cause the DATA to be replaced by the object eg: Students.object(1)
    """

    list_display = (
        "name",
        "age",
        "email",
        "phone",
        "course",
        "is_active",
        "joined_date",
    )

    """this tells django to make these fields searchable 
    i.e admin can use these fields to search the data if there are huge amount of data 
    """
    search_fields = ("name", "email", "phone")

    """if we have a foreign key relationship we can use the  __ double underscrore which is django's lookup"""
    # search_fields=(
    #     "foreignkey__childkey"
    #     "students__course"
    # )

    """list filter works the similiar way but instead of searching we use the fields to filter the data"""
    list_filter = ("email", "age")
