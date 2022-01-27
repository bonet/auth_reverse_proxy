# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest
from user.models import User
from oauth2_token.models import OAuth2Token
from partner.models import Partner
from user.models import User

class TestUser:
    def test_get_by_id(self, initial_user):
        user = User.create(fullname="Foo Bar", email="foo@bar.com", password="mypassword".encode('ascii'))

        retrieved = User.query.filter(User.id == user.id).one()
        assert retrieved == user

    def test_check_password(self, initial_user):
        assert initial_user.check_password("foobarbaz123") is False
        assert initial_user.check_password("hello123") is True

    def test_user_data(self, initial_user):
        assert initial_user.fullname == None
        assert initial_user.address == None
        assert initial_user.phone == None

        fullname_str = 'John Doe'
        address_str = '12 Elm St'
        phone_str = '202-1111111'
        initial_user.fullname = fullname_str
        initial_user.address = address_str
        initial_user.phone = phone_str
        initial_user.save()

        user = User.query.filter(User.id == initial_user.id).one()
        assert user.fullname == fullname_str
        assert user.address == address_str
        assert user.phone == phone_str
