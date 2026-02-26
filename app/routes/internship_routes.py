from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from scraper.internshala_scraper import scrape_internshala

router = APIRouter(prefix="/internships", tags=["Internships"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/scrape")
async def manual_scrape(keyword: str, db: Session = Depends(get_db)):
    count = await scrape_internshala(keyword, db)
    return {"new_saved": count}