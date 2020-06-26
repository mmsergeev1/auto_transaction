from __future__ import print_function
import ynab
from ynab.rest import ApiException


class YnabAPI:
    def __init__(self, token):
        self.api_token = token

    def get_budget_list(self):
        # Configure API key authorization: bearer
        configuration = ynab.Configuration()
        configuration.api_key['Authorization'] = self.api_token
        configuration.api_key_prefix['Authorization'] = 'Bearer'

        # create an instance of the API class
        api_instance = ynab.BudgetsApi(ynab.ApiClient(configuration))

        try:
            # List budgets
            api_response = api_instance.get_budgets()
            return api_response
        except ApiException as e:
            print("Exception when calling BudgetsApi->get_budgets: %s\n" % e)

    def get_transaction_list(self, budget_id, since_date):
        # Configure API key authorization: bearer
        configuration = ynab.Configuration()
        configuration.api_key['Authorization'] = self.api_token
        configuration.api_key_prefix['Authorization'] = 'Bearer'

        # create an instance of the API class
        api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
        budget_id = budget_id
        since_date = since_date
        transaction_type = 'categorized'

        try:
            # List transactions
            api_response = api_instance.get_transactions(budget_id, since_date=since_date, type=transaction_type)
            return api_response
        except ApiException as e:
            print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
