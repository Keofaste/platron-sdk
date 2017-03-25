from platron.request.data_objects.data_object import DataObject
from platron.request.data_objects.tripleg import TripLeg
from platron.sdk_exception import SdkException

class LongRecord(DataObject):
    '''
    Long record data to send in DoCapture request
    '''

    def __init__(self, passanger_name, ticket_number, ticket_restricked):
        self.pg_ticket_passenger_name = passanger_name
        self.pg_ticket_number = ticket_number
        self.pg_ticket_restricted = ticket_restricked
        
    def set_ticket_system(self, ticket_system):
        self.pg_ticket_system = ticket_system
        return self
    
    def set_agency_code(self, agency_code):
        self.pg_ticket_agency_code = agency_code
        return self
    
    def add_tripleg(self, tripleg):
        if type(tripleg) != TripLeg:
            raise SdkException('Only long record object expected')
        
        for param_name in tripleg.keys():
            setattr(self, param_name, tripleg.get(param_name))
            
        return self