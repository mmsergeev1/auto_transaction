from __future__ import print_function
import ynab
from ynab.rest import ApiException


def get_user(token):
    # Configure API key authorization: bearer
    configuration = ynab.Configuration()
    configuration.api_key['Authorization'] = str(token)
    configuration.api_key_prefix['Authorization'] = 'Bearer'

    # create an instance of the API class
    api_instance = ynab.UserApi(ynab.ApiClient(configuration))

    try:
        # User info
        api_response = api_instance.get_user()
        return api_response
    except ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
