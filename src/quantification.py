#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import abc

class Quantification(abc.ABC):

    dimensionDegree = 0.0

    def __init__(self, formula):
        self.formula = formula

    @abc.abstractmethod
    def score():
        pass

    @abc.abstractmethod
    def visualization():
        pass


