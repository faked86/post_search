import datetime
import csv

from search import db
from search.models import Post


db.drop_all()
db.create_all()
with open("posts.csv", encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',', quotechar='"')
    next(csv_reader)
    for row in csv_reader:
        created_date = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")

        rubrics_raw = row[2].strip("[]").split(",")
        rubrics = []
        for rubric in rubrics_raw:
            rubrics.append(rubric.strip(" '\""))

        post = Post(
            text=row[0],
            created_date=created_date,
            rubrics=rubrics
        )
        db.session.add(post)
    db.session.commit()
