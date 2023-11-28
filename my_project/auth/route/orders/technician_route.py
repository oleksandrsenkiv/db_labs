
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import technician_controller
from my_project.auth.domain import Technician

technician_bp = Blueprint('technician', __name__, url_prefix='/technician')


@technician_bp.get('/all')
def get_all_technician() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(technician_controller.find_all()), HTTPStatus.OK)


@technician_bp.post('')
def create_technician() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    technician = Technician.create_from_dto(content)
    technician_controller.create(technician)
    return make_response(jsonify(technician.put_into_dto()), HTTPStatus.CREATED)


@technician_bp.get('/<int:technician_id>')
def get_technician(technician_id: int) -> Response:
    """
    Gets technician by ID.
    :return: Response object
    """
    return make_response(jsonify(technician_controller.find_by_id(technician_id)), HTTPStatus.OK)

@technician_bp.get('/<int:technician_id>/fundraising_has_technician')
def get_all_technician_from_fundraising(technician_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(technician_controller.technicians_find_fundraising(technician_id)), HTTPStatus.OK)

@technician_bp.get('/<int:technician_id>/technician_has_coins_loading')
def get_all_technician_from_coins_loading(technician_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(technician_controller.technician_find_coins_loading(technician_id)), HTTPStatus.OK)


@technician_bp.get('/<int:technician_loading_id>/technician_has_product_loading')
def get_all_brands_from_snacks(technician_loading_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(technician_controller.technician_find_product_loading(technician_loading_id)), HTTPStatus.OK)


@technician_bp.put('/<int:technician_id>')
def update_technician(technician_id: int) -> Response:
    """
    Updates technician by ID.
    :return: Response object
    """
    content = request.get_json()
    technician = Technician.create_from_dto(content)
    technician_controller.update(technician_id, technician)
    return make_response("Technician updated", HTTPStatus.OK)


@technician_bp.patch('/<int:technician_id>')
def patch_technician(technician_id: int) -> Response:
    """
    Patches technician by ID.
    :return: Response object
    """
    content = request.get_json()
    technician_controller.patch(technician_id, content)
    return make_response("Technician updated", HTTPStatus.OK)


@technician_bp.delete('/<int:technician_id>')
def delete_technician(technician_id: int) -> Response:
    """
    Deletes technician by ID.
    :return: Response object
    """
    technician_controller.delete(technician_id)
    return make_response("Technician deleted", HTTPStatus.OK)
