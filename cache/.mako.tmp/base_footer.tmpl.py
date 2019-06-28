# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1561704693.496
_enable_loop = True
_template_filename = u'themes/ysarnet2-en/templates/base_footer.tmpl'
_template_uri = u'base_footer.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_footer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        content_footer = context.get('content_footer', UNDEFINED)
        template_hooks = context.get('template_hooks', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if content_footer:
            __M_writer(u'        <footer class="fixed-bottom">\n        <div class="container>\n            <p>')
            __M_writer(unicode(content_footer))
            __M_writer(u'</p>\n            ')
            __M_writer(unicode(template_hooks['page_footer']()))
            __M_writer(u'\n        </div>\n\n        </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 3, "35": 4, "36": 5, "37": 7, "38": 7, "39": 8, "40": 8, "46": 40, "16": 0, "21": 2, "22": 13, "28": 3}, "uri": "base_footer.tmpl", "filename": "themes/ysarnet2-en/templates/base_footer.tmpl"}
__M_END_METADATA
"""
