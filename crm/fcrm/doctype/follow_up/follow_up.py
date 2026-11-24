# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FollowUp(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        coment: DF.SmallText | None
        follow_up_date: DF.Date | None
        leads: DF.Link
        leads_name: DF.Data | None
        next_follow_up_date: DF.Date | None
        prospect_owner: DF.Link | None
        status: DF.Literal["Tertarik", "Tidak Tertarik", "Belum Tertarik", "Broadcast Whatsapp", "Re-Follow Up", "Terdaftar di PTN/PTS/Institusi", "Read Tidak di Respon", "Callback", "Telpon Tidak di Angkat", "Telpon Tidak Aktif", "Telpon di Tolak", "Ingin Konsultasi ke Kampus", "Wrong Number", "Menunggu PTN/Instansi", "Minat Beasiswa", "Lain-Lain"]
        subject: DF.Literal["Whatsapp", "Call", "Email", "Visit"]
    # end: auto-generated types
    pass
	# def validate(self):
	# 	if self.leads:
	# 		lead = frappe.get_doc("CRM Lead", self.leads)
	# 		if lead.table_cufc:
	# 			for row in lead.table_cufc:
	# 				if row.fu_detail == self.name:
	# 					frappe.throw(f"Follow Up {self.name} already exists in {lead.name}")
						
	# 		lead.append("table_cufc",{
	# 			"prospect_owner": self.prospect_owner,
	# 			"follow_up_date": self.follow_up_date,
	# 			"next_follow_up_date": self.next_follow_up_date,
	# 			"follow_up_result": self.status,
	# 			"comment": self.coment,
	# 			"fu_detail": self.name
	# 		})
	# 		lead.db_update()
	# 		lead.update_children()
	# 		frappe.msgprint(f"Follow Up added to {lead.name}")
