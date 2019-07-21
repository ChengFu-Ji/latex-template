#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import abc 

class Dimension(abc.ABC):

    attributes = list()
    degree = 0.0
	
    @abc.abstractmethod
    def set_attributes():
        pass

    @abc.abstractmethod
    def get_dimension_name():
        pass

    @abc.abstractmethod
    def get_attributes():
        pass

    @abc.abstractmethod
    def dimension_degree():
        pass
