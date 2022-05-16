# POST_SEARCH

## INSTALLATION

Prerequisites:
- docker
- docker-compose
- git

Simply clone this repo:

```
git clone https://github.com/faked86/post_search.git
cd post_search
```

## USAGE

1. Run `docker-compose up` in terminal.


### API Server

- `POST localhost:8000/search?query=<your_query>` - find post by your_query
- `DELETE localhost:8000/post/<post_id>` - delete post by post_id