#! /usr/bin/env AFDKOPython

import hindkit as kit

family = kit.Family(
    trademark = 'Kolar',
    script = 'Kannada',
    hide_script_name = True,
)

family.set_masters(
    modules = [
        # 'kerning',
        # 'mark_positioning',
        # 'mark_to_mark_positioning',
        # 'devanagari_matra_i_variants',
    ],
)

family.set_styles()

builder = kit.Builder(family)

builder.fontrevision = '0.200'

builder.set_options([

    'prepare_styles',   # stage i
    'prepare_features', # stage ii
    'compile',          # stage iii

    'makeinstances', #!
    # 'checkoutlines', #!
    # 'autohint',      #!

    'do_style_linking',
    'use_os_2_version_4',
    'prefer_typo_metrics',
    'is_width_weight_slope_only',

])

builder.generate_designspace()
builder.generate_fmndb()

hindkit.builder.import_glyphs(
    from_masters = [
        'masters/latin/KolarLatin-Light.ufo',
        'masters/latin/KolarLatin-Bold.ufo',
    ],
    to_masters = [
        'masters/gurmukhi/Kolar Kannada-Light.ufo',
        'masters/gurmukhi/Kolar Kannada-Bold.ufo',
    ],
    save_to_masters = [
        'masters/Kolar-Light.ufo',
        'masters/Kolar-Bold.ufo',
    ],
    excluding_names = 'space CR NULL'.split(),
    deriving_names = 'CR NULL'.split(),
)

builder.build()
