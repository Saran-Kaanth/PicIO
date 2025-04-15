import os

from ollama import ChatResponse, chat

class LLM_:
    """
    A class to interact with Gemma3 model from Ollama for image description generation.
    """
    def ask(self, image_data):
        """
        Requests an image description from the Gemma3 model.
        
        Args:
            image_data (str): The base64-encoded image data to describe.
        """
        try:
            response: ChatResponse=chat(model='gemma3:4b',messages=[
                {
                    "role": "user",
                    "content": """
                                Describe the given image within 250 words. It should be short and informative.
                                """,
                    "images": [image_data],
                },
            ])
            return response['message']['content']
        except Exception as e:
            print(e)
            return "Unable to generate the description for the image."
    
    # def __init__(self):
    #     try:
    #         self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    #     except Exception as e:
    #         print(e)
    #         raise

    # from dotenv import load_dotenv

    # load_dotenv(override=True)

    # def ask(self, image_data):
    #     """
    #     Requests an image description from the Groq API.

    #     Args:
    #         image_data (str): The base64-encoded image data to describe.

    #     Returns:
    #         str: The description of the image or a fallback message in case of failure.
    #     """
    #     try:
    #         if description := self.get_image_description(image_data):
    #             return description
    #         description = self.get_image_description(image_data, True)
    #         return description
    #     except Exception as e:
    #         print(e)
    #         return "Unable to generate the description for the image."

    # def get_image_description(self, image_data, is_fallback: bool = False):
    #     """
    #     Retrieves a description for the given image data using the Groq API.

    #     Args:
    #         image_data (str): The base64-encoded image data to describe.
    #         is_fallback (bool): Whether to use the fallback model (default is False).

    #     Returns:
    #         str: The description of the image or an error message if unable to generate the description.
    #     """
    #     try:
    #         chat_completion = self.client.chat.completions.create(
    #             messages=[
    #                 {
    #                     "role": "user",
    #                     "content": [
    #                         {
    #                             "type": "text",
    #                             "text": "Describe the given image within 250 characters.",
    #                         },
    #                         {
    #                             "type": "image_url",
    #                             "image_url": {
    #                                 "url": f"data:image/jpeg;base64,{image_data}",
    #                             },
    #                         },
    #                     ],
    #                 }
    #             ],
    #             model=(
    #                 "llama-3.2-90b-vision-preview"
    #                 if is_fallback
    #                 else "llama-3.2-11b-vision-preview"
    #             ),
    #             temperature=0.1,
    #         )
    #         return chat_completion.choices[0].message.content
    #     except Exception as e:
    #         print(e)
    #         return (
    #             "Unable to generate the description for the image."
    #             if is_fallback
    #             else False
    #         )
