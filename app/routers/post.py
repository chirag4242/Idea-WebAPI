from .. import schemas,models, oauth2
from fastapi import Depends, Response, status, HTTPException, APIRouter 
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)
# get method used to retive the information for example all the post 
# /posts path 
# used this to read operation
@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10,skip:int=0,search: Optional[str] =""):
    # cursor.execute("""SELECT * from posts""")
    # posts= cursor.fetchall()
    # for reference
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(
            func.lower(models.Post.title).contains(search.lower()),
            func.lower(models.Post.title).ilike(f"%{search}%")).limit(limit).offset(skip).all() 
    return  posts

# We want to create the data we use post which takes 
# data and use that data give an result 
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # connect.commit()
    # new_post=  models.Post(title=post.title,content=post.content,published =post.published)
    
    new_post=  models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id: int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # params always give string value so always convert it to int 
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))
    # post =cursor.fetchone()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post: 
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with {id} was not found"}
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                        detail =f"post with id: {id} was not found")
    return post

# delete post route
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    #my_posts.pop(index) that's for array example
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))
    # deleted_post =  cursor.fetchone()
    # connect.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} does not exist")    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authoqized to perform rquested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int,updated_post:schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title= %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title,post.content,post.published, str(id)))
    # updated_post = cursor.fetchone()
    # connect.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} does not exist")    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authoqized to perform rquested action")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return  post_query.first()
