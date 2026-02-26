from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.scraper.internshala import scrape_internshala

router = APIRouter(prefix="/internships", tags=["Internships"])


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/scrape")
async def run_scraper(db: Session = Depends(get_db)):
    total = await scrape_internshala(db)
    return {
        "message": "Scraping completed",
        "total_saved": total
    }