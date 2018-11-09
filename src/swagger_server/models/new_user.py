# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user_type import UserType  # noqa: F401,E501
from swagger_server import util


class NewUser(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: UserType=None, email: str=None, name: str=None):  # noqa: E501
        """NewUser - a model defined in Swagger

        :param type: The type of this NewUser.  # noqa: E501
        :type type: UserType
        :param email: The email of this NewUser.  # noqa: E501
        :type email: str
        :param name: The name of this NewUser.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'type': UserType,
            'email': str,
            'name': str
        }

        self.attribute_map = {
            'type': 'type',
            'email': 'email',
            'name': 'name'
        }

        self._type = type
        self._email = email
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'NewUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NewUser of this NewUser.  # noqa: E501
        :rtype: NewUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> UserType:
        """Gets the type of this NewUser.


        :return: The type of this NewUser.
        :rtype: UserType
        """
        return self._type

    @type.setter
    def type(self, type: UserType):
        """Sets the type of this NewUser.


        :param type: The type of this NewUser.
        :type type: UserType
        """

        self._type = type

    @property
    def email(self) -> str:
        """Gets the email of this NewUser.


        :return: The email of this NewUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this NewUser.


        :param email: The email of this NewUser.
        :type email: str
        """

        self._email = email

    @property
    def name(self) -> str:
        """Gets the name of this NewUser.


        :return: The name of this NewUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this NewUser.


        :param name: The name of this NewUser.
        :type name: str
        """

        self._name = name
