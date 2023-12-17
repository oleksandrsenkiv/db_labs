from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

technician_has_product_loading = db.Table(
    'technician_has_product_loading',
    db.Column('technician_id', db.Integer, db.ForeignKey('technician.id'), primary_key=True),
    db.Column('product_loading_id', db.Integer, db.ForeignKey('product_loading.id'), primary_key=True),
    db.UniqueConstraint('technician_id', 'product_loading_id', name='uq_technician_has_product_loading'),
    extend_existing=True
)

class ProductLoading(db.Model, IDto):
    __tablename__ = "product_loading"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loading_date = db.Column(db.Date, nullable=False)
    loading_snack_count = db.Column(db.Integer)
    technicians = db.relationship("Technician", secondary="technician_has_product_loading",
                                     back_populates="product_loadings")


    def __repr__(self) -> str:
        return f"ProductLoading({self.id}, {self.loading_date}, {self.loading_snack_count})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "loading_date": self.loading_date,
            "loading_snack_count": self.loading_snack_count
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProductLoading:
        obj = ProductLoading(
            loading_date=dto_dict.get("loading_date"),
            loading_snack_count=dto_dict.get("loading_snack_count")
        )
        return obj
