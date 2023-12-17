from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

snacks_has_brand = db.Table(
    'snacks_has_brand',
    db.Column('snacks_id', db.Integer, db.ForeignKey('snacks.id'), primary_key=True),
    db.Column('brand_id', db.Integer, db.ForeignKey('brand.id'), primary_key=True),
    db.UniqueConstraint('snacks_id', 'brand_id', name='uq_snacks_has_brand'),
    extend_existing=True
)


class Brand(db.Model, IDto):
    __tablename__ = "brand"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(40), nullable=False)
    snackses = db.relationship("Snacks", secondary="snacks_has_brand",
                             back_populates="brands")

    def __repr__(self) -> str:
        return f"Brand({self.id}, {self.brand})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "brand_name": self.brand_name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Brand:
        obj = Brand(
            brand_name=dto_dict.get("brand_name")
        )
        return obj
