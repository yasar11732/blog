# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1561701784.294
_enable_loop = True
_template_filename = u'themes/ysarnet2/templates/base_header.tmpl'
_template_uri = u'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_translation_header', 'html_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <nav id="menu">\n')
        for url, text in navigation_links[lang]:
            __M_writer(u'                <a href="')
            __M_writer(unicode(url))
            __M_writer(u'">')
            __M_writer(unicode(text))
            __M_writer(u'</a>\n')
        __M_writer(u'    ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'        <div id="toptranslations">\n            <h2>')
            __M_writer(unicode(messages("Languages:")))
            __M_writer(u'</h2>\n            ')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <header class="fixed-top"><div class="container">\n        <a href="http://ysar.net">\n            <img class="logo" src="/assets/img/Logo.svg" />\n        </a>\n        <div class="subtitle">Python, Yaz\u0131l\u0131m ve Programlama</div>\n    <nav id="menu">\n        <ul>\n            <li class="fi-info"><a href="/yasar-arabaci.html">Hakk\u0131mda</a></li>\n            <li class="fi-social-github"><a href="https://github.com/yasar11732/">GitHub</a></li>\n            <li class="question"><a href="/soru-cevap.html">Soru-Cevap</a></li>\n            <li class="fi-rss"><a href="/rss.xml">RSS</a></li>\n        </ul>\n    </nav>\n</div>\n        \n    </header>\n    ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <h1 id="brand"><a href="')
        __M_writer(unicode(abs_link(_link("root", None, lang))))
        __M_writer(u'" title="')
        __M_writer(filters.html_escape(unicode(blog_title)))
        __M_writer(u'" rel="home">\n')
        if logo_url:
            __M_writer(u'        <img src="')
            __M_writer(unicode(logo_url))
            __M_writer(u'" alt="')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'" id="logo">\n')
        __M_writer(u'\n')
        if show_blog_title:
            __M_writer(u'        <span id="blog-title">')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</span>\n')
        __M_writer(u'    </a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 27, "129": 29, "130": 30, "131": 31, "132": 31, "133": 31, "134": 33, "140": 134, "23": 2, "26": 0, "33": 2, "34": 22, "35": 34, "36": 44, "37": 53, "43": 36, "52": 36, "53": 38, "54": 39, "55": 39, "56": 39, "57": 39, "58": 39, "59": 41, "60": 41, "61": 41, "62": 42, "63": 42, "69": 46, "79": 46, "80": 47, "81": 48, "82": 49, "83": 49, "84": 50, "85": 50, "91": 4, "98": 4, "99": 21, "100": 21, "106": 24, "118": 24, "119": 25, "120": 25, "121": 25, "122": 25, "123": 26, "124": 27, "125": 27, "126": 27, "127": 27}, "uri": "base_header.tmpl", "filename": "themes/ysarnet2/templates/base_header.tmpl"}
__M_END_METADATA
"""
