from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Fundraising
from my_project.auth.domain.orders.technician import Technician
from my_project.auth.domain.orders.technician import fundraising_has_technician


class FundraisingDAO(GeneralDAO):
    _domain_type = Fundraising

    def fundraising_find_technician(self, fundraising_id: int):
        session = self.get_session()

        technicians_ids = (
            session.query(fundraising_has_technician.c.technician_id)
            .filter(fundraising_has_technician.c.fundraising_id == fundraising_id)
            .all()
        )

        technician_ids = [technician_id for (technician_id,) in technicians_ids]
        technician = session.query(Technician).filter(Technician.id.in_(technician_ids)).all()
        return [technician.put_into_dto() for technician in technician]
