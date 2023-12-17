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

snacks_has_vm_menu = db.Table(
    'snacks_has_vm_menu',
    db.Column('snacks_id', db.Integer, db.ForeignKey('snacks.id'), primary_key=True),
    db.Column('vm_menu_id', db.Integer, db.ForeignKey('vm_menu.id'), primary_key=True),
    db.Column('snack_availability_id', db.Integer, db.ForeignKey('snack_availability.id'), primary_key=True),
    db.UniqueConstraint('snacks_id', 'vm_menu_id', 'snack_availability_id', name='snacks_has_vm_menu'),
    extend_existing=True
)


class Snacks(db.Model, IDto):
    __tablename__ = "snacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    snack_name = db.Column(db.String(40), nullable=False)
    brands = db.relationship("Brand", secondary="snacks_has_brand",
                                    back_populates="snackses")
    vm_menus = db.relationship("VmMenu", secondary="snacks_has_vm_menu",
                               back_populates="snackses")

    def __repr__(self) -> str:
        return f"Snacks({self.id}, {self.snack_name})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "snack_name": self.snack_name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Snacks:
        obj = Snacks(
            snack_name=dto_dict.get("snack_name")
        )
        return obj
