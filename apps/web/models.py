from apps.app import db

relations = db.Table(
    "relations",
    db.Column("article_id", db.Integer, db.ForeignKey("articles._id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags._id")),
)


class Article(db.Model):
    __tablename__ = "articles"

    _id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, index=True)
    title = db.Column(db.String, index=True)
    tags = db.relationship(
        "Tag",
        secondary=relations,
        lazy="subquery",
        backref=db.backref("article", lazy="dynamic"),
    )
    pro_link = db.Column(db.String)
    content = db.Column(db.Text)

    def __init__(self, number, title, pro_link, content):
        self.number = number
        self.title = title
        self.pro_link = pro_link
        self.content = content


class Tag(db.Model):
    __tablename__ = "tags"
    _id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String, nullable=False)

    def __init__(self, tag):
        self.tag = tag
