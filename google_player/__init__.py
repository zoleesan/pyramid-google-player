from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan('.views')
    return config.make_wsgi_app()
