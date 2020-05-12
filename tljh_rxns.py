from tljh.hooks import hookimpl

@hookimpl
def tljh_extra_user_pip_packages():
    # FIXME: specify versions here.
    return [
        'numpy>=1.18.0',
        'scipy>=1.3.0',
        'matplotlib>=3.1.0',
        'pandas>=1.0.0',
        'scikit-learn>=0.22',
        'torch>=1.5.0', #pytorch
        'tensorflow>=2.0.0',
        'ipdb>=0.12',
    ]


@hookimpl
def tljh_extra_user_conda_packages():
    return [
        'graph-tool',
        'rdkit'
    ]

@hookimpl
def tljh_config_post_install(config):
    """
    Set JupyterLab to be default
    """
    user_environment = config.get('user_environment', {})
    user_environment['default_app'] = user_environment.get('default_app', 'jupyterlab')

    config['user_environment'] = user_environment

@hookimpl
def tljh_post_install():
    """
    Post install script to be executed after installation
    and after all the other hooks.
    This can be arbitrary Python code.
    """
    "brew install pipenv"