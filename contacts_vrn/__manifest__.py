
{
    "name": "Contact VRN/PON",
    "summary": "Add VRN / Po No / DN fields ",
    'description': """
        - Add VRN (Vat Registration Number) field to contacts.
        - Add Buyer Order Number (Po No) to Sales Order and Invoice.
        - Add Delivery Note to Invoice.
    """,
    "version": "14.0.1.0.0",
    "License": "AGPL-3.0",
    "category": "Customer Relationship Management",
    "author": "Stephen Ngailo, StiloTech Limited",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": ["base","sale_management","stock"],
    "data": ["views/res_partner.xml"],
    'images': ['static/description/icon.png'],
}
