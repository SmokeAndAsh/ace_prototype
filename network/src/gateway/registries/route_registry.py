# network/src/gateway/registries/route_registry.py
from flask import Flask, request
from typing import Callable, Dict, List

class RouteRegistry:
    def __init__(self, app: Flask):
        self.app = app
        self.routes: Dict[str, Dict[str, Callable]] = {}  # path: {method: function}

    def add_route(self, path: str, methods: List[str], handler: Callable):
        # Ensure the route isn't already registered
        if path in self.routes and any(method in self.routes[path] for method in methods):
            raise ValueError(f"Route already registered for {path} with method {methods}")

        # Register the route for each method
        for method in methods:
            self.routes.setdefault(path, {})[method] = handler
            self.app.add_url_rule(path, endpoint=handler.__name__, view_func=handler, methods=methods)

    def remove_route(self, path: str, method: str = None):
        # Remove a specific method for a route or the entire route if no method specified
        if method:
            if method in self.routes.get(path, {}):
                del self.routes[path][method]
                # Additional logic might be needed to remove the route from Flask
        else:
            self.routes.pop(path, None)
            # Additional logic might be needed to remove the route from Flask

    # Additional methods as needed for listing routes, clearing the registry, etc.
