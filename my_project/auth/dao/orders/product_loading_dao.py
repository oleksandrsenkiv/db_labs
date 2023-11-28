from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import ProductLoading
from my_project.auth.domain.orders.technician import technician_has_product_loading
from my_project.auth.domain.orders.technician import Technician

class ProductLoadingDAO(GeneralDAO):
    _domain_type = ProductLoading

    def product_loading_find_technician(self, product_loading_id: int):
        """
        Find solar system associated with a specific owner.
        :param product_loading_id: ID of the owner
        :return: List of SolarSystem objects associated with the owner
        """
        session = self.get_session()

        technicians_ids = (
            session.query(technician_has_product_loading.c.technician_id)
            .filter(technician_has_product_loading.c.product_loading_id == product_loading_id)
            .all()
        )

        technician_ids = [technician_id for (technician_id,) in technicians_ids]
        technician = session.query(Technician).filter(Technician.id.in_(technician_ids)).all()
        return [technician.put_into_dto() for technician in technician]