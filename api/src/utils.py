from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from src.models import User, Challenge, Solve


def get_users_score(db: Session):
    return db.query(User, func.sum(Challenge.score).label("total_score")) \
        .join(Solve, Solve.challenge_id == Challenge.id) \
        .join(User, Solve.user_id == User.id) \
        .group_by(User.id) \
        .order_by(desc("total_score"), User.last_solve.asc()).all()
