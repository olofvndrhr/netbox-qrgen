from extras.plugins import PluginConfig


class NetBoxQRGenConfig(PluginConfig):
    name = "netbox_qrgen"
    verbose_name = "NetBox QRGen"
    description = "NetBox plugin to generate QR codes for assets"
    version = "0.0.1"
    base_url = "qrgen"
    min_version = "3.4.0"
    author = "Ivan Schaller"
    author_email = "ivan@schaller.sh"
    default_settings = {
        "qr_with_text": True,
        "qr_text_fields": ["name", "serial"],
        "qr_font": "Tahoma",
        "qr_width": "200px",
        "qr_custom_text": None,
        "qr_text_location": "right",
        "qr_version": 2,
        "qr_error_correction": 1,
        "qr_box_size": 6,
        "qr_border_size": 4,
        "labels": {
            "dcim.cable": [
                "tenant",
                "a_terminations.device",
                "a_terminations.name",
                "b_terminations.device",
                "b_terminations.name",
            ],
            "dcim.rack": [
                "tenant",
                "site",
                "facility_id",
                "name",
            ],
            "dcim.device": ["tenant", "name", "serial"],
            "dcim.inventoryitem": ["tenant", "name", "serial"],
            "circuits.circuit": ["tenant", "name", "serial"],
        },
    }


config = NetBoxQRGenConfig
