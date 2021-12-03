from odoo import models, fields, api
from odoo.exceptions import ValidationError


class saleextend(models.Model):
    _inherit = 'sale.order'

    vrn = fields.Char(string="VRN",related="partner_id.vrn",readonly=True)
    po_no = fields.Char('Buyer Order No')

class partnerextend(models.Model):
    _inherit = 'res.partner'

    vrn = fields.Char('VRN')
    vat = fields.Char(string='TIN', index=True, help="The Tax Identification Number. Complete it if the contact is subjected to government taxes. Used in some legal statements.")

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Customer/Supplier Name already exists!')
    ]

    # _sql_constraints = [
    #     ('unique_vrn', 'unique (vrn)', 'Customer/Supplier VRN already exists!')

class commpanyextend(models.Model):
    _inherit = 'res.company'

    vrn = fields.Char('Company VRN')
    vat = fields.Char(related='partner_id.vat', string="TIN", readonly=False)

class invoiceexted(models.Model):
    _inherit = 'account.move'

    vrn = fields.Char(string="VRN",related="partner_id.vrn",readonly=True)
    po_no = fields.Char(string="Buyer Order No",related="sale_id.po_no")
    delivery_ids = fields.Many2many('stock.picking', string='Delivery Note')

    sale_id = fields.Many2one('sale.order',string="Sale Order", compute='compute_sale_id')

    def compute_sale_id(self):
        self.sale_id = False
        if self.type == 'out_invoice':
            if self.invoice_origin:
                sale = self.env['sale.order'].search([['name','=',self.invoice_origin]],limit=1)
                self.sale_id = sale.id
        return


	
