#! /usr/bin/env python3

from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField
import crypt
import os
import shutil

class VirtualDomainAdmin(ModelView):
    def on_model_change(self, form, model, is_created):
        domain_path = '/var/vmail/{}'.format(model.name)
        if not os.path.exists(domain_path):
            os.mkdir(domain_path)
        shutil.chown(domain_path, 'vmail', 'vmail')

class VirtualUserAdmin(ModelView):
    column_filters = ('username', 'email', 'password')
    form_excluded_columns = ('last_name', 'email')

    form_overrides = {
        'password': PasswordField,
    }

    form_widget_args = {
        'email': {
            'readonly': True
        },
    }

    def on_model_change(self, form, model, is_created):
        model.password = crypt.crypt(model.password, salt=crypt.METHOD_SHA256)
        model.email = '{}@{}'.format(model.username, model.domain)
        user_path = '/var/vmail/{}/{}'.format(model.domain, model.username)
        if not os.path.exists(user_path):
            os.mkdir(user_path)
        shutil.chown(user_path, 'vmail', 'vmail')

class VirtualAliasesAdmin(ModelView):
    column_filters = ('source', 'destination')