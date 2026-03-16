'android.provider module, include Settings .'
class provider:
    @property
    def Settings(self):
        from . import Settings as s
        provider.Settings=s
        return s
provider.__doc__=__doc__