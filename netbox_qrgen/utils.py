import base64
from io import BytesIO
from typing import Union

import qrcode
from qrcode.image.pure import PyPNGImage
from qrcode.image.svg import SvgPathFillImage


def generate_qrcode(url: str, **kwargs) -> PyPNGImage:
    qr = qrcode.QRCode(
        version=kwargs["qr_version"],
        error_correction=kwargs["qr_error_correction"],
        box_size=kwargs["qr_box_size"],
        border=kwargs["qr_border_size"],
        image_factory=PyPNGImage,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img


def get_base64(img: Union[SvgPathFillImage, PyPNGImage]) -> str:
    stream = BytesIO()
    img.save(stream)
    base64_value = base64.b64encode(stream.getvalue()).decode(encoding="ascii")

    return base64_value
