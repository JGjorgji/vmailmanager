#! /usr/bin/env python3

from flask_admin.contrib.sqla import ModelView
import crypt

class VirtualDomainAdmin(ModelView):
    pass

class VirtualUserAdmin(ModelView):
    column_filters = ('email', 'password')

    def on_model_change(self, form, model, is_created):
        model.password = crypt.crypt(model.password, salt=crypt.METHOD_SHA256)

class VirtualAliasesAdmin(ModelView):
    column_filters = ('source', 'destination')