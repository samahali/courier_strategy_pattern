from abc import abstractmethod, ABC


class Shipment(ABC):
    def __init__(self):
        self.cancel_shipping_behavior = None

    @abstractmethod
    def create_shipment(self, reference_number: str, merchant: object, customer: object, weight: dict):
        pass

    @abstractmethod
    def track_shipment_status(self, reference_number: str):
        pass

    @abstractmethod
    def map_shipment_status(self):
        pass

    def perform_cancel_shipping(self, reference_number: str):
        self.cancel_shipping_behavior.cancel(reference_number)


class WayBill(ABC):
    @abstractmethod
    def create_waybill(self):
        pass

    @abstractmethod
    def print_waybill(self):
        pass


class Courier(WayBill, Shipment):
    def create_shipment(self, reference_number: str, merchant: object, customer: object, weight: dict):
        pass

    def track_shipment_status(self, reference_number: str):
        pass

    def map_shipment_status(self):
        pass

    def create_waybill(self):
        pass

    def print_waybill(self):
        pass


class CancelShippingBehavior(ABC):

    @abstractmethod
    def cancel(self):
        pass


class CancelShipping(CancelShippingBehavior):
    def cancel(self, reference_number: str):
        pass


class CourierWithCanceling(Courier):

    def __init__(self):
        super().__init__()
        self.cancel_shipping_behavior = CancelShipping()
