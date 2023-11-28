from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

fundraising_has_technician = db.Table(
    'fundraising_has_technician',
    db.Column('fundraising_id', db.Integer, db.ForeignKey('fundraising.id'), primary_key=True),
    db.Column('technician_id', db.Integer, db.ForeignKey('technician.id'), primary_key=True),
    db.UniqueConstraint('fundraising_id', 'technician_id', name='uq_fundraising_has_technician'),
    extend_existing=True
)

technician_has_coins_loading = db.Table(
    'technician_has_coins_loading',
    db.Column('technician_id', db.Integer, db.ForeignKey('technician.id'), primary_key=True),
    db.Column('coins_loading_id', db.Integer, db.ForeignKey('coins_loading.id'), primary_key=True),
    db.UniqueConstraint('technician_id', 'coins_loading_id', name='uq_technician_has_coins_loading'),
    extend_existing=True
)


class Fundraising(db.Model, IDto):
    __tablename__ = "fundraising"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fundraising_count = db.Column(db.Integer, nullable=False)
    fundraising_date = db.Column(db.Date, nullable=False)
    technicians = db.relationship("Technician", secondary="fundraising_has_technician",
                               back_populates="fundraisings")

    def __repr__(self) -> str:
        return f"Fundraising({self.id}, {self.fundraising_count}, {self.fundraising_date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "fundraising_count": self.fundraising_count,
            "fundraising_date": self.fundraising_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Fundraising:
        obj = Fundraising(
            fundraising_count=dto_dict.get("fundraising_count"),
            fundraising_date=dto_dict.get("fundraising_date")
        )
        return obj
