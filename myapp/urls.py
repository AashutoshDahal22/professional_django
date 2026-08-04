from django.urls import path
from myapp import views
from . import views 

# urlpatterns=[
#     path("yourroutename/",views.yourfunctionname)
# ]

urlpatterns=[

    path("",views.home,name="home"),
    
    path("welcome/",views.welcome), #map
    
    path("about/",views.about),
    
    path("contact/",views.contact),
    
    path("student/",views.student)
    
    # #dynamic urls
    # path("student/<int:id>/",views.student),
    
    # #dynamic urls with multiple parameters or parameter url
    # path("student-info/<int:id>/<str:name>/",views.student_info),
    
    # path("search/", views.search),
    
    # path("login/",views.login),
    
    # path("login-class",views.LoginView.as_view(),name="login-class")
    
]