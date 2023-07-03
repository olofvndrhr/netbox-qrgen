from django.conf import settings
from extras.plugins import PluginTemplateExtension

from .utils import generate_qrcode, get_base64

plugin_settings = settings.PLUGINS_CONFIG.get("netbox_qrgen", {})


class QRGen(PluginTemplateExtension):
    def _get_url(self) -> str:
        obj = self.context["object"]
        request = self.context["request"]
        url: str = request.build_absolute_uri(obj.get_absolute_url())

        return url

    def _get_qrcode(self, url: str) -> tuple[str, str]:
        img_png, img_svg = generate_qrcode(url=url, **plugin_settings)
        b64_png = get_base64(img_png)
        b64_svg = get_base64(img_svg)

        return b64_png, b64_svg

    def right_page(self):
        b64_png, b64_svg = self._get_qrcode(self._get_url())
        return self.render(
            "netbox_qrgen/qrgen.html",
            extra_context={
                "image_width": plugin_settings["qr_width"],
                "image_png": b64_png,
                "image_svg": b64_svg,
            },
        )


class QRGenLocation(QRGen):
    model = "dcim.location"


class QRGenRack(QRGen):
    model = "dcim.rack"


class QRGenDevice(QRGen):
    model = "dcim.device"


class QRGenPowerFeed(QRGen):
    model = "dcim.powerfeed"


class QRGenPowerPanel(QRGen):
    model = "dcim.powerpanel"


class QRGenCable(QRGen):
    model = "dcim.cable"


class QRGenInventoryItem(QRGen):
    model = "dcim.inventoryitem"


class QRGenCircuit(QRGen):
    model = "circuits.circuit"


class QRGenVirtualizationCluster(QRGen):
    model = "virtualization.cluster"


class QRGenPluginInventoryAsset(QRGen):
    model = "netbox_inventory.asset"


class QRGenPluginInventoryItemType(QRGen):
    model = "netbox_inventory.inventoryitemtype"


template_extensions = [
    QRGenLocation,
    QRGenRack,
    QRGenDevice,
    QRGenPowerFeed,
    QRGenPowerPanel,
    QRGenCable,
    QRGenInventoryItem,
    QRGenCircuit,
    QRGenVirtualizationCluster,
    QRGenPluginInventoryAsset,
    QRGenPluginInventoryItemType,
]
