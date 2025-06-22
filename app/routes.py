from flask import Blueprint, jsonify, request
from .models import db, Episode, Guest, Appearance

api_bp = Blueprint('api', __name__)

@api_bp.route("/episodes")
def get_episodes():
    return jsonify([e.to_dict() for e in Episode.query.all()])

@api_bp.route("/episodes/<int:id>")
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    data = episode.to_dict()
    data["appearances"] = [a.to_dict() for a in episode.appearances]
    return jsonify(data)

@api_bp.route("/guests")
def get_guests():
    return jsonify([g.to_dict() for g in Guest.query.all()])

@api_bp.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()
    try:
        rating = data["rating"]
        guest_id = data["guest_id"]
        episode_id = data["episode_id"]
    except KeyError:
        return jsonify({"errors": ["Missing data"]}), 400

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    errors = appearance.validate()
    if errors:
        return jsonify({"errors": errors}), 400

    db.session.add(appearance)
    db.session.commit()
    return jsonify(appearance.to_dict()), 201
