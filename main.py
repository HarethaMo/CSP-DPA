from structures import User, PrakingSlot
from algorithm import DynamicParkingAllocation
from constraints import constraints
from get_input_args import get_input_args
from get_variables_domains import get_users, get_slots

def main():
    input_args = get_input_args()

    users_path = input_args.users
    slots_path = input_args.slots
    
    users_list = get_users(users_path)
    slots_list = get_slots(slots_path)
    
    dynamic_parking_allocation = DynamicParkingAllocation(users_list, slots_list, constraints)
    assignments = dynamic_parking_allocation.depth_first_backtracking_search()
    
    
    if assignments is None:
        print("No solution found.")
        return
    
    print("Parking slots assignment:\n")
    for key, value in assignments.items():
        print(f"{key}: {value}")
    
    
    

if __name__ == "__main__":  
    main()
    