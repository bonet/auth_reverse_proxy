# -*- coding: utf-8 -*-
"""Model unit tests."""
from datetime import datetime as dt

import pytest
from user.models import User
from oauth2_token.models import OAuth2Token
from partner.models import Partner
from user.models import User

class TestOAuth2Token:
    def test_get_by_id(self, initial_user):
        partner_scopes = {
                '/api/v1/products': ['GET'],
                '/api/v1/orders': ['GET', 'POST']
            }
        partner_name = 'shopee'
        partner_secret_key = 'XYZ'

        partner = Partner.create(
            name=partner_name,
            scopes=partner_scopes,
            secret_key=partner_secret_key
            )

        token_expires_in = 3600

        partner_scopes = {
                '/api/v1/products': ['GET'],
                '/api/v1/orders': ['GET', 'POST']
            }

        oauth2_token = OAuth2Token.create(
            scopes=partner_scopes,
            expires_in=token_expires_in,
            user_id=initial_user.id,
            partner_id=partner.id
            )

        retrieved = OAuth2Token.query.filter(OAuth2Token.id == oauth2_token.id).one()
        assert retrieved == oauth2_token
        assert retrieved.auth_code == oauth2_token.auth_code
        assert retrieved.scopes == oauth2_token.scopes
        assert retrieved.issued_at == oauth2_token.issued_at
        assert retrieved.expires_in == token_expires_in
        assert retrieved.user == initial_user
        assert retrieved.partner == partner
