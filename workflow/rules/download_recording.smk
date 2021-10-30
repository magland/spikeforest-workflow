from common import RECORDINGS_DIR, RECORDINGS_DOWNLOADED_DIR

rule download_recording:
    input: RECORDINGS_DIR + '/{recording}.json'
    output: RECORDINGS_DOWNLOADED_DIR + '/{recording}.json'
    shell: "python workflow/scripts/download_recording.py {input} {output}"
