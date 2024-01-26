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

#### For users, the file should be a csv file with the following columns:

1. name: string
2. type: string, either "emp" for employee or "vis"" for visitor
3. priority: int, with 0 being the highest priority
4. shift: int

#### For parking slots, the file should be a csv file with the following columns:

1. slot: string, the name of the slot, which includes its area and number
2. priority: int, with 0 being the highest priority
