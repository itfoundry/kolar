#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    client = 'Google Fonts',
    script = 'Kannada',
    trademark = 'Kolar',
    designers = 'Ramakrishna Saiteja (Kannada); Shiva Nallaperumal (Latin)',
)
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

builder = kit.Builder(
    family,
    fontrevision = '0.900',
    vertical_metrics = {
        'Ascender': 750,
        'Descender': -250,
        'LineGap': 200,
    },
    options = {
        # 'prep_mark_positioning': True,
        'override_GDEF': True,
        'do_style_linking': True,
    },
)

kit.tools.import_glyphs(
    source_paths = [
        'masters/latin/Kolar Latin-Light.ufo',
        'masters/latin/Kolar Latin-Bold.ufo',
    ],
    target_paths = [
        'masters/kannada/Kolar Kannada-Light.ufo',
        'masters/kannada/Kolar Kannada-Bold.ufo',
    ],
    save_as_paths = [
        'masters/Kolar-Light.ufo',
        'masters/Kolar-Bold.ufo',
    ],
    excluding_names = 'space CR NULL'.split(),
    deriving_names = 'CR NULL'.split(),
)

builder.build()
