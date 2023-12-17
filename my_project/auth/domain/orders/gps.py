from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Gps(db.Model, IDto):
    __tablename__ = "gps"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    vending_machines = db.relationship("VendingMachine", backref="gps_", lazy="dynamic")

    def __repr__(self) -> str:
        return f"Gps({self.id}, {self.latitude}, {self.longitude})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Gps:
        obj = Gps(
            latitude=dto_dict.get("latitude"),
            longitude=dto_dict.get("longitude")
        )
        return obj
