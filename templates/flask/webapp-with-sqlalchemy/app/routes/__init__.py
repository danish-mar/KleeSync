from app.routes.static_routes import static_route_bp


def register_blueprints(app):
    # register routes here...
    app.register_blueprint(static_route_bp, url_prefix="/")