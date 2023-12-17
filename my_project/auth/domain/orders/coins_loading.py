from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

technician_has_coins_loading = db.Table(
    'technician_has_coins_loading',
    db.Column('technician_id', db.Integer, db.ForeignKey('technician.id'), primary_key=True),
    db.Column('coins_loading_id', db.Integer, db.ForeignKey('coins_loading.id'), primary_key=True),
    db.UniqueConstraint('technician_id', 'coins_loading_id', name='uq_technician_has_coins_loading'),
    extend_existing=True
)

class CoinsLoading(db.Model, IDto):
    __tablename__ = "coins_loading"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coins_loading_date = db.Column(db.Date, nullable=False)
    coin_nominal = db.Column(db.Integer, nullable=False)
    coin_count = db.Column(db.Integer, nullable=False)
    technicians = db.relationship("Technician", secondary="technician_has_coins_loading",
                                  back_populates="coins_loadings")

    def __repr__(self) -> str:
        return f"CoinsLoading({self.id}, {self.coins_loading_date}, {self.coin_nominal}, {self.coin_count})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "coins_loading_date": self.coins_loading_date,
            "coin_nominal": self.coin_nominal,
            "coin_count": self.coin_count
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CoinsLoading:
        obj = CoinsLoading(
            coins_loading_date=dto_dict.get("coins_loading_date"),
            coin_nominal=dto_dict.get("coin_nominal"),
            coin_count=dto_dict.get("coin_count")
        )
        return obj
