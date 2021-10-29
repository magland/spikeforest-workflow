import os
import json
import sys
import kachery_client as kc
import figurl as fig
from sortingview.experimental.SpikeSortingView import SpikeSortingView

def main():
    recording_json_fname = sys.argv[1]
    spikesortingview_data_fname = sys.argv[2]
    output_fname = sys.argv[3]
    with open(recording_json_fname, 'r') as f:
        r = json.load(f)
    X = SpikeSortingView(spikesortingview_data_fname)
    a = X.create_summary()
    b = X.create_units_table(unit_ids=X.unit_ids)
    c = X.create_autocorrelograms(unit_ids=X.unit_ids)
    d = X.create_raster_plot(unit_ids=X.unit_ids)
    e = X.create_average_waveforms(unit_ids=X.unit_ids)
    composite_data = {
        'type': 'Composite',
        'layout': 'default',
        'views': [
            {
                'type': view0.data['type'],
                'label': view0.label,
                'figureDataSha1': _upload_data_and_return_sha1(view0.data),
                'defaultHeight': 300
            }
            for view0 in [a, b, c, d, e]
        ]
    }

    F = fig.Figure(view_url='gs://figurl/spikesortingview-1', data=composite_data)
    url = F.url(label=r['studyName'] + '/' + r['name'] + ' ground truth')
    r['viewUrl'] = url
    with open(output_fname, 'w') as f:
        json.dump(r, f, indent=4)

def _upload_data_and_return_sha1(data):
    data_uri = _store_json(data)
    data_hash = data_uri.split('/')[2]
    kc.upload_file(data_uri, channel=os.environ['FIGURL_CHANNEL'])
    return data_hash

def _store_json(x: dict):
    from figurl.core.serialize_wrapper import _serialize
    return kc.store_json(_serialize(x))

if __name__ == '__main__':
    main()