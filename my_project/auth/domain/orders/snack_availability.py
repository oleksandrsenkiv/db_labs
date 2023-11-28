
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

class SnackAvailability(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "snack_availability"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    snack_count = db.Column(db.Integer, nullable=False)
    vm_menus = db.relationship("VmMenu", secondary="snacks_has_vm_menu",
                               back_populates="snack_availabilities")

    def __repr__(self) -> str:
        return f"SnackAvailability({self.id}, {self.snack_count})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "snack_count": self.snack_count
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SnackAvailability:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SnackAvailability(
            snack_count=dto_dict.get("snack_count")
        )
        return obj
