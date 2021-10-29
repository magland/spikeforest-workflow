import json
import sys
import yaml

def main():
    output_fname = sys.argv[1]
    records = []
    for j in range(2, len(sys.argv)):
        input_fname = sys.argv[j]
        with open(input_fname, 'r') as f:
            records.append(json.load(f))
    with open(output_fname, 'w') as f:
        json.dump(records, f, indent=4)

if __name__ == '__main__':
    main()