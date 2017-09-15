#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pest_rule_builder import build_to_pest_rule

# See also: http://www.fileformat.info/info/unicode/category/Zs/list.htm
unicode_zclass_characters = [
    0x0020, # SPACE
    0x00A0, # NO-BREAK SPACE
    0x1680, # OGHAM SPACE MARK (dash)
    0x2000, # EN QUAD
    0x2001, # EM QUAD
    0x2002, # EN SPACE
    0x2003, # EM SPACE
    0x2004, # THREE-PER-EM SPACE
    0x2005, # FOUR-PER-EM SPACE
    0x2006, # SIX-PER-EM SPACE
    0x2007, # FIGURE SPACE
    0x2008, # PUNCTUATION SPACE
    0x2009, # THIN SPACE
    0x200A, # HAIR SPACE
    0x202F, # NARROW NO-BREAK SPACE
    0x205F, # MEDIUM MATHEMATICAL SPACE
    0x3000, # IDEOGRAPHIC SPACE
]

pest_rule = build_to_pest_rule(rule_name="unicode_zsclass", code_point_list=unicode_zclass_characters)

with open(file='markdown.pest', mode='a', encoding='utf-8') as pest_file:
    pest_file.write('{0}\n'.format(pest_rule))
