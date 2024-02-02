from django . urls import path
from . import views,admin_views,nurse_views,user_views

urlpatterns=[
     path('',views.index,name='index'),
    # path('create/',views.create,name='create'),
    path('login_view/',views.login_view,name='login_view'),
    path('user_reg/',views.user_reg,name='user_reg'),
    path('nurse_reg/',views.nurse_reg,name='nurse_reg'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('userpage/',views.userpage,name='userpage'),
    path('nursepage/',views.nursepage,name='nursepage'),
    path('logout_view/', views.login_view, name='logout_view'),

    path('nurse_update/<int:update>',admin_views.nurse_update,name='nurse_update'),
    path('nurse_delete/<int:delete>',admin_views.nurse_delete,name='nurse_delete'),
    path('nurse_view',admin_views.nurse_view,name='nurse_view'),

    path('user_update/<int:update>',admin_views.nurse_update,name='user_update'),
    path('user_delete/<int:delete>',admin_views.user_delete,name='user_delete'),
    path('user_view',admin_views.user_view,name='user_view'),

    path('hospital/',admin_views.hospital,name='hospital'),
    path('hospital_view', admin_views.hospital_view, name='hospital_view'),
    path('hospital_update/<int:update>', admin_views.hospital_update, name='hospital_update'),
    path('hospital_delete/<int:delete>', admin_views.hospital_delete, name='hospital_delete'),

    path('vaccine/',admin_views.vaccine,name='vaccine'),
    path('vaccine_view', admin_views.vaccine_view, name='vaccine_view'),
    path('vaccine_update/<int:update>', admin_views.vaccine_update, name='vaccine_update'),
    path('vaccine_delete/<int:delete>', admin_views.vaccine_delete, name='vaccine_delete'),


    path('complaint_viewall/',admin_views.complaint_viewall,name='complaint_viewall'),
    path('reply_complaints/<int:id>',admin_views.reply_complaints,name='reply_complaints'),

    path('vaccine_viewn/',nurse_views.vaccine_viewn,name='vaccine_viewn'),


    path('user_viewn/',nurse_views.user_viewn,name='user_viewn'),


    path('hospital_viewn/',nurse_views.hospital_viewn,name='hospital_viewn'),


    path('complaint_viewn/',nurse_views.complaint_viewn,name='complaint_viewn'),
    path('complaint_viewu/',user_views.complaint_viewu,name='complaint_viewu'),



    path('complaintregister/',nurse_views.complaintregister,name='complaintregister'),

    path('complaint_viewn/',nurse_views.complaint_viewn,name='complaint_viewn'),



    path('complaint_registeru/',user_views.complaint_registeru,name='complaint_registeru'),

    path('scheduleadd/',nurse_views.scheduleadd,name='scheduleadd'),
    path('schedule_viewn/',nurse_views.schedule_viewn,name='schedule_viewn'),
    path('scheduleadd_update/<int:update>',nurse_views.scheduleadd_update,name='scheduleadd_update'),
    path('scheduleadd_delete/<int:delete>',nurse_views.scheduleadd_delete,name='scheduleadd_delete'),

    path('schedule_viewu/',user_views.schedule_viewu,name='schedule_viewu'),
    path('bookappointment/<int:id>',user_views.bookappointment,name='bookappointment'),
    path('bookappointmentviewa/',admin_views.bookappointmentviewa,name='bookappointmentviewa'),
    path('approve_appointment/<int:id>',admin_views.approve_appointment,name='approve_appointment'),
    path('reject_appointment/<int:id>',admin_views.reject_appointment,name='reject_appointment'),
    path('bookappointmentstatusviewn/',nurse_views.bookappointmentstatusviewn,name='bookappointmentstatusviewn'),
    path('markvaccinated/<int:id>',nurse_views.markvaccinated,name='markvaccinated'),
    path('bookappointmentstatusviewu/',user_views.bookappointmentstatusviewu,name='bookappointmentstatusviewu'),
    path('nursebookappointmentview/',admin_views.nursebookappointmentview,name='nursebookappointmentview'),

    path('vaccinationcard/<int:id>',admin_views.vaccinationcard,name='vaccinationcard'),
    path('profile/',user_views.profile,name='profile'),
    path('profileupdate/<int:update>',user_views.profileupdate,name='profileupdate'),
    path('addreportcard/<int:id>',admin_views.addreportcard,name='addreportcard')



    ]

