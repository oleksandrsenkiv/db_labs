from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import vending_machine_controller
from my_project.auth.domain import VendingMachine

vending_machine_bp = Blueprint('vending_machine', __name__, url_prefix='/vending_machine')


@vending_machine_bp.get('/all')
def get_all_vending_machines() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(vending_machine_controller.find_all()), HTTPStatus.OK)


@vending_machine_bp.post('')
def create_vending_machine() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    vending_machine = VendingMachine.create_from_dto(content)
    vending_machine_controller.create(vending_machine)
    return make_response(jsonify(vending_machine.put_into_dto()), HTTPStatus.CREATED)


@vending_machine_bp.get('/<int:vending_machine_id>')
def get_vending_machine(vending_machine_id: int) -> Response:
    """
    Gets vending_machine by ID.
    :return: Response object
    """
    return make_response(jsonify(vending_machine_controller.find_by_id(vending_machine_id)), HTTPStatus.OK)


@vending_machine_bp.put('/<int:vending_machine_id>')
def update_vending_machine(vending_machine_id: int) -> Response:
    """
    Updates vending_machine by ID.
    :return: Response object
    """
    content = request.get_json()
    vending_machine = VendingMachine.create_from_dto(content)
    vending_machine_controller.update(vending_machine_id, vending_machine)
    return make_response("VendingMachine updated", HTTPStatus.OK)


@vending_machine_bp.patch('/<int:vending_machine_id>')
def patch_vending_machine(vending_machine_id: int) -> Response:
    """
    Patches vending_machine by ID.
    :return: Response object
    """
    content = request.get_json()
    vending_machine_controller.patch(vending_machine_id, content)
    return make_response("VendingMachine updated", HTTPStatus.OK)


@vending_machine_bp.delete('/<int:vending_machine_id>')
def delete_vending_machine(vending_machine_id: int) -> Response:
    """
    Deletes vending_machine by ID.
    :return: Response object
    """
    vending_machine_controller.delete(vending_machine_id)
    return make_response("VendingMachine deleted", HTTPStatus.OK)
