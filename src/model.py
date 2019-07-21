#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import abc 

class Model(abc.ABC):

    dimension = list()
    value = 0.0

    @abc.abstractmethod
    def set_dimensions():
        pass

    @abc.abstractmethod
    def get_dimensions():
        pass

    @abc.abstractmethod
    def veracity_value():
        pass

