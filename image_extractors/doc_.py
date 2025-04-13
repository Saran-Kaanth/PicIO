from spire.doc import *
from spire.doc.common import *

from models.llm import LLM_
from utils.utils import encode_image_data


class DocImageExtractor:
    def __init__(self, llm: LLM_):
        self.llm = llm

    def extract_images_pagewise_from_word(self, file_bytes):
        """
        Extracts images from a Word document, including images from each page, tables, headers, and footers.

        Args:
            file_bytes (bytes): The content of the Word (.docx) file in bytes.

        Returns:
            dict: A dictionary with page numbers and image data with descriptions.
                Includes keys for "header_footer" and "tables" as well.
        """
        document = Document()
        stream = Stream(file_bytes)
        document.LoadFromStream(stream, FileFormat.Docx)

        result = {}

        layout_doc = FixedLayoutDocument(document)

        for page_index in range(layout_doc.Pages.Count):
            layout_page = layout_doc.Pages[page_index]
            images = []

            for line_index in range(layout_page.Columns[0].Lines.Count):
                line = layout_page.Columns[0].Lines[line_index]
                paragraph = line.Paragraph

                for obj_index in range(paragraph.ChildObjects.Count):
                    obj = paragraph.ChildObjects[obj_index]
                    if isinstance(obj, DocPicture):
                        base64_image = encode_image_data(obj.ImageBytes, True)
                        image_desc = self.llm.ask(base64_image)
                        images.append((obj.ImageBytes, image_desc))
                    if isinstance(obj, Table):
                        table = document.Sections.get_Item(idx).Tables.get_Item(
                            table_idx
                        )
                        for i in range(table.Rows.Count):
                            row = table.Rows[i]
                            for j in range(row.Cells.Count):
                                cell = row.Cells[j]
                                for k in range(cell.Paragraphs.Count):
                                    paragraph = cell.Paragraphs[k]
                                    for o in range(paragraph.ChildObjects.Count):
                                        obj = paragraph.ChildObjects[o]
                                        if isinstance(obj, DocPicture):
                                            base64_image = encode_image_data(
                                                obj.ImageBytes, True
                                            )
                                            image_desc = self.llm.ask(base64_image)
                                            images.append((obj.ImageBytes, image_desc))

            result[page_index + 1] = images

        header_footer_images = []
        for idx in range(document.Sections.Count):
            header = document.Sections.get_Item(idx).HeadersFooters.Header
            footer = document.Sections.get_Item(idx).HeadersFooters.Footer

            for container in [header, footer]:
                for i in range(container.Paragraphs.Count):
                    paragraph = container.Paragraphs[i]
                    for j in range(paragraph.ChildObjects.Count):
                        obj = paragraph.ChildObjects[j]
                        if isinstance(obj, DocPicture):
                            base64_image = encode_image_data(obj.ImageBytes, True)
                            image_desc = self.llm.ask(base64_image)
                            header_footer_images.append((obj.ImageBytes, image_desc))

        result["header_footer"] = header_footer_images

        table_images = []
        for idx in range(document.Sections.Count):
            for table_idx in range(document.Sections.get_Item(idx).Tables.Count):
                table = document.Sections.get_Item(idx).Tables.get_Item(table_idx)
                for i in range(table.Rows.Count):
                    row = table.Rows[i]
                    for j in range(row.Cells.Count):
                        cell = row.Cells[j]
                        for k in range(cell.Paragraphs.Count):
                            paragraph = cell.Paragraphs[k]
                            for o in range(paragraph.ChildObjects.Count):
                                obj = paragraph.ChildObjects[o]
                                if isinstance(obj, DocPicture):
                                    base64_image = encode_image_data(
                                        obj.ImageBytes, True
                                    )
                                    image_desc = self.llm.ask(base64_image)
                                    table_images.append((obj.ImageBytes, image_desc))

        result["tables"] = table_images

        document.Close()
        return result
