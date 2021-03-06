import json
import pytest
import requests
import time

from pages.moderator import Moderator
from pages.mozillians import Mozillians
from pages.reps import Reps
from pages.standups import Standups
from pages.rptest import RpTest
from tests import conftest

TIME_TO_WAIT_FOR = 900


class TestLogin:

    @pytest.mark.nondestructive
    def test_login_testrp(self, selenium, ldap, token, urls):
        test = RpTest(selenium, urls['testRP'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        two_factor_authentication_page = test.login_with_ldap(ldap['email'], ldap['password'])
        two_factor_authentication_page.enter_passcode(current_passcode)
        while two_factor_authentication_page.is_error_message_displayed:
            two_factor_authentication_page.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            two_factor_authentication_page.enter_passcode(conftest.passcode(ldap['secret_seed']))
        assert test.is_logout_button_displayed
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        last_user_log_type = json.loads(user_logs.content)[0]['type']
        assert last_user_log_type == "ssa"
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()

    @pytest.mark.nondestructive
    def test_login_mozillians(self, selenium, ldap, token, urls):
        test = Mozillians(selenium, urls['mozillians'])
        two_factor_authentication_page = test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        two_factor_authentication_page.enter_passcode(current_passcode)
        while two_factor_authentication_page.is_error_message_displayed:
            two_factor_authentication_page.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            two_factor_authentication_page.enter_passcode(conftest.passcode(ldap['secret_seed']))
        assert test.is_username_displayed
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()

    @pytest.mark.nondestructive
    def test_login_moderator(self, selenium, ldap, token, urls):
        test = Moderator(selenium, urls['moderator'])
        two_factor_authentication_page = test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        two_factor_authentication_page.enter_passcode(current_passcode)
        while two_factor_authentication_page.is_error_message_displayed:
            two_factor_authentication_page.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            two_factor_authentication_page.enter_passcode(conftest.passcode(ldap['secret_seed']))
        assert test.is_logout_button_displayed
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.logout()

    def test_login_reps(self, selenium, ldap, token, urls):
        test = Reps(selenium, urls['reps'])
        two_factor_authentication_page = test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        two_factor_authentication_page.enter_passcode(current_passcode)
        while two_factor_authentication_page.is_error_message_displayed:
            two_factor_authentication_page.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            two_factor_authentication_page.enter_passcode(conftest.passcode(ldap['secret_seed']))
        assert test.is_logout_button_displayed
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()

    def test_login_standups(self, selenium, ldap, token, urls):
        test = Standups(selenium, urls['standups'])
        two_factor_authentication_page = test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        two_factor_authentication_page.enter_passcode(current_passcode)
        while two_factor_authentication_page.is_error_message_displayed:
            two_factor_authentication_page.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            two_factor_authentication_page.enter_passcode(conftest.passcode(ldap['secret_seed']))
        assert test.is_logout_button_displayed
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()
