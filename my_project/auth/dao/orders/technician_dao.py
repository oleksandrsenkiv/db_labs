from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Technician
from my_project.auth.domain.orders.fundraising import Fundraising
from my_project.auth.domain.orders.fundraising import fundraising_has_technician
from my_project.auth.domain.orders.coins_loading import technician_has_coins_loading
from my_project.auth.domain.orders.coins_loading import CoinsLoading
from my_project.auth.domain.orders.product_loading import ProductLoading
from my_project.auth.domain.orders.product_loading import technician_has_product_loading



class TechnicianDAO(GeneralDAO):
    _domain_type = Technician

    def technicians_find_fundraising(self, technician_id: int):
        """
        Find solar system associated with a specific owner.
        :param technician_id: ID of the owner
        :return: List of SolarSystem objects associated with the owner
        """
        session = self.get_session()

        fundraisings_ids = (
            session.query(fundraising_has_technician.c.fundraising_id)
            .filter(fundraising_has_technician.c.technician_id == technician_id)
            .all()
        )

        # Extract solar system IDs from the result
        fundraising_ids = [fundraising_id for (fundraising_id,) in fundraisings_ids]
        fundraising = session.query(Fundraising).filter(Fundraising.id.in_(fundraising_ids)).all()
        return [fundraising.put_into_dto() for fundraising in fundraising]

    def technician_find_coins_loading(self, technician_id: int):
        session = self.get_session()

        coins_loadings_ids = (
            session.query(technician_has_coins_loading.c.coins_loading_id)
            .filter(technician_has_coins_loading.c.technician_id == technician_id)
            .all()
        )

        coins_loading_ids = [coins_loading_id for (coins_loading_id,) in coins_loadings_ids]
        coins_loading = session.query(CoinsLoading).filter(CoinsLoading.id.in_(coins_loading_ids)).all()
        return [coins_loading.put_into_dto() for coins_loading in coins_loading]

    def technician_find_product_loading(self, technician_id: int):
        """
        Find solar system associated with a specific owner.
        :param technician_id: ID of the owner
        :return: List of SolarSystem objects associated with the owner
        """
        session = self.get_session()

        product_loadings_ids = (
            session.query(technician_has_product_loading.c.product_loading_id)
            .filter(technician_has_product_loading.c.technician_id == technician_id)
            .all()
        )

        product_loading_ids = [product_loadings_id for (product_loadings_id,) in product_loadings_ids]
        product_loading = session.query(ProductLoading).filter(ProductLoading.id.in_(product_loading_ids)).all()
        return [product_loading.put_into_dto() for product_loading in product_loading]
