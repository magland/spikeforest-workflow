RECORDINGS = [
    'PAIRED_KAMPFF.paired_kampff.2014_11_25_Pair_3_0',
    'PAIRED_KAMPFF.paired_kampff.2015_09_03_Pair_9_0A',
    'PAIRED_KAMPFF.paired_kampff.2015_09_03_Pair_9_0B',
    'PAIRED_KAMPFF.paired_kampff.c14',
    'SYNTH_MAGLAND.synth_magland_noise10_K10_C4.001_synth',
    'SYNTH_MAGLAND.synth_magland_noise10_K10_C4.002_synth',
    'SYNTH_MAGLAND.synth_magland_noise10_K10_C4.003_synth'
]

SPIKEFOREST_RECORDINGS_REPO = "https://github.com/flatironinstitute/spikeforest_recordings"
SPIKEFOREST_RECORDINGS_DIR = "data/spikeforest_recordings"

RECORDINGS_DIR = "data/recordings"
RECORDINGS_DOWNLOADED_DIR = "data/recordings_downloaded"
SPIKESORTINGVIEW_DATA_DIR = "data/spikesortingview_data"
RECORDINGS_PROCESSED_DIR = "data/recordings_processed"

OUTPUT_JSON = "output.json"
OUTPUT_MD = "output.md"

rule all:
    input: OUTPUT_MD, OUTPUT_JSON

rule get_recording:
    input: srdir=SPIKEFOREST_RECORDINGS_DIR
    output: RECORDINGS_DIR + '/{recording}.json'
    shell: "python scripts/get_recording.py {input.srdir} {wildcards.recording} {output}"

rule download_recording:
    input: RECORDINGS_DIR + '/{recording}.json'
    output: RECORDINGS_DOWNLOADED_DIR + '/{recording}.json'
    shell: "python scripts/download_recording.py {input} {output}"

rule prepare_spikesortingview_data:
    input: RECORDINGS_DOWNLOADED_DIR + '/{recording}.json'
    output: SPIKESORTINGVIEW_DATA_DIR + '/{recording}.spikesortingview.h5'
    shell: "python scripts/prepare_spikesortingview_data.py {input} {output}"

rule process_recording:
    input: rec=RECORDINGS_DIR + '/{recording}.json', ssvd=SPIKESORTINGVIEW_DATA_DIR + '/{recording}.spikesortingview.h5'
    output: RECORDINGS_PROCESSED_DIR + '/{recording}.json'
    shell: "FIGURL_CHANNEL=flatiron1 python scripts/process_recording.py {input} {output}"

rule clone_recordings:
    output: directory(SPIKEFOREST_RECORDINGS_DIR)
    shell: f"git clone {SPIKEFOREST_RECORDINGS_REPO}" + " {output}"

rule make_output_json:
    input: expand(RECORDINGS_PROCESSED_DIR + '/{recording}.json', recording=RECORDINGS)
    output: OUTPUT_JSON
    shell: "python scripts/make_output_json.py {output} {input}"

rule make_output_md:
    input: OUTPUT_JSON
    output: OUTPUT_MD
    shell: "python scripts/make_output_md.py {input} {output}"