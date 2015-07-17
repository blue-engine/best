import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import *

class ContentAreaAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'content_area')

class InstructorAdmin(admin.ModelAdmin):
    list_display =  ('first_name', 'last_name', 'email', 'school')

class StudentAdmin(admin.ModelAdmin):
    list_display =  ('osis_number', 'first_name', 'last_name', 'email', 'school')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'course')

class LearningTargetAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')

class GroupStudentInline(admin.TabularInline):
    model = GroupStudent
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupStudentInline]
    list_display = ('code', 'section', 'instructor')

class ReportStudentInline(admin.TabularInline):
    model = ReportStudent
    extra = 3


class ReportAdmin(admin.ModelAdmin):
    inlines = [ReportStudentInline]
    list_display = ('group', 'date', 'week', 'exported')
    #list_filter = ('exported',)
    actions = ['export_report_action']

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
                    report.dosage,
                    report_student.exit_ticket,
                    report.exit_ticket_denominator,
                    report.learning_target.code,
                    report_student.get_homework_effort_display(),
                    report_student.homework_accuracy,
                    report.homework_denominator,
                    '?',
                    '?',
                    "{} {}".format(report.group.instructor.first_name, report.group.instructor.last_name),
                ])

        queryset.update(exported=True)
        self.message_user(request, "{} report(s) exported".format(queryset.count()))
        return response
    export_report_action.short_description = 'Export selected reports for Apricot'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'group':
            #kwargs["queryset"] = Group.objects.filter(instructor__user=request.user)
            pass
        return super(ReportAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(School)
admin.site.register(ContentArea, ContentAreaAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Standard)
admin.site.register(LearningTarget, LearningTargetAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupStudent)
admin.site.register(Report, ReportAdmin)
admin.site.register(ReportStudent)
