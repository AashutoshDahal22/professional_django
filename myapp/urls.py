from django.urls import path
from myapp import views
from . import views 

urlpatterns=[

    path("<int:id>/",views.home_with_dynamicURL,name="dynamic_home"),
    
    path("",views.home,name="home"),
    
    path("welcome/",views.welcome), #map
    
    path("about/",views.about),
    
    path("contact/",views.contact),
    
    path("student/",views.student),
        
]