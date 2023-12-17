from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import vm_menu_controller
from my_project.auth.domain import VmMenu

vm_menu_bp = Blueprint('vm_menu', __name__, url_prefix='/vm_menu')


@vm_menu_bp.get('/all')
def get_all_vm_menus() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(vm_menu_controller.find_all()), HTTPStatus.OK)

@vm_menu_bp.get('/<int:vm_menu_id>/snacks_has_vm_menu')
def get_all_snack_availability_snacks_from_vm_menu(vm_menu_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(vm_menu_controller.vm_menu_find_snack_availability_snacks(vm_menu_id)), HTTPStatus.OK)


@vm_menu_bp.post('')
def create_vm_menu() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    vm_menu = VmMenu.create_from_dto(content)
    vm_menu_controller.create(vm_menu)
    return make_response(jsonify(vm_menu.put_into_dto()), HTTPStatus.CREATED)


@vm_menu_bp.get('/<int:vm_menu_id>')
def get_vm_menu(vm_menu_id: int) -> Response:
    """
    Gets vm_menu by ID.
    :return: Response object
    """
    return make_response(jsonify(vm_menu_controller.find_by_id(vm_menu_id)), HTTPStatus.OK)


@vm_menu_bp.put('/<int:vm_menu_id>')
def update_vm_menu(vm_menu_id: int) -> Response:
    """
    Updates vm_menu by ID.
    :return: Response object
    """
    content = request.get_json()
    vm_menu = VmMenu.create_from_dto(content)
    vm_menu_controller.update(vm_menu_id, vm_menu)
    return make_response("VmMenu updated", HTTPStatus.OK)


@vm_menu_bp.patch('/<int:vm_menu_id>')
def patch_vm_menu(vm_menu_id: int) -> Response:
    """
    Patches vm_menu by ID.
    :return: Response object
    """
    content = request.get_json()
    vm_menu_controller.patch(vm_menu_id, content)
    return make_response("VmMenu updated", HTTPStatus.OK)


@vm_menu_bp.delete('/<int:vm_menu_id>')
def delete_vm_menu(vm_menu_id: int) -> Response:
    """
    Deletes vm_menu by ID.
    :return: Response object
    """
    vm_menu_controller.delete(vm_menu_id)
    return make_response("VmMenu deleted", HTTPStatus.OK)
