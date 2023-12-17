from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import ProductLoading
from my_project.auth.domain.orders.technician import technician_has_product_loading
from my_project.auth.domain.orders.technician import Technician
from sqlalchemy import text


class ProductLoadingDAO(GeneralDAO):
    _domain_type = ProductLoading

    def product_loading_find_technician(self, product_loading_id: int):

        session = self.get_session()

        technicians_ids = (
            session.query(technician_has_product_loading.c.technician_id)
            .filter(technician_has_product_loading.c.product_loading_id == product_loading_id)
            .all()
        )

        technician_ids = [technician_id for (technician_id,) in technicians_ids]
        technician = session.query(Technician).filter(Technician.id.in_(technician_ids)).all()
        return [technician.put_into_dto() for technician in technician]


    def get_product_loading_stats(self, stats_type: str):
        try:
            session = self.get_session()
            sql_expression = text("CALL find_product_loading_stats(:stats_type)")
            result = session.execute(sql_expression, {'stats_type': stats_type}).scalar()
            return result
        except Exception as e:
            print(f"Error with getting stats: {e}")
