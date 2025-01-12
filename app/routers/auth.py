from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oath2
from ..database import engine, get_db

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model= schemas.Token)
def authenticate(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="KILL YOURSELF")
    
    hashed_password = user.password
    if not utils.verify(user_credentials.password, hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="KILL YOURSELF")
    
    access_token = oath2.create_access_token(data = {"user_id": user.id})
    return {"access_token" : access_token, "token_type": "bearer"}
