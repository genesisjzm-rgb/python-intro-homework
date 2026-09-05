#Defensive CSV Reader
#file that will be used "..data/messy-data.csv"
#some rows have missing values, some rows have extra values, and some rows have the wrong data type
#first check if file evists, if not print message and exit
#must read file with csv.DictReader
#process each row inside a try/except block
#catch valueError when amount cant be converted to float
#KeyError- when columm missing a row

import csv
from pathlib import Path

def read_file(filename):

    parsed_rows = []
    skipped_rows = []
    total_attempted = 0



    try: 
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)

                #track line numbers

            for row_num, row in enumerate(reader, start=2):
                total_attempted += 1

            
                    #check for extra columns
                if None in row:
                        skipped_rows.append(f'Row {row_num}: extra column detected -skipped')
                        continue

                try: 
                    val = row.get('amount', '')
                    amount = float(val)
                    parsed_rows.append(row)
                except KeyError:
                    skipped_rows.append(f"Row {row_num}: KeyError – missing required column")
                except ValueError as e:
                    skipped_rows.append(f"Row {row_num}: ValueError – could not convert '{row.get('amount', '')}' to float")

    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'")
        return

    # Print the report summary
    print("=== CSV Report ===")
    print(f"Rows attempted: {total_attempted}")
    print(f"Rows parsed:    {len(parsed_rows)}")
    print(f"Rows skipped:   {len(skipped_rows)}\n")

    print("Skipped rows:")
    for skip in skipped_rows:
        print(f"  {skip}")


script_dir = Path(__file__).parent
read_file(script_dir / ".." / "data" / "messy_data.csv")

