# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest
from user.models import User
from oauth2_token.models import OAuth2Token
from partner.models import Partner
from user.models import User

class TestPartner:
    def test_get_by_id(self, initial_user):
        partner_name = 'shopee'
        partner_scopes = {
                '/api/v1/products': ['GET'],
                '/api/v1/orders': ['GET', 'POST']
            }
        partner_secret_key = 'XYZ'
        partner = Partner.create(
            name=partner_name,
            scopes=partner_scopes,
            secret_key=partner_secret_key
            )

        retrieved = Partner.query.filter(Partner.id == partner.id).one()
        assert retrieved == partner
        assert retrieved.name == partner_name
        assert retrieved.scopes == partner_scopes
        assert retrieved.secret_key == partner_secret_key
