PLUGINS = [
    "netbox_inventory",
    "netbox_qrgen",
]

PLUGINS_CONFIG = {
    "netbox_inventory": {
        "top_level_menu": True,
        "used_status_name": "used",
        "stored_status_name": "stored",
        "sync_hardware_serial_asset_tag": True,
        "asset_import_create_purchase": True,
        "asset_import_create_device_type": True,
        "asset_import_create_module_type": True,
        "asset_import_create_inventoryitem_type": True,
        "asset_import_create_tenant": True,
        "prefill_asset_name_create_inventoryitem": True,
        "prefill_asset_tag_create_inventoryitem": True,
    },
    "netbox_qrgen": {
        "qr_with_text": True,
        "qr_text_fields": ["name", "serial"],
        "qr_font": "TahomaBold",
        "qr_width": "200px",
        "qr_custom_text": None,
        "qr_text_location": "bottom",
        "qr_version": 2,
        "qr_error_correction": 2,
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
    },
}
