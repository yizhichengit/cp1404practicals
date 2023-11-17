from silver_service_taxi import SilverServiceTaxi
def test_silver_service_taxi():
    """Test function for the SilverServiceTaxi class."""
    # Create a SilverServiceTaxi instance with a fanciness level of 2
    silver_taxi = SilverServiceTaxi("Silver Service", 100, 2)
    silver_taxi.drive(18)  # Drive 18 km
    fare = silver_taxi.get_fare()
    print(f"Silver Service Taxi fare for 18 km trip: ${fare:.2f}")

    # Print the details of the taxi
    print(silver_taxi)
if __name__ == '__main__':
    test_silver_service_taxi()