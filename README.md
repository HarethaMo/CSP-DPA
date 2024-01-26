## How to use

This is a command line app, you need python3 and pandas installed.

To do a test run with the provided data, run the following command:

```bash
python main.py
```

If you want to use your own data files, you can run the following command:

```bash
python main.py --users <path_to_users_file> --slots <path_to_parking_slots_file>
```

For users, the file should be a csv file with the following columns:
name: string
type: string, either "emp" for employee or "vis"" for visitor
priority: int, with 0 being the highest priority
shift: int

For parking slots, the file should be a csv file with the following columns:
slot: string, the name of the slot, which includes its area and number
priority: int, with 0 being the highest priority
