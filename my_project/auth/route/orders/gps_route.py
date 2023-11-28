
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import gps_controller
from my_project.auth.domain import Gps

gps_bp = Blueprint('gps', __name__, url_prefix='/gps')


@gps_bp.get('/all')
def get_all_gps() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(gps_controller.find_all()), HTTPStatus.OK)


@gps_bp.post('')
def create_gps() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    gps = Gps.create_from_dto(content)
    gps_controller.create(gps)
    return make_response(jsonify(gps.put_into_dto()), HTTPStatus.CREATED)


@gps_bp.get('/<int:gps_id>')
def get_gps(gps_id: int) -> Response:
    """
    Gets gps by ID.
    :return: Response object
    """
    return make_response(jsonify(gps_controller.find_by_id(gps_id)), HTTPStatus.OK)


@gps_bp.put('/<int:gps_id>')
def update_gps(gps_id: int) -> Response:
    """
    Updates gps by ID.
    :return: Response object
    """
    content = request.get_json()
    gps = Gps.create_from_dto(content)
    gps_controller.update(gps_id, gps)
    return make_response("Gps updated", HTTPStatus.OK)


@gps_bp.patch('/<int:gps_id>')
def patch_gps(gps_id: int) -> Response:
    """
    Patches gps by ID.
    :return: Response object
    """
    content = request.get_json()
    gps_controller.patch(gps_id, content)
    return make_response("Gps updated", HTTPStatus.OK)


@gps_bp.delete('/<int:gps_id>')
def delete_gps(gps_id: int) -> Response:
    """
    Deletes gps by ID.
    :return: Response object
    """
    gps_controller.delete(gps_id)
    return make_response("Gps deleted", HTTPStatus.OK)
