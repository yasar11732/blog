# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1561701784.136
_enable_loop = True
_template_filename = u'themes/ysarnet2/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'feeds_translations', context._clean_inheritance_tokens(), templateuri=u'feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'feeds_translations')] = ns

    ns = runtime.TemplateNamespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pagination')] = ns

    ns = runtime.TemplateNamespace(u'math', context._clean_inheritance_tokens(), templateuri=u'math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'math')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'feeds_translations')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context._locals(__M_locals))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        comments = _mako_get_namespace(context, 'comments')
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'feeds_translations')._populate(_import_ns, [u'*'])
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def content():
            return render_content(context)
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer(u'\n')
        if 'main_index' in pagekind:
            __M_writer(u'    ')
            __M_writer(unicode(front_index_header))
            __M_writer(u'\n')
        if page_links:
            __M_writer(u'    ')
            __M_writer(unicode(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer(u'\n')
        __M_writer(u'<div class="postindex">\n')
        for post in posts:
            __M_writer(u'    <article class="h-entry post-')
            __M_writer(unicode(post.meta('type')))
            __M_writer(u'">\n    <header class="index-header">\n        <time class="index-date" datetime="')
            __M_writer(unicode(post.formatted_date('webiso')))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
            __M_writer(u'</time>\n        <a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="index-link">')
            __M_writer(filters.html_escape(unicode(post.title())))
            __M_writer(u'</a>\n    </header>\n    </article>\n')
        __M_writer(u'</div>\n')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        __M_writer(unicode(math.math_scripts_ifposts(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'feeds_translations')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer(u'        <link rel="prefetch" href="')
            __M_writer(unicode(posts[0].permalink()))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'    ')
        __M_writer(unicode(math.math_styles_ifposts(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'feeds_translations')._populate(_import_ns, [u'*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(feeds_translations.translation_link()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 25, "129": 25, "130": 27, "131": 28, "132": 29, "133": 29, "134": 29, "135": 31, "136": 31, "137": 31, "138": 31, "139": 31, "140": 31, "141": 32, "142": 32, "143": 32, "144": 32, "145": 36, "146": 37, "147": 37, "148": 38, "149": 38, "150": 39, "23": 6, "26": 5, "175": 12, "29": 3, "32": 2, "35": 4, "41": 0, "170": 9, "171": 10, "172": 10, "173": 11, "174": 12, "157": 9, "176": 12, "177": 14, "178": 14, "179": 14, "185": 18, "151": 39, "202": 196, "194": 18, "195": 19, "196": 19, "71": 2, "72": 3, "73": 4, "74": 5, "75": 6, "76": 7, "81": 15, "86": 40, "92": 17, "116": 17, "121": 20, "122": 21, "123": 22, "124": 22, "125": 22, "126": 24, "127": 25}, "uri": "index.tmpl", "filename": "themes/ysarnet2/templates/index.tmpl"}
__M_END_METADATA
"""
