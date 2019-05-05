from django.urls import path

from main import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.my_register, name='register'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('restaurant/<int:res_id>', views.restaurant, name='restaurant'),
    path('vote_restaurants/<int:res_id>/<path:url>', views.vote_restaurant, name='vote_restaurant'),
    path('unvote_restaurants/<int:res_id>/<path:url>', views.unvote_restaurant, name='unvote_restaurant'),
    path('menus/', views.menus, name='menus'),
    path('menu/<int:menu_id>', views.menu, name='menu'),
    path('vote_menus/<int:menu_id>/<path:url>', views.vote_menu, name='vote_menu'),
    path('unvote_menus/<int:menu_id>/<path:url>', views.unvote_menu, name='unvote_menu'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('my_history/', views.my_history, name='my_history'),
    path('my_restaurant/', views.my_restaurant, name='my_restaurant'),
    path('update_my_restaurant/', views.update_my_restaurant, name='update_my_restaurant'),
    path('open_my_restaurant/', views.open_my_restaurant, name='open_my_restaurant'),
    path('close_my_restaurant/', views.close_my_restaurant, name='close_my_restaurant'),
    
    # path('login/', views.logIn, name='login'),
    # path('login/', views.logIn, name='login'),
    # path('login/', views.logIn, name='login'),
    # path('login/', views.logIn, name='login'),
    # path('login/', views.logIn, name='login'),
    # path('login/', views.logIn, name='login'),
    # path('login/', views.logIn, name='login'),
    # path('login/', views.logIn, name='login')

]
