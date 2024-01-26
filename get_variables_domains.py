import pandas as pd

from structures import User, PrakingSlot

def get_users(users_path):
    """
    Reads the users csv file and returns a list of User objects.
    """
    users_df = pd.read_csv(users_path)
    users = []
    for _, row in users_df.iterrows():
        user = User(row['name'], row['user_type'], row['shift'], row['priority'])
        users.append(user)
    return users

def get_slots(slots_path):
    """
    Reads the slots csv file and returns a list of ParkingSlot objects.
    """
    slots_df = pd.read_csv(slots_path, )
    slots = []
    for _, row in slots_df.iterrows():
        slot = PrakingSlot(row['slot'], row['priority'])
        slots.append(slot)
    return slots