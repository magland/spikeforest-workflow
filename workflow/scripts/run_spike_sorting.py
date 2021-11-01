import json
import sys
import sortingview as sv
import kachery_client as kc
from sortingview.experimental.SpikeSortingView import prepare_spikesortingview_data, SpikeSortingView
import hither2 as hi
import spikeforest as sf

def main():
    recording_json_fname = sys.argv[1]
    output_sorting_json_fname = sys.argv[2]
    sorter_name = sys.argv[3]
    with open(recording_json_fname, 'r') as f:
        r = json.load(f)
    recording_uri = r['recordingUri']
    recording_object = kc.load_json(recording_uri)

    job_cache = hi.JobCache(feed_name='spikeforest-job-cache')

    with hi.Config(use_container=True, job_cache=job_cache):
        if sorter_name == 'mountainsort4':
            job: hi.Job = sf.mountainsort4_wrapper1.run(
                recording_object=recording_object,
                detect_sign=-1,
                adjacency_radius=50,
                clip_size=50,
                detect_threshold=3,
                detect_interval=10,
                freq_min=300,
                freq_max=6000,
                whiten=True,
                filter=True
            )
        elif sorter_name == 'spykingcircus':
            job: hi.Job = sf.spykingcircus_wrapper1.run(
                recording_object=recording_object,
                detect_sign=-1,
                adjacency_radius=100,
                detect_threshold=6,
                template_width_ms=3,
                filter=True,
                merge_spikes=True,
                auto_merge=0.75,
                whitening_max_elts=1000,
                clustering_max_elts=10000
            )
        elif sorter_name == 'kilosort2':
            job: hi.Job = sf.kilosort2_wrapper1.run(
                recording_object=recording_object
            )
        elif sorter_name == 'kilosort3':
            job: hi.Job = sf.kilosort3_wrapper1.run(
                recording_object=recording_object
            )
        elif sorter_name == 'tridesclous':
            job: hi.Job = sf.tridesclous_wrapper1.run(
                recording_object=recording_object
            )
        else:
            raise Exception(f'Unexpected sorter name: {sorter_name}')
        sorting_object = job.wait().return_value

    sorting_uri = kc.store_json(sorting_object)
    output = {
        'sortingUri': sorting_uri
    }
    with open(output_sorting_json_fname, 'w') as f:
        json.dump(output, f)

if __name__ == '__main__':
    main()
