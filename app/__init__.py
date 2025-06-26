from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)

    from .models import Episode, Guest, Appearance

    class EpisodesResource(Resource):
        def get(self):
            episodes = Episode.query.all()
            return [e.to_dict() for e in episodes], 200

    class EpisodeResource(Resource):
        def get(self, id):
            episode = Episode.query.get(id)
            if not episode:
                return {"error": "Episode not found"}, 404
            data = episode.to_dict()
            data["appearances"] = [a.to_dict() for a in episode.appearances]
            return data, 200

    class GuestsResource(Resource):
        def get(self):
            guests = Guest.query.all()
            return [g.to_dict() for g in guests], 200

    class AppearancesResource(Resource):
        def post(self):
            data = request.get_json()
            try:
                rating = data["rating"]
                guest_id = data["guest_id"]
                episode_id = data["episode_id"]
            except (KeyError, TypeError):
                return {"errors": ["Missing data"]}, 400

            appearance = Appearance(
                rating=rating,
                guest_id=guest_id,
                episode_id=episode_id
            )
            errors = appearance.validate()
            if errors:
                return {"errors": errors}, 400

            db.session.add(appearance)
            db.session.commit()
            return appearance.to_dict(), 201

    class AppearanceResource(Resource):
        def delete(self, id):
            appearance = Appearance.query.get(id)
            if not appearance:
                return {"error": "Appearance not found"}, 404
            db.session.delete(appearance)
            db.session.commit()
            return {}, 204

    # Register endpoints
    api.add_resource(EpisodesResource, "/episodes")
    api.add_resource(EpisodeResource, "/episodes/<int:id>")
    api.add_resource(GuestsResource, "/guests")
    api.add_resource(AppearancesResource, "/appearances")
    api.add_resource(AppearanceResource, "/appearances/<int:id>")

    return app
