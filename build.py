#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    client = 'Google Fonts',
    trademark = 'Kolar',
    script = 'Kannada',
    hide_script_name = True,
)
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

builder = kit.Builder(
    family,
    fontrevision = '0.201',
    vertical_metrics = {
        'Ascender': 750,
        'Descender': -250,
        'LineGap': 200,
    },
    options = {
        'prep_mark_positioning': True,
        'override_GDEF': True,
        'do_style_linking': True,
    },
)
builder.import_glyphs(
    from_masters = [
        'masters/latin/KolarLatin-Light.ufo',
        'masters/latin/KolarLatin-Bold.ufo',
    ],
    to_masters = [
        'masters/kannada/Kolar Kannada-Light.ufo',
        'masters/kannada/Kolar Kannada-Bold.ufo',
    ],
    save_to_masters = [
        'masters/Kolar-Light.ufo',
        'masters/Kolar-Bold.ufo',
    ],
    excluding_names = 'space CR NULL'.split(),
    deriving_names = 'CR NULL'.split(),
)
builder.build()
