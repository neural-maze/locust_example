from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from .database import get_session
from .models import Album, Artist

from sqlmodel import Session, select


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Load Testing API Example"}

@app.post("/albums")
async def get_albums_by_artist(
    artist: Artist, 
    session: SessionDep,    
) -> list[Album]:
    
    statement = select(Album).where(Album.ArtistId == artist.ArtistId)
    results = session.exec(statement).all()
     
    if not results:
        raise HTTPException(status_code=404, detail="Artist or albums not found")
    return list(results)
