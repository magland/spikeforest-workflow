from common import RECORDINGS_DIR, SPIKESORTINGVIEW_DATA_DIR, RECORDINGS_PROCESSED_DIR

rule process_recording:
    input: rec=RECORDINGS_DIR + '/{recording}.json', ssvd=SPIKESORTINGVIEW_DATA_DIR + '/{recording}.spikesortingview.h5'
    output: RECORDINGS_PROCESSED_DIR + '/{recording}.json'
    shell: "FIGURL_CHANNEL=flatiron1 python workflow/scripts/process_recording.py {input} {output}"
