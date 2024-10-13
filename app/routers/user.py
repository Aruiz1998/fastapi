from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
 
router = APIRouter(prefix="/users",
                   tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)

def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    user.password = utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def find_user(id: int, db: Session=Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.id == id).first()
    print(user_query)
    if user_query:
        return user_query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kill yourself")
