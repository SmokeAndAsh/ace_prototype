# src/network/network_start.py
import sys
import logging
from src.network_diagnostics import run_diagnostics
from src.connections.http_connection import HttpConnection
from src.connections.kafka_connection import KafkaConnection
from src.gateway.gateway_main import GatewayManager
from src.gateway.client_handler import CommunicationHandler
from src.gateway.clients.terminal_cli import TerminalClient
from src.gateway.clients.web_cli import WebClient

logging.basicConfig(level=logging.INFO)

def start_network_module():
    diagnostics_report = run_diagnostics()

    if diagnostics_report['status'] == 'success':
        logging.info("Starting Network Module...")
        GatewayManager.start_gateway()
        HttpConnection.start_http()
        KafkaConnection.start_kafka()
        TerminalClient.start_terminal()
        #Check config before `start_web`
        #Ignore if WEB_CLIENT_ENABLED: "False"
        WebClient.start_web()
        CommunicationHandler.start_comm_client()
    else:
        logging.error("Network Module failed to start. Diagnostics report: {}".format(diagnostics_report))
        sys.exit(1)

if __name__ == "__main__":
    start_network_module()