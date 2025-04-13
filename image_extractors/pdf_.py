import fitz

from models.llm import LLM_
from utils.utils import encode_image_data


class PDFImageExtractor:
    def __init__(self, llm: LLM_):
        self.llm = llm

    def extract_images_pagewise(self, pdf_bytes):
        """
        Extracts images from each page of a PDF file and generates descriptions.

        Args:
            pdf_bytes (bytes): The content of the PDF file in bytes.

        Returns:
            dict: A dictionary with page numbers as keys and a list of image info dictionaries as values.
                Each image info contains image bytes, extension, xref, and a description.
        """
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        pagewise_images = {}

        for page_number in range(len(doc)):
            page = doc[page_number]
            images = page.get_images(full=True)
            image_list = []

            for img in images:
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                base64_image = encode_image_data(base_image["image"], True)
                image_desc = self.llm.ask(base64_image)
                ext = base_image["ext"]
                image_list.append(
                    {
                        "image_bytes": image_bytes,
                        "ext": ext,
                        "xref": xref,
                        "description": image_desc,
                    }
                )

            pagewise_images[page_number + 1] = image_list

        return pagewise_images
