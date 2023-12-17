
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Snacks
from my_project.auth.domain.orders.brand import snacks_has_brand
from my_project.auth.domain.orders.brand import Brand
from my_project.auth.domain.orders.snack_availability import snacks_has_vm_menu
from my_project.auth.domain.orders.snack_availability import SnackAvailability
from my_project.auth.domain.orders.vm_menu import VmMenu
from sqlalchemy import text


class SnacksDAO(GeneralDAO):
    _domain_type = Snacks

    def snacks_find_brand(self, snacks_id: int):
        session = self.get_session()

        brands_ids = (
            session.query(snacks_has_brand.c.brand_id)
            .filter(snacks_has_brand.c.snacks_id == snacks_id)
            .all()
        )
        brand_ids = [brand_id for (brand_id,) in brands_ids]
        brands = session.query(Brand).filter(Brand.id.in_(brand_ids)).all()
        return [brand.put_into_dto() for brand in brands]

    def snacks_find_snack_availability_vm_menu(self, snacks_id: int):
        """
        Find availability and vm_menu associated with a specific snack.
        :param snacks_id: ID of the snack
        :return: List of SnackAvailability and VmMenu objects associated with the snack
        """
        session = self.get_session()
        associations = (
            session.query(snacks_has_vm_menu.c.snack_availability_id, snacks_has_vm_menu.c.vm_menu_id)
            .filter(snacks_has_vm_menu.c.snacks_id == snacks_id)
            .all()
        )

        availability_ids, vm_menu_ids = zip(*associations)
        availabilities = session.query(SnackAvailability).filter(SnackAvailability.id.in_(availability_ids)).all()
        vm_menus = session.query(VmMenu).filter(VmMenu.id.in_(vm_menu_ids)).all()

        return {
            "availabilities": [availability.put_into_dto() for availability in availabilities],
            "vm_menus": [vm_menu.put_into_dto() for vm_menu in vm_menus]
        }

    def add_brand_to_snack(self, snacks_id: int, brand_id: int):
        session = self.get_session()

        association = snacks_has_brand.insert().values(
            snacks_id=snacks_id,
            brand_id=brand_id
        )

        session.execute(association)
        session.commit()

    def remove_brand_from_snack(self, snacks_id: int, brand_id: int):
        session = self.get_session()
        session.execute(
            snacks_has_brand.delete()
            .where(snacks_has_brand.c.snacks_id == snacks_id)
            .where(snacks_has_brand.c.brand_id == brand_id)
        )
        session.commit()

    def add_vm_menu_and_availability_to_snack(self, snacks_id: int, vm_menu_id: int, snack_availability_id: int):
        session = self.get_session()

        association = snacks_has_vm_menu.insert().values(
            snacks_id=snacks_id,
            vm_menu_id=vm_menu_id,
            snack_availability_id=snack_availability_id
        )

        session.execute(association)
        session.commit()

    def remove_vm_menu_and_availability_from_snack(self,  snacks_id: int, vm_menu_id: int, snack_availability_id: int):
        session = self.get_session()
        session.execute(
            snacks_has_vm_menu.delete()
            .where(snacks_has_vm_menu.c.snacks_id == snacks_id)
            .where(snacks_has_vm_menu.c.vm_menu_id == vm_menu_id)
            .where(snacks_has_vm_menu.c.snack_availability_id == snack_availability_id)
        )
        session.commit()

    def insert_ten_no_name_snacks(self):
        try:
            session = self.get_session()
            sql_expression = text("CALL insert_noname_snacks()")
            session.execute(sql_expression)
            session.commit()
        except Exception as e:
            print(f"Error with adding no name snacks: {e}")

    def insert_in_snacks_has_brand(self, insert_brand_name: str, insert_snack_name: str):
        try:
            session = self.get_session()
            sql_expression = text("CALL insert_into_snacks_has_brand(:insert_brand_name, :insert_snack_name)")
            session.execute(sql_expression,
                            {'insert_brand_name': insert_brand_name, 'insert_snack_name': insert_snack_name})
            session.commit()
        except Exception as e:
            print(f"Error with adding into snacks has brand: {e}")

    def create_db_from_snacks(self):
        try:
            session = self.get_session()
            sql_expression = text("CALL create_db_from_snacks()")
            session.execute(sql_expression)
            session.commit()
        except Exception as e:
            print(f"Error with creating db: {e}")


