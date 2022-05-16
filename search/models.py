from sqlalchemy.dialects import postgresql

from search import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    rubrics = db.Column(postgresql.ARRAY(db.Text))

    def __repr__(self):
        return f"<post:{self.id}, {self.created_date}>"
