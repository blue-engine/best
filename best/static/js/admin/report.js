(function($){
    $(window).load(function() {
        $plans = $('#id_plan')
        old_group_id = $plans.val()

        $('#id_group').change(function(){
            group_id = $(this).val()
            if (group_id != old_group_id 
                && (!old_group_id || confirm('Changing Groups, Will remove all form data'))) {
                $student_selects = $('#reportstudent_set-group .field-student select')
                $('#reportstudent_set-group input').val(null)
                $('#reportstudent_set-group select').val(null)
                $('#reportstudent_set-group .inline-deletelink').click()
                $student_selects.html('<option value="">---------</option>')

                $.getJSON("/api/groups/"+group_id, function( data ) {
                    current_plan_id = $plans.val()
                    $plans.html('<option value="">---------</option>')
                    for (var i in data.plans){
                      if (data['plans'].hasOwnProperty(i)) {
                        plan = data['plans'][i]
                        $plans.append('<option value="' + plan.id + '">' + plan.description + '</option>')
                      }
                    }

                    for (var i in data.group_students){
                      if (data.group_students.hasOwnProperty(i)) {
                        student = data.group_students[i].student
                        $student_selects.append('<option value="' + student.id + '">' + student.last_name + ', ' + student.first_name + '</option>')
                        if (parseInt(i) + 1 == $student_selects.length){
                            $('#reportstudent_set-group .add-row a').click()
                            $student_selects = $('#reportstudent_set-group .field-student select')
                        }
                        $('#reportstudent_set-'+i+' .field-student select').val(student.id)
                      }
                    }
                });
                old_group_id = group_id
            } else {
              $(this).val(old_group_id)
            }
        })
    });
})(django.jQuery);
