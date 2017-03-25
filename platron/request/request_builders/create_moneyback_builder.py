from platron.request.request_builders.request_builder import RequestBuilder

class CreateMoneybackBuilder(RequestBuilder):
    '''
    Create moneyback API request
    '''

    def __init__(self, contract, moneyback_system, amount, description, ps_additional_params):
        self.pg_contract_id = contract
        self.pg_moneyback_system = moneyback_system
        self.pg_amount = amount
        self.pg_description = description
        for ps_param_name in ps_additional_params.keys():
            setattr(self, ps_param_name, ps_additional_params.get(ps_param_name))

    def get_url(self):
        return self.PLATRON_URL + 'create_moneyback.php'
                
    def bind_to_transaction(self, payment):
        self.pg_payment_id = payment