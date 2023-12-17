
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import fundraising_controller
from my_project.auth.domain import Fundraising

fundraising_bp = Blueprint('fundraising', __name__, url_prefix='/fundraising')


@fundraising_bp.get('/all')
def get_all_fundraising() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(fundraising_controller.find_all()), HTTPStatus.OK)

@fundraising_bp.get('/<int:fundraising_id>/fundraising_has_technician')
def get_all_fundraising_from_technician(fundraising_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(fundraising_controller.fundraising_find_technician(fundraising_id)), HTTPStatus.OK)

@fundraising_bp.post('')
def create_fundraising() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    fundraising = Fundraising.create_from_dto(content)
    fundraising_controller.create(fundraising)
    return make_response(jsonify(fundraising.put_into_dto()), HTTPStatus.CREATED)


@fundraising_bp.get('/<int:fundraising_id>')
def get_fundraising(fundraising_id: int) -> Response:
    """
    Gets fundraising by ID.
    :return: Response object
    """
    return make_response(jsonify(fundraising_controller.find_by_id(fundraising_id)), HTTPStatus.OK)


@fundraising_bp.put('/<int:fundraising_id>')
def update_fundraising(fundraising_id: int) -> Response:
    """
    Updates fundraising by ID.
    :return: Response object
    """
    content = request.get_json()
    fundraising = Fundraising.create_from_dto(content)
    fundraising_controller.update(fundraising_id, fundraising)
    return make_response("Fundraising updated", HTTPStatus.OK)


@fundraising_bp.patch('/<int:fundraising_id>')
def patch_fundraising(fundraising_id: int) -> Response:
    """
    Patches fundraising by ID.
    :return: Response object
    """
    content = request.get_json()
    fundraising_controller.patch(fundraising_id, content)
    return make_response("Fundraising updated", HTTPStatus.OK)


@fundraising_bp.delete('/<int:fundraising_id>')
def delete_fundraising(fundraising_id: int) -> Response:
    """
    Deletes fundraising by ID.
    :return: Response object
    """
    fundraising_controller.delete(fundraising_id)
    return make_response("Fundraising deleted", HTTPStatus.OK)
