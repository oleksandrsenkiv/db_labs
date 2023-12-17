from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Brand
from my_project.auth.domain.orders.snacks import snacks_has_brand
from my_project.auth.domain.orders.snacks import Snacks
from sqlalchemy import text


class BrandDAO(GeneralDAO):
    _domain_type = Brand

    def brand_find_snacks(self, brand_id: int):
        """
        Find solar system associated with a specific owner.
        :param brand_id: ID of the owner
        :return: List of SolarSystem objects associated with the owner
        """
        session = self.get_session()

        snackses_ids = (
            session.query(snacks_has_brand.c.snacks_id)
            .filter(snacks_has_brand.c.brand_id == brand_id)
            .all()
        )

        snacks_ids = [snacks_id for (snacks_id,) in snackses_ids]
        snacks = session.query(Snacks).filter(Snacks.id.in_(snacks_ids)).all()
        return [snacks.put_into_dto() for snacks in snacks]

    def add_snacks_to_brand(self, brand_id: int, snacks_id: int):
        session = self.get_session()

        association = snacks_has_brand.insert().values(
            brand_id=brand_id,
            snacks_id=snacks_id
        )

        session.execute(association)
        session.commit()

    def remove_snack_from_brand(self, brand_id: int, snacks_id: int):
        session = self.get_session()
        session.execute(
            snacks_has_brand.delete()
            .where(snacks_has_brand.c.brand_id == brand_id)
            .where(snacks_has_brand.c.snacks_id == snacks_id)
        )
        session.commit()

    def add_brand(self, insert_brand: str):
        try:
            session = self.get_session()
            sql_expression = text("CALL add_brand(:brand_name)")
            session.execute(sql_expression, {'brand_name': insert_brand})
            session.commit()
        except Exception as e:
            print(f"Error with adding brand: {e}")

