import csv
import logging

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from daterange_filter.filter import DateRangeFilter
from django.http import HttpResponse

from .models import *

_log = logging.getLogger(__name__)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')

class InstructorInline(admin.StackedInline):
    model = Instructor
    can_delete=False
    verbose_name_plural = 'Instructor'

class StudentAdmin(admin.ModelAdmin):
    list_display =  ('osis_number', 'first_name', 'last_name', 'email', 'school')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'course')

class LearningTargetAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')

class GroupStudentInline(admin.StackedInline):
    model = GroupStudent
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupStudentInline]
    list_display = ('code', 'section', 'instructor')

    def get_queryset(self, request):
        qs = super(GroupAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(instructor__user=request.user)
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'instructor':
                kwargs["queryset"] = Instructor.objects.filter(user=request.user)
        return super(GroupAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('course', 'instructor', 'description')
    
    def get_queryset(self, request):
        qs = super(PlanAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(instructor__user=request.user)

class ReportStudentInline(admin.StackedInline):
    model = ReportStudent
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'student' and not request.user.is_superuser:
            instructor_groups = request.user.instructor_set.first().group_set.all()
            student_ids = set()
            for group in instructor_groups:
                for student in group.groupstudent_set.all():
                    student_ids.add(student.id)
            kwargs["queryset"] = Student.objects.filter(pk__in=student_ids)
        return super(ReportStudentInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ReportAdmin(admin.ModelAdmin):
    inlines = [ReportStudentInline]
    list_display = ('group', 'date', 'week', 'exported')
    exporter_list_filter = (
        'exported',
        ('date', DateRangeFilter)
    )
    actions = ['export_report_action']
    
    class Media:
      js = ("js/admin/report.js",)

    def get_actions(self, request):
        actions = super(ReportAdmin, self).get_actions(request)
        if not request.user.has_perm('best.export_report'):
            if 'export_report_action' in actions:
                del actions['export_report_action']
        return actions

    def get_list_filter(self, request):
        if request.user.has_perm('best.export_report'):
            return self.exporter_list_filter
        else:
            return ()

    def export_report_action(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=reports.csv'

        writer = csv.writer(response)
        writer.writerow([
            'OSIS #', 'Course', 'Fiscal/Schol Year', 'Date', 'Quarter', 'Week', 'Attendance', 'Dosage', 'Exit Ticket',
            'Exit Ticket (Denominator)', 'Learning Target Notes', 'HW Effort', 'HW Accuracy',
            'HW (Denominator)', 'Weekly Quiz', 'Weekly Quiz', 'Instructor'
        ])
        for report in queryset:
            for report_student in report.reportstudent_set.all():
                student = report_student.student
                writer.writerow([
                    student.osis_number,
                    report.group.section.course.code,
                    report.group.section.year_code,
                    report.date,
                    report.group.section.semester_code,
                    report.week,
                    report_student.get_attendance_display(),
                    report.plan.dosage,
                    report_student.exit_ticket,
                    report.plan.exit_ticket_denominator,
                    report.plan.learning_target.code,
                    report_student.get_homework_effort_display(),
                    report_student.homework_accuracy,
                    report.plan.homework_denominator,
                    'Yes' if report_student.quiz and str(report_student.quiz) else 'No',
                    report_student.quiz,
                    "{} {}".format(report.group.instructor.user.first_name, report.group.instructor.user.last_name),
                ])

        queryset.update(exported=True)
        self.message_user(request, "{} report(s) exported".format(queryset.count()))
        return response
    export_report_action.short_description = 'Export selected reports for Apricot'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'group':
                kwargs["queryset"] = Group.objects.filter(instructor__user=request.user)
        return super(ReportAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(ReportAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        if request.user.has_perm('best.export_report'):
            return qs.filter(group__section__school=request.user.instructor.school)

        return qs.filter(group__instructor__user=request.user)

class UserAdmin(UserAdmin):
    inlines = (InstructorInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(School)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Standard)
admin.site.register(LearningTarget, LearningTargetAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Report, ReportAdmin)
