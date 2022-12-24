from odoo import api, fields, models, exceptions


class Session(models.Model):
    _name = 'husniacademy.session'
    _description = 'Data Course Session'

    name = fields.Char(string='Name')
    course_id = fields.Many2one(
        comodel_name='husni_academy.course', 
        string='Course'
    )

    instructor_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Instructor', 
        domain="[('is_instructor', '=', True)]"
    )

    session_date = fields.Datetime(
        string='Session Data', 
        default=fields.Datetime.now()
    )

    min_attendee = fields.Integer(
        string='Minimum Attendee'
    )

    attendee_ids = fields.One2many(
        comodel_name='husniacademy.attendee', 
        inverse_name='session_id', 
        string='Attendee'
    )

    taken_seats = fields.Float(
        compute='_compute_taken_seats', 
        string='Taken Seats',
        store=True
    )
    
    @api.depends('min_attendee', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.min_attendee:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.min_attendee
    
    @api.onchange('min_attendee', 'attendee_ids')
    def _onchange_attendee(self):
        if self.min_attendee < 0:
            return {
                'warning': {
                    'title': "Salah Data!",
                    'message': "Min Attendee tidak boleh kurang dari 0",
                },
            }
        if self.min_attendee < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase min attendee or remove excess attendees",
                },
            }
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Nama Session harus unik, tidak boleh sama!!!"),
    ]

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            students = [record.student_id.id for record in r.attendee_ids]
            if r.instructor_id and r.instructor_id.id in students:
                raise exceptions.ValidationError("Instructor tidak boleh menjadi Attendee...!!!")


class ModuleName(models.Model):
    _name = 'husniacademy.attendee'
    _description = 'Attendee of course session'

    name = fields.Char(string='No Pendaftaran')
    student_id = fields.Many2one(
        comodel_name='res.partner', 
        domain="[('is_student', '=', True)]",
        string='Student'
    )
    reg_date = fields.Datetime(string='Reg Date', default=fields.Datetime.now())
    session_id = fields.Many2one(
        comodel_name='husniacademy.session',  
        string='Session'
    )
    remark = fields.Char(string='Remarks')
    
    
    
    
    
    
