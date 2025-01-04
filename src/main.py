from fastapi import FastAPI
from pydantic import BaseModel




app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    
    
posts = []



@app.post('/posts/')
def create_post(post: Post):
    posts.append(post)
    return {"message": "Post Created Successfully!"}


@app.get('/posts/')
def get_posts():
    return {"posts": posts}



@app.put('/posts/{post_id}/')
def update_post(post_id: int, update_post: Post):
    if post_id < 0 or post_id >= len(posts):
        return {"error": "The post is not found!"}
    posts[post_id] = update_post
    return {"message": "Post Updaetd Successfully!", "post": update_post}



@app.delete('/posts/{post_id}/')
def delete_post(post_id: int):
    if post_id < 0 or post_id >= len(posts):
        return {"error": "The post is not found!"}
    delet_post = posts.pop(post_id)
    return {"message": "Post delete Successfully!"}
