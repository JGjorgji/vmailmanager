#! /usr/bin/env python3

from vmailmanager.main import db

class VirtualDomain(db.Model):

    __tablename__ = 'virtual_domains'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, index=True)

    def __repr__(self):
        return "{}".format(self.name)

class VirtualUser(db.Model):

    __tablename__ = 'virtual_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('virtual_domains.id', ondelete='CASCADE'), default=None, nullable=False)
    domain = db.relationship(VirtualDomain, single_parent=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True, index=True)

    def __repr__(self):
        return "{}".format(self.email)

class VirtualAliases(db.Model):

    __tablename__ = 'virtual_aliases'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('virtual_domains.id', ondelete='CASCADE'), default=None)
    domain = db.relationship(VirtualDomain, single_parent=True)
    source = db.Column(db.Text, nullable=False, index=True)
    destination = db.Column(db.Text, nullable=False)
