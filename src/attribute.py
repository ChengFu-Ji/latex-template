#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import abc

class Attribute(abc.ABC):
	
    def get_attribute_name(self):
        return __class__.__name__

    @abc.abstractmethod
    def quantification():
        pass

