from search.models import Post

from search import es


posts = Post.query.all()

for post in posts:
    doc = {
        "id": post.id,
        "text": post.text
    }
    resp = es.index(index="posts", id=post.id, document=doc)
