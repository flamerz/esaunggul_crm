# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FollowUp(Document):
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
