from datetime import date, timedelta
from sqlalchemy.orm import Session
from app.database import models

def delete_old_internships(db: Session):
    cutoff_date = date.today() - timedelta(days=14)

    deleted_rows = (
        db.query(models.Internship)
        .filter(models.Internship.scraped_date < cutoff_date)
        .delete()
    )

    db.commit()
    return deleted_rows