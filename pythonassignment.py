class Flight:
    def __init__(self, pid, process, start_time, priority):
        self.pid = pid
        self.process = process
        self.start_time = start_time
        self.priority = priority
    
    def display(self):
        print(f"{self.pid}\t{self.process}\t{self.start_time}\t{self.priority}")

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def sort_by_pid(self):
        self.flights.sort(key=lambda flight: flight.pid)
    
    def sort_by_start_time(self):
        self.flights.sort(key=lambda flight: flight.start_time)
    
    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        self.flights.sort(key=lambda flight: priority_order[flight.priority])
    
    def display_table(self):
        print("P_ID\tProcess\tStart Time (ms)\tPriority")
        print("--------------------------------------")
        for flight in self.flights:
            flight.display()

def main():
    flight_table = FlightTable()
    
    flight_data = [
        ("P1", "VSCode", 100, "MID"),
        ("P23", "Eclipse", 234, "MID"),
        ("P93", "Chrome", 189, "High"),
        ("P42", "JDK", 9, "High"),
        ("P9", "CMD", 7, "High"),
        ("P87", "NotePad", 23, "Low")
    ]
    
    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)
    
    sorting_options = {
        1: flight_table.sort_by_pid,
        2: flight_table.sort_by_start_time,
        3: flight_table.sort_by_priority
    }
    
    print("Choose sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    
    choice = int(input("Enter your choice: "))
    
    if choice in sorting_options:
        sorting_options[choice]()
        flight_table.display_table()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
