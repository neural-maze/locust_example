from sqlmodel import SQLModel, Field

class Artist(SQLModel, table=True):
        
    ArtistId: int = Field(primary_key=True)
    Name: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "ArtistId": 1,
                    "Name": "AC/DC",
                }
            ]
        }
    }
    
class Album(SQLModel, table=True):
    
    AlbumId: int = Field(primary_key=True)
    Title: str
    ArtistId: int = Field(foreign_key="Artist.ArtistId")
