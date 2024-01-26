
def occupied_constraint(user):
    """
    Checks if the user is assigned to an occupied slot.

    Args:
        user (User): The user to check.

    Returns:
        bool: True if the user is assigned to an unoccupied slot, False otherwise.
    """
    
    # If the assigned slot is unoccupied, set it as occupied and return True
    if not user.assigned_slot.is_occupied:
        user.assigned_slot.is_occupied = True
        return True
    else:
        return False
    
    

constraints = [occupied_constraint]