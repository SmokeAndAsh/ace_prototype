# src/network/network_diagnostics.py
import sys
import logging
from src.connections.http_connection import HttpConnection
from src.connections.kafka_connection import KafkaConnection
from src.gateway.gateway_main import GatewayManager
from src.gateway.client_handler import CommunicationHandler, LanguageHandler
from src.gateway.clients.terminal_cli import TerminalClient
from src.gateway.clients.web_cli import WebClient

def run_diagnostics():
    logging.info("Running Network Module Diagnostics...")
    all_tests_pass = all([
        GatewayManager.test_gateway(),
        HttpConnection.test_connection(),
        KafkaConnection.test_connection(),
        TerminalClient.test_client(),
        WebClient.test_client(),
        CommunicationHandler.test_client(),
        LanguageHandler.test_client()
    ])
    return {'status': 'success' if all_tests_pass else 'failed'}