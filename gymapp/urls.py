from django.urls import path

# from .views import home , about
from .views import *

urlpatterns = [
    path('',home, name='home'), # Include gymapp URLs
    path('about/', about, name='about'), # Include gymapp URLs
    path('admin-login/',admin_login_view,name='admin_login'),
    path('admin-dashboard/',admin_dashboard_view, name='admin_dashboard'),
    path('logout/', logout_view, name='logout'),
   
    path('admin_plans/',admin_plans_list, name='admin_plans_list'),
    path('admin_plans_add/', admin_plan_add, name='admin_plan_add'),
    path('admin_plans_edit/<int:plan_id>/' , admin_plan_edit, name='admin_plan_edit'),
    path('admin_plan_delete/<int:plan_id>/', admin_plan_delete, name='admin_plan_delete'),

    path('admin_trainers/', admin_trainers_list, name='admin_trainers_list'),
    path('admin_trainers_add/', admin_trainer_add, name='admin_trainer_add'),
    path('admin_trainers_edit/<int:trainer_id>/', admin_trainer_edit, name='admin_trainer_edit'),
    path('admin_trainers_delete/<int:trainer_id>/', admin_trainer_delete, name='admin_trainer_delete'),
   

    path('admin_members/', admin_members_list, name='admin_members_list'),
    path('admin_members_add/', admin_member_add, name='admin_member_add'),
    path('admin_members_edit/<int:member_id>/', admin_member_edit, name='admin_member_edit'),
    path('admin_members_delete/<int:member_id>/', admin_member_delete, name='admin_member_delete'),

    path('admin_attendance/', admin_attendance_list, name='admin_attendance_list'),
    path('admin_attendance_add/', admin_attendance_add, name='admin_attendance_add'),
    path('admin_equipment/', admin_equipment_list, name='admin_equipment_list'),
    path('admin_equipment_add/', admin_equipment_add, name='admin_equipment_add'),
    path('admin_equipment_edit/<int:equipment_id>/', admin_equipment_edit, name='admin_equipment_edit'),
    path('admin_equipment_delete/<int:equipment_id>/', admin_equipment_delete, name='admin_equipment_delete'),
    path('admin_enquiries_list/', admin__enquiries_list, name='admin_enquiries_list'),
    path('admin_enquiries_list/<int:enquiry_id>/update/', admin_enquiry_update_status, name='admin_enquiry_update_status'),

    path('admin_workout_plans/', admin_workout_plans_list, name='admin_workout_plans_list'),
    path('admin_workout_plan_add/', admin_workout_plan_add, name='admin_workout_plan_add'),
    path('admin_workout_plan_delete/<int:plan_id>/', admin_workout_plan_delete, name='admin_workout_plan_delete'),
    
    path('admin_payments/', admin_payments_list, name='admin_payments_list'),
    path('admin_payment_add/', admin_payment_add, name='admin_payment_add'),
    
    path('member-login/', member_login_view, name='member_login'),
    path('member-dashboard/', member_dashboard_view, name='member_dashboard'),
    path('member-attendance/', member_attendance, name='member_attendance'),
    path('member-membership/', member_membership, name='member_membership'),

    path('member-payments/', member_payments, name='member_payments'),
    path('member-workout-plans/', member_workout_plans, name='member_workout_plans'),
    path('member-profile-edit/', member_profile_edit, name='member_profile_edit'),
    path('member-change-password/', member_change_password, name='member_change_password'),
    path('member-profile/', member_profile, name='member_profile'),  
    path('member-feedback/', member_feedback_view, name='member_feedback'),
    path('member-feedbacks-list/',admin_feedbacks_list, name='admin_feedbacks_list'),

 ]  
   
   

