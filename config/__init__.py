from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['config/settings.yaml'],
    environments=True,
    env="development",
    envvar_prefix="VIZ",
    env_switcher="VIZ_ENV"
)