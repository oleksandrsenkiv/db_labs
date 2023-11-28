from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

snacks_has_vm_menu = db.Table(
    'snacks_has_vm_menu',
    db.Column('snacks_id', db.Integer, db.ForeignKey('snacks.id'), primary_key=True),
    db.Column('vm_menu_id', db.Integer, db.ForeignKey('vm_menu.id'), primary_key=True),
    db.Column('snack_availability_id', db.Integer, db.ForeignKey('snack_availability.id'), primary_key=True),
    db.UniqueConstraint('snacks_id', 'vm_menu_id', 'snack_availability_id', name='snacks_has_vm_menu'),
    extend_existing=True
)
class VmMenu(db.Model, IDto):
    __tablename__ = "vm_menu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vending_machines = db.relationship("VendingMachine", backref="vm_menu_", lazy="dynamic")
    snack_availabilities = db.relationship("SnackAvailability", secondary="snacks_has_vm_menu",
                               back_populates="vm_menus")
    snackses = db.relationship("Snacks", secondary="snacks_has_vm_menu",
                                           back_populates="vm_menus")


    def __repr__(self) -> str:
        return f"VmMenu({self.id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> VmMenu:
        obj = VmMenu()
        return obj
