from typing import List
from io import BytesIO

from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import PIL.Image

from models.llm import LLM_
from utils.utils import encode_image_data


class ExcelImageExtractor:
    def __init__(self, llm: LLM_):
        self.llm = llm

    def extract_images_from_excel_file(self, file_bytes):
        """
        Extracts images from each sheet of an Excel file and generates descriptions.

        Args:
            file_bytes (bytes): The content of the Excel (.xlsx) file in bytes.

        Returns:
            dict: A dictionary with sheet names as keys and a list of (PIL image, description) tuples as values.
        """
        output_images = {}

        workbook = load_workbook(filename=BytesIO(file_bytes))
        for sheet in workbook.worksheets:
            all_images: List[Image] = sheet._images
            image_list = []
            for img in all_images:
                image_stream = BytesIO(img._data())
                base64_image = encode_image_data(image_stream)
                image_desc = self.llm.ask(base64_image)
                image_stream.seek(0)
                pil_image = PIL.Image.open(image_stream)
                image_list.append((pil_image, image_desc))
            output_images[sheet.title] = image_list
        return output_images
