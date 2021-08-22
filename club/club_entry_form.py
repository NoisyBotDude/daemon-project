from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FormOption(FlaskForm):
    club_add_form = SubmitField("Add Club")
    club_update_form = SubmitField("Update Club")
    club_delete_form = SubmitField("Delete Club")

class ClubAdd(FlaskForm):
    club_name = StringField("Club Name", validators=[DataRequired()])
    club_description = StringField("Club Description", validators=[DataRequired()])
    club_registration_link = StringField("Club Registration Link", validators=[DataRequired()])
    submit = SubmitField("Add club")

class ClubUpdate(FlaskForm):
    club_name = StringField("Club Name", validators=[DataRequired()])
    portion_to_be_updated = StringField("Portion to be updated", validators=[DataRequired()])
    updated_info = StringField("Updated information", validators=[DataRequired()])
    submit = SubmitField("Update Club")

class ClubDelete(FlaskForm):
    club_name = StringField("Club Name", validators=[DataRequired()])
    submit = SubmitField("Delete Club")

