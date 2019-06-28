# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1561702938.586
_enable_loop = True
_template_filename = u'c:/python27/lib/site-packages/nikola/data/themes/base/templates/gallery.tmpl'
_template_uri = u'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'sourcelink', u'extra_js', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'ui', context._clean_inheritance_tokens(), templateuri=u'crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'ui')] = ns

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
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(ui.bar(crumbs)))
        __M_writer(u'\n')
        if title:
            __M_writer(u'    <h1>')
            __M_writer(filters.html_escape(unicode(title)))
            __M_writer(u'</h1>\n')
        if post:
            __M_writer(u'    <p>\n        ')
            __M_writer(unicode(post.text()))
            __M_writer(u'\n    </p>\n')
        if folders:
            __M_writer(u'    <ul>\n')
            for folder, ftitle in folders:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(folder))
                __M_writer(u'"><i\n        class="icon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(unicode(ftitle)))
                __M_writer(u'</a></li>\n')
            __M_writer(u'    </ul>\n')
        __M_writer(u'\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer(u'<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(image['url']))
                __M_writer(u'" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(unicode(image['title'])))
                __M_writer(u'">\n            <img src="')
                __M_writer(unicode(image['url_thumb']))
                __M_writer(u'" alt="')
                __M_writer(filters.html_escape(unicode(image['title'])))
                __M_writer(u'" /></a>\n')
            __M_writer(u'</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer(u'    ')
            __M_writer(unicode(comments.comment_form(None, permalink, title)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        def extra_js():
            return render_extra_js(context)
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<script src="/assets/js/flowr.js"></script>\n<script>\njsonContent = ')
        __M_writer(unicode(photo_array_json))
        __M_writer(u';\nflowr(document.querySelectorAll("#gallery_container")[0], {\n        data : jsonContent,\n        height : ')
        __M_writer(unicode(thumbnail_size))
        __M_writer(u'*.6,\n        padding: 5,\n        rows: -1,\n        render : function(params) {\n            // Just return a div, string or a dom object, anything works fine\n            var img = document.createElement("img");\n            img.setAttribute(\'src\', params.itemData.url_thumb);\n            img.setAttribute(\'width\', params.width);\n            img.setAttribute(\'height\', params.height);\n            img.setAttribute(\'alt\', params.itemData.title);\n            img.style.maxWidth = \'100%\';\n            link = document.createElement("a");\n            link.setAttribute(\'href\', params.itemData.url);\n            link.setAttribute(\'class\', \'image-reference\');\n            div = document.createElement("div");\n            div.setAttribute(\'class\', \'image-block\');\n            div.setAttribute(\'title\', params.itemData.title);\n            div.setAttribute(\'data-toggle\', "tooltip")\n            link.append(img);\n            div.append(link);\n            //div.hover(div.tooltip());\n            return div;\n        },\n        itemWidth : function(data) { return data.size.w; },\n        itemHeight : function(data) { return data.size.h; },\n        complete : function(params) {\n            if( jsonContent.length > params.renderedItems ) {\n                nextRenderList = jsonContent.slice( params.renderedItems );\n            }\n        }\n    });\n    baguetteBox.run(\'#gallery_container\', {\n        captions: function(element) {\n            return element.getElementsByTagName(\'img\')[0].alt;\n    }});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    .image-block {\n        display: inline-block;\n    }\n    .flowr_row {\n        width: 100%;\n    }\n    </style>\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang:
                    __M_writer(u'             <link rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'" href="')
                    __M_writer(unicode(_link('gallery', gallery_path, langname)))
                    __M_writer(u'">\n')
        __M_writer(u'<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 21, "129": 21, "130": 23, "131": 25, "132": 27, "133": 28, "134": 30, "135": 31, "136": 31, "137": 31, "138": 31, "139": 31, "140": 32, "141": 32, "142": 32, "143": 32, "144": 34, "145": 37, "146": 38, "147": 38, "148": 38, "23": 4, "26": 3, "154": 5, "32": 0, "167": 63, "177": 63, "178": 66, "179": 66, "180": 69, "181": 69, "187": 42, "65": 2, "66": 3, "67": 4, "72": 5, "201": 42, "202": 43, "203": 43, "204": 53, "77": 40, "206": 55, "205": 54, "208": 56, "209": 56, "82": 61, "211": 56, "212": 60, "87": 105, "218": 212, "207": 56, "93": 7, "210": 56, "111": 7, "112": 8, "113": 8, "114": 9, "115": 10, "116": 10, "117": 10, "118": 12, "119": 13, "120": 14, "121": 14, "122": 17, "123": 18, "124": 19, "125": 20, "126": 20, "127": 20}, "uri": "gallery.tmpl", "filename": "c:/python27/lib/site-packages/nikola/data/themes/base/templates/gallery.tmpl"}
__M_END_METADATA
"""
