from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import CoinsLoading
from my_project.auth.domain.orders.technician import technician_has_coins_loading
from my_project.auth.domain.orders.technician import Technician


class CoinsLoadingDAO(GeneralDAO):
    _domain_type = CoinsLoading

    def coins_loading_find_technician(self, coins_loading_id: int):
        session = self.get_session()

        technicians_ids = (
            session.query(technician_has_coins_loading.c.technician_id)
            .filter(technician_has_coins_loading.c.coins_loading_id == coins_loading_id)
            .all()
        )

        technician_ids = [technician_id for (technician_id,) in technicians_ids]
        technician = session.query(Technician).filter(Technician.id.in_(technician_ids)).all()
        return [technician.put_into_dto() for technician in technician]