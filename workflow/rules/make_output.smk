from common import RECORDINGS_PROCESSED_DIR, OUTPUT_JSON, OUTPUT_MD


rule make_output_json:
    input: expand(RECORDINGS_PROCESSED_DIR + '/{recording}.json', recording=config['recordings'])
    output: OUTPUT_JSON
    shell: "python workflow/scripts/make_output_json.py {output} {input}"

rule make_output_md:
    input: OUTPUT_JSON
    output: OUTPUT_MD
    shell: "python workflow/scripts/make_output_md.py {input} {output}"