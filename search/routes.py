from flask import request, jsonify

from search import app, db, es
from search.models import Post


@app.get("/search")
def search():
    args = request.args
    query = args.get("query")
    if query is None:
        return jsonify("Need 'query' parameter in GET method"), 400

    resp = es.search(index="posts", size=20, query={"match": {
        "text": query
    }})

    posts = []
    for hit in resp['hits']['hits'][:20]:
        print("%(id)d: %(text)s" % hit["_source"])
        post = Post.query.get(hit["_source"]["id"])
        posts.append(
            {
                "id": post.id,
                "text": post.text,
                "created_date": post.created_date,
                "rubrics": post.rubrics
            }
        )

    sorted_posts = sorted(posts, key=lambda d: d['created_date'])
    return jsonify(sorted_posts)


@app.delete("/post/<post_id>")
def delete(post_id):
    post = Post.query.get(post_id)
    try:
        es.delete_by_query(index='posts', body={
            "query": {"match": {
                "id": post.id
                }
            }
        })
        db.session.delete(post)
        db.session.commit()

    except Exception as err:
        print(err)
        db.session.rollback()
        return jsonify("Something went wrong"), 500

    return jsonify("Post was successfully deleted"), 200
