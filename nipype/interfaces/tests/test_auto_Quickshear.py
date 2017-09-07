# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..quickshear import Quickshear


def test_Quickshear_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    buff=dict(argstr='%d',
    position=4,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    mask_file=dict(argstr='%s',
    mandatory=True,
    position=2,
    ),
    out_file=dict(argstr='%s',
    keep_extension=True,
    name_source='in_file',
    name_template='%s_defaced',
    position=3,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Quickshear.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Quickshear_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Quickshear.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
