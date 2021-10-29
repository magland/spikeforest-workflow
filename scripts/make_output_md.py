import json
import sys
import yaml

def main():
    input_fname = sys.argv[1]
    output_fname = sys.argv[2]
    with open(input_fname, 'r') as f:
        recordings = json.load(f)

    md = ''
    md += '| Recording      |\n'
    md += '| ----------- |\n'
    for r in recordings:
        study_name = r['studyName']
        recording_name = r['name']
        view_url = r['viewUrl']
        md += f'| [{study_name}/{recording_name}]({view_url}) |\n'

    with open(output_fname, 'w') as f:
        f.write(md)

if __name__ == '__main__':
    main()