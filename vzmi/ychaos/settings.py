#  Copyright 2021, Verizon Media
#  Licensed under the terms of the ${MY_OSI} license. See the LICENSE file in the project root for terms

from typing import Optional, Union

from pydantic import BaseModel


class ApplicationSettings(BaseModel):
    """
    Defines the Global Settings that are consistent in both Development &
    Production scenarios
    """

    APP = "YChaos"
    APP_DESC = "YChaos, The resilience testing framework"
    PROG = "ychaos"

    COMMAND_IDENTIFIER = "_cmd.{}"

    @classmethod
    def get_instance(cls):
        return cls()


class DevSettings(ApplicationSettings):
    """
    Defines the Development settings for YChaos Application.
    """

    CONFIG = "dev"


class ProdSettings(DevSettings):
    """
    Defines the Production settings for YChaos Application

    Prod Settings overrides the Dev Settings class and redefines all
    the constants defined in DevSettings that can be used in the production scenario
    """

    CONFIG = "prod"


class Settings:
    __instance: Optional[Union[DevSettings, ProdSettings]] = None

    @classmethod
    def get_instance(cls) -> Union[DevSettings, ProdSettings]:
        if cls.__instance is None:
            cls(config="prod")
        assert cls.__instance is not None
        return cls.__instance

    def __init__(self, config):
        if config == "dev":
            self.__class__.__instance = DevSettings()
        elif config == "prod":
            self.__class__.__instance = ProdSettings()
        else:
            raise Exception("Unknown configuration found")
