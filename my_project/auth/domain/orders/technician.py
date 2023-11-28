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

technician_has_product_loading = db.Table(
    'technician_has_product_loading',
    db.Column('technician_id', db.Integer, db.ForeignKey('technician.id'), primary_key=True),
    db.Column('product_loading_id', db.Integer, db.ForeignKey('product_loading.id'), primary_key=True),
    db.UniqueConstraint('technician_id', 'product_loading_id', name='uq_technician_has_product_loading'),
    extend_existing=True
)

class Technician(db.Model, IDto):
    __tablename__ = "technician"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    technician_name = db.Column(db.String(45), nullable=False)
    technician_last_name = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(45), nullable=False)
    fundraisings = db.relationship("Fundraising", secondary="fundraising_has_technician",
                               back_populates="technicians")
    coins_loadings = db.relationship("CoinsLoading", secondary="technician_has_coins_loading",
                               back_populates="technicians")
    product_loadings = db.relationship("ProductLoading", secondary="technician_has_product_loading",
                                     back_populates="technicians")


    def __repr__(self) -> str:
        return f"Technician({self.id}, {self.technician_name}, {self.technician_last_name}, {self.phone_number})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "technician_name": self.technician_name,
            "technician_last_name": self.technician_last_name,
            "phone_number": self.phone_number

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Technician:
        obj = Technician(
            technician_name=dto_dict.get("technician_name"),
            technician_last_name=dto_dict.get("technician_last_name"),
            phone_number=dto_dict.get("phone_number")
        )
        return obj
