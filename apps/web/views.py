from pathlib import Path

import markdown
import markdown.extensions.fenced_code
from flask import Blueprint, redirect, render_template, url_for

from apps.app import db
from apps.web.forms import ArticleForm
from apps.web.models import Article, Tag
from apps.web.utils import add_toc

article_basedir = Path(__file__).parent.parent.parent


web = Blueprint(
    "web",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)


def add_article(article, tags):
    # Remove the tag with no article linked to it
    for tag in article.tags:
        if tag.article.count() == 1:
            db.session.delete(tag)

    # Clear the original tags and link the new tags to it
    article.tags.clear()
    for tag in tags.data.split("/"):
        new_tag = Tag.query.filter_by(tag=tag).first()
        if new_tag is None:
            new_tag = Tag(tag)
        article.tags.append(new_tag)
    db.session.add(article)
    db.session.commit()


@web.route("/")
def index():
    articles = Article.query.order_by(Article.number).all()
    return render_template("index.html", articles=articles)


@web.route("/article/new", methods=["GET", "POST"])
def create_article():
    form = ArticleForm()

    if form.validate_on_submit():
        article = Article(
            number=form.number.data,
            title=form.title.data,
            pro_link=form.pro_link.data,
            content=form.content.data,
        )

        add_article(article, form.tag)

        return redirect(url_for("web.index"))

    return render_template("add_article.html", form=form)


@web.route("/article/<number>")
def read_article(number):
    mkd_text = markdown.markdown(
        add_toc(Article.query.filter_by(number=number).first().content),
        extensions=["fenced_code", "mdx_math", "codehilite", "toc"],
        extension_configs={
            "mdx_math": {
                "enable_dollar_delimiter": True,
            },
            "toc": {"anchorlink": "icon"},
        },
    )

    return render_template(
        "markdown.html",
        mkd_text=mkd_text,
    )


@web.route("/article/edit/<number>", methods=["GET", "POST"])
def edit_article(number):
    article = Article.query.filter_by(number=number).first()
    form = ArticleForm()

    if form.validate_on_submit():
        article.number = form.number.data
        article.title = form.title.data
        article.pro_link = form.pro_link.data
        article.content = form.content.data
        add_article(article, form.tag)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("web.index"))

    # Prevent from overwritten after click the submit button
    form.tag.data = "/".join([tag.tag for tag in article.tags])
    form.content.data = article.content
    return render_template("edit.html", form=form, article=article)


@web.route("/tag/<tag>")
def get_tag(tag):
    articles = (
        Tag.query.filter_by(tag=tag).first().article.order_by(Article.number).all()
    )

    return render_template("index.html", articles=articles)
