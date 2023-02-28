from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    number = IntegerField(
        label="Problem No.", validators=[DataRequired("Requires the problem number")]
    )
    title = StringField(
        label="Problem title",
        validators=[DataRequired("Please provide the problem's title")],
    )
    tag = StringField(
        validators=[
            DataRequired(
                "Please provide at least a tag and separate multiple tag with '/'"
            )
        ]
    )
    pro_link = StringField(
        label="Link to the problem",
        validators=[DataRequired("Please paste the link for the article")],
    )

    content = TextAreaField(
        label="Content", validators=[DataRequired("Please provide the content")]
    )

    submit = SubmitField("Add")
