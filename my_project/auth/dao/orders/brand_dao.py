from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Brand
from my_project.auth.domain.orders.snacks import snacks_has_brand
from my_project.auth.domain.orders.snacks import Snacks



class BrandDAO(GeneralDAO):
    _domain_type = Brand

    def brand_find_snacks(self, brand_id: int):
        """
        Find solar system associated with a specific owner.
        :param brand_id: ID of the owner
        :return: List of SolarSystem objects associated with the owner
        """
        session = self.get_session()

        snackss_ids = (
            session.query(snacks_has_brand.c.snacks_id)
            .filter(snacks_has_brand.c.brand_id == brand_id)
            .all()
        )

        snacks_ids = [snacks_id for (snacks_id,) in snackss_ids]
        snacks = session.query(Snacks).filter(Snacks.id.in_(snacks_ids)).all()
        return [snacks.put_into_dto() for snacks in snacks]