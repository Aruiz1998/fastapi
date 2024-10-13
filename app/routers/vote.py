from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, oath2
from ..database import engine, get_db

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session=Depends(get_db), current_user: int=Depends(oath2.get_current_user)):
    # Query database for vote
    # If vote does not exist Try to insert
    # If vote exists try to update
    vote_query = db.query(models.Vote).filter(models.Vote.user_id == current_user.id, models.Vote.post_id == vote.post_id)
    query_result = vote_query.first()
    if vote.dir == 1:
        if query_result:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Vote already exists")
        if query_result == None:
            new_vote = models.Vote(user_id=current_user.id, post_id=vote.post_id)
            db.add(new_vote)
            db.commit()
            return {"message" : "Sucess"}
        
    else:
        if query_result == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no vote from this user to remove")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message" : "Successfully deleted post"}