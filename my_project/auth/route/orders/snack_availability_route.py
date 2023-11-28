
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import snack_availability_controller
from my_project.auth.domain import SnackAvailability

snack_availability_bp = Blueprint('snack_availability', __name__, url_prefix='/snack_availability')


@snack_availability_bp.get('/all')
def get_all_snack_availability() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(snack_availability_controller.find_all()), HTTPStatus.OK)

@snack_availability_bp.get('/<int:snack_availability_id>/snacks_has_vm_menu')
def get_all_snacks_vm_menu_from_snack_availability(snack_availability_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(snack_availability_controller.snack_availability_find_vm_menu_snacks(snack_availability_id)), HTTPStatus.OK)

@snack_availability_bp.post('')
def create_snack_availability() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    snack_availability = SnackAvailability.create_from_dto(content)
    snack_availability_controller.create(snack_availability)
    return make_response(jsonify(snack_availability.put_into_dto()), HTTPStatus.CREATED)


@snack_availability_bp.get('/<int:snack_availability_id>')
def get_snack_availability(snack_availability_id: int) -> Response:
    """
    Gets snack_availability by ID.
    :return: Response object
    """
    return make_response(jsonify(snack_availability_controller.find_by_id(snack_availability_id)), HTTPStatus.OK)


@snack_availability_bp.put('/<int:snack_availability_id>')
def update_snack_availability(snack_availability_id: int) -> Response:
    """
    Updates snack_availability by ID.
    :return: Response object
    """
    content = request.get_json()
    snack_availability = SnackAvailability.create_from_dto(content)
    snack_availability_controller.update(snack_availability_id, snack_availability)
    return make_response("SnackAvailability updated", HTTPStatus.OK)


@snack_availability_bp.patch('/<int:snack_availability_id>')
def patch_snack_availability(snack_availability_id: int) -> Response:
    """
    Patches snack_availability by ID.
    :return: Response object
    """
    content = request.get_json()
    snack_availability_controller.patch(snack_availability_id, content)
    return make_response("SnackAvailability updated", HTTPStatus.OK)


@snack_availability_bp.delete('/<int:snack_availability_id>')
def delete_snack_availability(snack_availability_id: int) -> Response:
    """
    Deletes snack_availability by ID.
    :return: Response object
    """
    snack_availability_controller.delete(snack_availability_id)
    return make_response("SnackAvailability deleted", HTTPStatus.OK)
