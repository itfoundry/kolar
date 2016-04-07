#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

def generate(self):
    self.import_glyphs_from(
        source_dir = 'masters/Latin/',
        target_dir = 'masters/Kannada/',
        excluding_names = 'space NULL CR apostrophe'.split(),
    )
    self.derive_glyphs('NULL CR'.split())

kit.Master.generate = generate

# ---

family = kit.Family(
    client = 'Google Fonts',
    base_name = 'Kolar',
    script = 'Kannada',
)

i = family.info
i.openTypeNameDesigner = "Ramakrishna Saiteja (Kannada); Shiva Nallaperumal (Latin)"
i.openTypeHheaAscender, i.openTypeHheaDescender = (1050, -750)

family.set_masters()
family.set_styles([
    ('Light',       0, 300),
    ('Regular',     9, 400),
    ('Medium',     26, 500),
    ('SemiBold',   49, 600),
    ('Bold',       76, 700),
    ('ExtraBold', 100, 800),
])

# ---

project = kit.Project(
    family,
    fontrevision = '1.001',
    options = {
        # 'prep_mark_positioning': True,
        'do_style_linking': True,
        'build_ttf': True,
    },
)
project.build()
