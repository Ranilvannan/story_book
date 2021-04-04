from odoo import models, fields, api, exceptions

PROJECT = [("project.site1", "Project Site 1"),
           ("project.site2", "Project Site 2")]


class ValidationService(models.TransientModel):
    _name = "validation.service"
    _description = "Validation Service"

    project = fields.Selection(selection=PROJECT, string="Project", required=1)

    def trigger_validation(self):
        if self.project == "project.site1":
            self.project_site1_validation(site_model="project.site1")

    def project_site1_validation(self, site_model):
        recs = self.env[site_model].search([("is_valid", "=", False)])[:100]

        for rec in recs:
            if rec.title \
                    and rec.preview \
                    and rec.content_ids \
                    and rec.category_id \
                    and rec.site_title \
                    and rec.site_preview \
                    and rec.site_url:
                rec.write({"is_valid": True})