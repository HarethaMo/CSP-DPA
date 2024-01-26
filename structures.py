class User:
    def __init__(self, name,user_type, shift, priority):
        """
        A data structure to hold user information.
        There are 2 types of users: Employees and Visitors.
        Employees are assigned a shift and priority.
        Visitors are only assigned a priority.

        Args:
            name (str): The name of the user.
            user_type (str): The type of user. Either "emp" or "vis".
            shift (int): The index of the shift the user is assigned to.
            priority (int): The priority level of the user. 0 is highest priority.
        """
        self.name = name
        self.user_type = user_type
        self.shift = shift
        self.priority = priority
        self.assigned_slot = None
    
    

class PrakingSlot:
    def __init__(self, slot, priority):
        """
        A data structure to hold parking slot information.
        Each slot is assigned a priority and is initially unoccupied.

        Args:
            slot (str): The name of the slot. Ex: "A1" where "A" is the parking area and "1" is the slot number.
            priority (int): The priority level of the slot. 1 is highest priority.
        """
        self.slot = slot
        self.priority = priority
        self.is_occupied = False