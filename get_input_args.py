from argparse import ArgumentParser

def get_input_args():
    
    parser = ArgumentParser()
    
    parser.add_argument('--users', type=str, default='users.csv', help='Path to the users csv file.')
    parser.add_argument('--slots', type=str, default='parking_slots.csv', help='Path to the parking slots csv file.')
    
    return parser.parse_args()