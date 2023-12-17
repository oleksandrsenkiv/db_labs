from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class VendingMachine(db.Model, IDto):
    __tablename__ = "vending_machine"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gps_id = db.Column(db.Integer, db.ForeignKey('gps.id'), nullable=False)
    address = db.Column(db.String(255),  nullable=False)
    vm_menu_id = db.Column(db.Integer, db.ForeignKey('vm_menu.id'))
    gps = db.relationship("Gps", backref="vending_machine_gps_")
    vm_menu = db.relationship("VmMenu", backref="vending_machine_")

    def __repr__(self) -> str:
        return f"VendingMachine({self.id}, {self.latitude}, {self.longitude})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "gps": self.gps_id,
            "address": self.address,
            "vm_menu_id": self.vm_menu_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> VendingMachine:
        obj = VendingMachine(
            gps_id=dto_dict.get("gps_id"),
            address=dto_dict.get("address"),
            vm_menu_id=dto_dict.get("vm_menu_id"),

        )
        return obj
