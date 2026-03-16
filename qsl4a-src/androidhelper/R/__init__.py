'android.R module, include id,layout,style Constants .'
class R:
    @property
    def id(self):
        from . import id
        R.id=id
        return id
    @property
    def layout(self):
        from . import layout
        R.layout=layout
        return layout
    @property
    def style(self):
        from . import style
        R.style=style
        return style
R.__doc__=__doc__