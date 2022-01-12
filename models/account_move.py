from odoo import fields,models,api
import convert_numbers
# from deep_translator import GoogleTranslator
from uuid import uuid4
import qrcode
from odoo.exceptions import UserError

import base64
import logging

from lxml import etree

logger = logging.getLogger(__name__)

from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
from odoo.tools import float_compare, date_utils, email_split, email_re
from odoo.tools.misc import formatLang, format_date, get_lang
from odoo import fields, models
import requests
import json
from datetime import datetime,date



class AccountMove(models.Model):
    _inherit = 'account.move'
    _order = "invoice_nat_times desc"

    invoice_nat_times = fields.Datetime(string="Date with Time")

    def update_date_all(self):
        my_total = 0
        for each in self.env['account.move'].search([]):
            if my_total <= 10:
                my_total += 1
                if each.invoice_date_time:
                    print(each,'fgfgfth')
                    import datetime
                    date = datetime.date(each.invoice_date.year, each.invoice_date.month, each.invoice_date.day)
                    time = datetime.time(each.datetime_field.time().hour, each.datetime_field.time().minute)
                    each.invoice_nat_times = datetime.datetime.combine(date, time)
