from itsdangerous import URLSafeTimedSerializer
from os import getcwd

class Config:
    SECRET_KEY                      = 'dkdkdj387942847243_+=e--=3498743bchjjk^%$%^&*(%^&**&^%$)(*^$'
    WEB_TOKEN_SERIALIZER            = URLSafeTimedSerializer("5c3b1335sdffsdfsdfsf774dlsjfdfj000d8924ea0822de9a8e657495f")
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    EXPLAIN_TEMPLATE_LOADING        = False
    SQLALCHEMY_ECHO                 = False
    SQLALCHEMY_ENGINE_OPTIONS       = {
                                        'pool_recycle':200,
                                        'pool_reset_on_return':'commit',
                                        'pool_pre_ping': True,
                                    }

    @staticmethod
    def init_app(app):
        pass

class Testconfig(Config):
    userpass                        = 'mysql://root:@'
    basedir                         = '127.0.0.1'
    dbname                          = '/inventory_store'
    SQLALCHEMY_DATABASE_URI         = userpass + basedir + dbname
    DEBUG                           = True

class Developmentconfig(Config):
    SQLALCHEMY_DATABASE_URI         = 'sqlite:///{}/App/Model/tmp/db.db'.format(getcwd())
    DEBUG                           = True

class Deploymentconfig(Config):
    SQLALCHEMY_DATABASE_URI         = 'sqlite:///{}/App/Model/tmp/db.db'.format(getcwd())
    DEBUG                           = False

config = {
    'deployment':   Deploymentconfig,
    'development':  Developmentconfig,
    'default':      Testconfig
}