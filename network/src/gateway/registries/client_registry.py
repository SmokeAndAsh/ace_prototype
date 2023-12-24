# network/src/gateway/registries/client_registry.py
from dataclasses import dataclass, field
from typing import Type, Dict, Optional
from src.gateway.clients.base_cli import BaseClient

class ClientRegistry:
    def __init__(self):
        self._registry: Dict[str, Type[BaseClient]] = {}

    def register(self, client_type: str, client_class: Type[BaseClient]):
        if client_type in self._registry:
            raise ValueError(f"Client type '{client_type}' is already registered.")
        self._registry[client_type] = client_class

    def get_client_class(self, client_type: str) -> Optional[Type[BaseClient]]:
        return self._registry.get(client_type)

@dataclass
class SystemClientSpec:
    name: str

@dataclass
class LanguageClientSpec:
    name: str
    model: Optional[str] = None
    parameters: Dict[str, str] = field(default_factory=dict)

@dataclass
class CommunicationClientSpec:
    name: str

@dataclass
class WebClientSpec:
    name: str
