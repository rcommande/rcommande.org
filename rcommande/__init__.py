from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    # config.add_route('contact', '/')
    config.include('rcommande.contact', route_prefix='contact')
    return config.make_wsgi_app()
