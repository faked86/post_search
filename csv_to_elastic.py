from search.models import Post

from elasticsearch7 import Elasticsearch


es = Elasticsearch()
# posts = Post.query.all()

# for post in posts:
#     doc = {
#         "id": post.id,
#         "text": post.text
#     }
#     resp = es.index(index="posts", id=post.id, document=doc)
#     print(resp['result'])

resp = es.search(index="posts", query={"match": {"text": "Слив информации на пассивки"}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(id)d: %(text)s" % hit["_source"])
