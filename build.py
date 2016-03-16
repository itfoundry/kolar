#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    client = 'Google Fonts',
    trademark = 'Kolar',
    script = 'Kannada',
)
family.info.openTypeNameDesigner = "Ramakrishna Saiteja (Kannada); Shiva Nallaperumal (Latin)"

family.set_masters()
family.set_styles(
    style_scheme = [
        ('Light',       0, 300),
        ('Regular',     9, 400),
        ('Medium',     26, 500),
        ('SemiBold',   49, 600),
        ('Bold',       76, 700),
        ('ExtraBold', 100, 800),
    ],
)

def prepare_master(self, master):
    master.import_glyphs_from(
        source_dir = 'masters/Latin/',
        target_dir = 'masters/Kannada/',
        excluding_names = 'space NULL CR'.split(),
    )
    master.derive_glyphs('NULL CR'.split())

kit.Builder.prepare_master = prepare_master

builder = kit.Builder(
    family,
    fontrevision = '1.000',
    vertical_metrics = {
        'Ascender': 1050,
        'Descender': -450,
        'TypoAscender': 800,
        'TypoDescender': -200,
    },
    options = {
        # 'prep_mark_positioning': True,
        'override_GDEF': True,
        'do_style_linking': True,
    },
)
builder.build()
