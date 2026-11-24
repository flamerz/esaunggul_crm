# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FollowUpDetail(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		comment: DF.SmallText | None
		follow_up_date: DF.Datetime | None
		follow_up_result: DF.Literal["Tertarik", "Tidak Tertarik", "Belum Tertarik", "Broadcast Whatsapp", "Re-Follow Up", "Terdaftar di PTN/PTS/Institusi", "Wrong Number", "Menunggu PTN/Instansi", "Minat Beasiswa", "Read Tidak di Respon", "Callback", "Telpon Tidak di Angkat", "Telpon Tidak Aktif", "Telpon di Tolak", "Ingin Konsultasi ke Kampus", "Broadcast Email", "Lain-Lain"]
		fu_detail: DF.Data | None
		next_follow_up_date: DF.Date | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		prospect_owner: DF.Link | None
	# end: auto-generated types
	pass
