from common import RECORDINGS_DOWNLOADED_DIR, SPIKESORTINGVIEW_DATA_DIR

rule prepare_spikesortingview_data:
    input: RECORDINGS_DOWNLOADED_DIR + '/{recording}.json'
    output: SPIKESORTINGVIEW_DATA_DIR + '/{recording}.spikesortingview.h5'
    shell: "python workflow/scripts/prepare_spikesortingview_data.py {input} {output}"
