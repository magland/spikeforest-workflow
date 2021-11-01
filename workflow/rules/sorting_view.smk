rule sorting_spikesortingview_data:
    input: r='data/recordings/{study_set}.{study}.{recording}.json', s='data/sortings/{study_set}.{study}.{recording}.{sorter}.json'
    output: 'data/sorting_views/{study_set}.{study}.{recording}.{sorter}.spikesortingview.h5'
    shell: "python workflow/scripts/create_spikesortingview_data.py {input.r} {input.s} {output}"

rule sorting_view:
    input: json='data/recordings/{study_set}.{study}.{recording}.json', h5='data/sorting_views/{study_set}.{study}.{recording}.{sorter}.spikesortingview.h5'
    output: 'data/sorting_views/{study_set}.{study}.{recording}.{sorter}.json'
    shell: "FIGURL_CHANNEL=flatiron1 python workflow/scripts/create_spikesortingview_url.py {input.json} {input.h5} {output}"