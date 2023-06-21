from django.conf import settings
from extras.plugins import PluginTemplateExtension

from .utils import generate_qrcode, get_base64

plugin_settings = settings.PLUGINS_CONFIG.get("netbox_qrgen", {})


class QRGen(PluginTemplateExtension):
    def get_url(self) -> str:
        obj = self.context["object"]
        request = self.context["request"]
        url: str = request.build_absolute_uri(obj.get_absolute_url())

        return url

    def get_qrcode(self, url: str) -> str:
        img = generate_qrcode(url=url, **plugin_settings)
        b64 = get_base64(img)

        return b64

    def right_page(self):
        qr_img = self.get_qrcode(self.get_url())
        return self.render(
            "netbox_qrgen/qrgen.html",
            extra_context={"image": qr_img},
        )


class QRGenDevice(QRGen):
    model = "dcim.device"
    # kind = "device"


class QRGenRack(QRGen):
    model = "dcim.rack"
    # kind = "rack"


class QRGenCable(QRGen):
    model = "dcim.cable"
    # kind = "cable"


class QRGenInventoryItem(QRGen):
    model = "dcim.inventoryitem"
    # kind = "inventoryitem"


class QRGenCircuit(QRGen):
    model = "circuits.circuit"
    # kind = "circuit"


template_extensions = [
    QRGenDevice,
    QRGenRack,
    QRGenCable,
    QRGenInventoryItem,
    QRGenCircuit,
]
