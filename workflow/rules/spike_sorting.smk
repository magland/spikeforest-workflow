rule mountainsort4:
    input: "data/recordings/{study_set}.{study}.{recording}.json"
    output: "data/sortings/{study_set}.{study}.{recording}.mountainsort4.json"
    shell: "python workflow/scripts/run_spike_sorting.py {input} {output} mountainsort4"

rule spykingcircus:
    input: "data/recordings/{study_set}.{study}.{recording}.json"
    output: "data/sortings/{study_set}.{study}.{recording}.spykingcircus.json"
    shell: "python workflow/scripts/run_spike_sorting.py {input} {output} spykingcircus"

rule kilosort2:
    input: "data/recordings/{study_set}.{study}.{recording}.json"
    output: "data/sortings/{study_set}.{study}.{recording}.kilosort2.json"
    shell: "python workflow/scripts/run_spike_sorting.py {input} {output} kilosort2"

rule kilosort3:
    input: "data/recordings/{study_set}.{study}.{recording}.json"
    output: "data/sortings/{study_set}.{study}.{recording}.kilosort3.json"
    shell: "python workflow/scripts/run_spike_sorting.py {input} {output} kilosort3"

rule tridesclous:
    input: "data/recordings/{study_set}.{study}.{recording}.json"
    output: "data/sortings/{study_set}.{study}.{recording}.tridesclous.json"
    shell: "python workflow/scripts/run_spike_sorting.py {input} {output} tridesclous"