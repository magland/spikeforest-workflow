rule sorting_view:
    input: r='data/recordings/{study_set}.{study}.{recording}.json', s='data/sortings/{study_set}.{study}.{recording}.{sorter}.json'
    output: 'data/sorting_views/{study_set}.{study}.{recording}.{sorter}.json'
    params:
        sorter='{sorter}'
    shell: "FIGURL_CHANNEL=spikeforest python workflow/scripts/create_spikesortingview_url.py {input.r} {input.s} {output} {params.sorter}"