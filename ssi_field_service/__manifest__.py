# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Field Service",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_ready_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_transaction_terminate_mixin",
        "ssi_transaction_date_duration_mixin",
        "ssi_transaction_partner_mixin",
        "ssi_localdict_mixin",
        "ssi_frequency",
        "base_automation",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/approval_template_data.xml",
        "data/policy_template_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_automation_data.xml",
        "menu.xml",
        "views/field_service_type_views.xml",
        "views/field_service_role_views.xml",
        "views/field_service_role_set_views.xml",
        "views/field_service_time_slot_views.xml",
        "views/field_service_order_views.xml",
        "views/group_field_service_order_views.xml",
    ],
    "demo": [
        "demo/field_service_time_slot_demo.xml",
        "demo/field_service_role_demo.xml",
        "demo/field_service_role_set_demo.xml",
        "demo/field_service_type_demo.xml",
    ],
}
