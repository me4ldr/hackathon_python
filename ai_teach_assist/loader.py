import json
import fitz
import tqdm
import numpy as np
import filetype
from rapidocr_onnxruntime import RapidOCR


class FileLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        if filetype.is_image(self.file_path):
            print(f"{self.file_path} is a valid image...")
            return self.load_img(self.file_path)
        elif self.file_path.endswith('.txt'):
            return self.load_text(self.file_path)
        elif filetype.guess(self.file_path).mime == 'application/pdf':
            return self.load_pdf(self.file_path)
        else:
            print('please provide supported file types: pic, pdf, txt')

    @staticmethod
    def load_img(file_path):
        resp = ""
        ocr = RapidOCR()
        result, _ = ocr(file_path)
        if result:
            ocr_result = [line[1] for line in result]
            resp += "\n".join(ocr_result)
        return resp

    @staticmethod
    def load_pdf(file_path):
        ocr = RapidOCR()
        doc = fitz.open(file_path)
        resp = ""

        b_unit = tqdm.tqdm(total=doc.page_count, desc="RapidOCRPDFLoader context page index: 0")
        for i, page in enumerate(doc):

            # 更新描述
            b_unit.set_description("RapidOCRPDFLoader context page index: {}".format(i))
            # 立即显示进度条更新结果
            b_unit.refresh()
            # TODO: 依据文本与图片顺序调整处 理方式
            text = page.get_text("")
            resp += text + "\n"

            img_list = page.get_images()
            for img in img_list:
                pix = fitz.Pixmap(doc, img[0])
                img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, -1)
                result, _ = ocr(img_array)
                if result:
                    ocr_result = [line[1] for line in result]
                    resp += "\n".join(ocr_result)

            # 更新进度
            b_unit.update(1)
        return resp

    @staticmethod
    def load_text(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()


def load_json(filename, **kwargs):
    """
    Load a JSON object from the specified file.
    :param filename: Path to the input JSON file.
    :param kwargs: Additional arguments to 'json.load'
    :return: The object deserialized from JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f, **kwargs)


if __name__ == '__main__':
    FileLoader('../assignments/quiz1_question.pdf').load()