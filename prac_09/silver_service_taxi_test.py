from silver_service_taxi import SilverServiceTaxi

taxi1 = SilverServiceTaxi("taxi1", 100, 2)
taxi1.drive(18)
print(taxi1, ",", "Fare:", taxi1.get_fare())