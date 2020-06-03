from . import views
# from django.conf.urls import url
from django.conf.urls import include, url
from django.urls import path, include  # add this
from .views import searchposts, BootstrapFilterView


app_name = "reward"


urlpatterns = [

    url('^$', views.index, name="RemList"),

    path('Profile', views.profileview, name="Profile"),
    path('about', views.about_rewardview, name="About"),
    path('blind_reward', views.blind_rewardview, name="Blind Reward"),
    path('flexible_work', views.flexible_workview, name="Flexible Work"),
    # path('reward_form', RewardFormView.as_view(), name='Reward Form'),
    # url(r'^search/$', views.search, name='search'),
    # url(r'^$', searchposts, name='searchposts'),
    path('searchposts', searchposts, name="searchposts"),
    path('benefits', views.benefitsview, name="Benefits"),
    # path('reward_proposal', views.reward_proposal, name="Reward Proposal"),
    # path('reward_proposal', views.RemFilterView, name="Reward Proposal"),
    # url(r'^search/$', views.search, name='search'),
    # path('rem/<str:pk_test>/', views.reward_proposal, name="rem"),
    path('reward_form', BootstrapFilterView, name='bootstrap'),




]

