# src/cognition/focus/focus_actions/action_web.py


class ActionWeb:

    async def search_web(self):
        """
        Follows a given URL or searches the web.
        """
        pass

    async def get_web_content(self):
        """
        Retrieves web contents from given URL.
        """
        pass

    async def save_web_content(self):
        """
        Saves contents retrieved from given URL.
        """
        pass


class ActionWebMedia:

    async def find_gif(self):
        """
        Uses Giphy API to find contextually-appropriate GIF.
        """
        pass

    async def generate_image(self):
        """
        Generates image using local model or external API.
        """
        pass

    async def send_web_media(self):
        """
        Replaces the media prompt with URL to GIF or generated image.
        """
        pass
