from common import SPIKEFOREST_RECORDINGS_DIR, RECORDINGS_DIR, SPIKEFOREST_RECORDINGS_REPO

rule get_recording:
    input: srdir=SPIKEFOREST_RECORDINGS_DIR
    output: RECORDINGS_DIR + '/{recording}.json'
    shell: "python workflow/scripts/get_recording.py {input.srdir} {wildcards.recording} {output}"

rule clone_recordings:
    output: directory(SPIKEFOREST_RECORDINGS_DIR)
    shell: f"git clone {SPIKEFOREST_RECORDINGS_REPO}" + " {output}"