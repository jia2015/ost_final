from django.conf.urls import patterns, include, url
from django.contrib.syndication.views import Feed
from django.contrib import admin
from questionAnswerSite.models import Questions
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'questionAnswerSite.views.home', name='home'),
    url(r'^about/', 'questionAnswerSite.views.about', name='about'),
    url(r'^review/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.question', name='question'),
    url(r'^reviews/add', 'questionAnswerSite.views.add_review', name='add_review'),

    url(r'^reviews/(?P<count>\w{0,256})$', 'questionAnswerSite.views.reviews', name='reviews'),
    url(r'^reviews/', 'questionAnswerSite.views.reviews', name='reviews'),
    url(r'^my_question/', 'questionAnswerSite.views.my_question', name='my_question'),

    url(r'^my_answers/', 'questionAnswerSite.views.my_answers', name='my_answers'),
  #  url(r'^answer/add', 'questionAnswerSite.views.add_answer', name='add_answer'),

    url(r'^modify_question/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.modify_question', name='modify_question'),
    url(r'^modify_question_act', 'questionAnswerSite.views.modify_question_act', name='modify_question_act'),
    url(r'^delete_question/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.delete_question', name='delete_question'),
    
    url(r'^add_answer_page/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.add_answer_page', name='add_answer_page'),
    url(r'^add_answer/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.add_answer', name='add_answer'),

    url(r'^modify_answer/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.modify_answer', name='modify_answer'),
    url(r'^modify_answer_act', 'questionAnswerSite.views.modify_answer_act', name='modify_answer_act'),
    url(r'^delete_answer/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.delete_answer', name='delete_answer'),
    url(r'^per_ans/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.per_ans', name='per_ans'),
    url(r'^per_quest/(?P<identifier>\w{0,256})/$', 'questionAnswerSite.views.per_quest', name='per_quest'),

    
    url(r'^vote/(?P<identifier>\w{0,256})-(?P<voteVal>\w{0,1})-(?P<type>\w.+)$', 'questionAnswerSite.views.vote', name='vote'),

    url(r'^add_pic/', 'questionAnswerSite.views.add_pic', name='add_pic'),
    url(r'^delete_img/(?P<blobKey>.+)$', 'questionAnswerSite.views.delete_img', name='delete_img'),

    url(r'^list_all_img/', 'questionAnswerSite.views.list_all_img', name='list_all_img'),


    url(r'^feed/', "questionAnswerSite.views.index", name='index')

    #url(r'^admin/', include(admin.site.urls)),
)
