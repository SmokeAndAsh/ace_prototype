# network/src/gateway/clients/discord_cli.py

import discord
import requests
import os
from src.gateway.clients.comm_clients.comm_cli import CommunicationClient
from src.gateway.clients.lang_clients.lang_cli import LanguageClient
from src.error_handling.client_error_handler import (
    ClientError, ClientAuthenticationError, ClientConnectionError, ClientRequestError
)

class DiscordClient(CommunicationClient):
    def __init__(self, intents, *args, **kwargs):
        super().__init__("DiscordClient", *args, **kwargs)
        self.intents = intents  # Discord specific intents

    def test_connection(self):
            try:
                response = requests.get('https://discord.com/api/v9/gateway')
            if response.status_code == 200:
                print("Testing Discord Client connectivity successful.")
                return True
            elif response.status_code == 401:
                raise ClientAuthenticationError("Discord", "Invalid or missing token")
            else:
                raise ClientRequestError("Discord", f"Status Code: {response.status_code}")
            except requests.exceptions.HTTPError as e:
                raise ClientRequestError("Discord", "HTTP Error occurred")
            except Exception as e:
                raise ClientError(f"Unknown error testing Discord Client: {e}")

    def test_client(self):
        # Pinging Discord server
        return self.test_connection()

    def start_client(self):
        # Implement start logic for Discord client
        print(f"Starting {self.name}...")
        # Discord-specific startup logic
        return True

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.user:
            return

        # Ignore non-text messages or system messages
        if not message.content:
            print("No text content in the message.")
            return

        print(f"Received message content: '{message.content}'")

        response_text = await self.generate_response(message.content)
        await message.channel.send(response_text)

    async def generate_response(self, input_text):
        try:
            response = self.text_generator(input_text, "kayra-v1", {
                "use_string": True,
                "temperature": 1,
                "min_length": 1,
                "max_length": 100
            })

            if 'output' in response:
                return response['output']  # Changed from 'result' to 'output'
            else:
                print("Full response from NovelAI:", response)
                return "Error: Unable to generate response. Check logs for details."
        except Exception as e:
            print(f"Error in generating response: {e}")
            return "An exception occurred. Check logs for details."

def setup_discord_client(novelai_client):
    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    intents.guilds = True

    discord_client = DiscordClient(novelai_client.generate_text, intents)
    discord_client.run(discord_token)

def start_discord_client():
    novelai_client = NovelAIClient()

    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    intents.guilds = True

    discord_token = os.getenv('DISCORD_TOKEN')
    discord_client = DiscordClient(novelai_client.generate_text, intents)
    discord_client.run(discord_token)

if __name__ == "__main__":
    language_client = LanguageClient()
    setup_discord_client(novelai_client)
