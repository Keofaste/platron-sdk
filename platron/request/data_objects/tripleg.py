from platron.request.data_objects.data_object import DataObject

class TripLeg(DataObject):
    '''
    Tripleg data to set in long record
    '''

    def __init__(self, tripleg_number, date, carrier, class_transport, dest_from, dest_to, stop_over, basis_code, flight_number):
        setattr(self, 'pg_tripleg_' + date + '_date', date)
        setattr(self, 'pg_tripleg_' + date + '_carrier', carrier)
        setattr(self, 'pg_tripleg_' + date + '_class', class_transport)
        setattr(self, 'pg_tripleg_' + date + '_destination_from', dest_from)
        setattr(self, 'pg_tripleg_' + date + '_destination_to', dest_to)
        setattr(self, 'pg_tripleg_' + date + '_stopover', stop_over)
        setattr(self, 'pg_tripleg_' + date + '_fare_basis_code', basis_code)
        setattr(self, 'pg_tripleg_' + date + '_flight_number', flight_number)