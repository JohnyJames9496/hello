import asyncio
from app.database.database import SessionLocal
from app.scraper.internshala import scrape_internshala
from app.tasks.cleanup import delete_old_internships

async def main():
    db = SessionLocal()

    try:
        print("Deleting old internships...")
        deleted = delete_old_internships(db)
        print(f"Deleted {deleted} old internships")

        print("Scraping new internships...")
        saved = await scrape_internshala(db)
        print(f"Saved {saved} new internships")

    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(main())