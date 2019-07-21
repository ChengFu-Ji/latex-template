class document_standalone(model.Attribute):

  def __init__(self, base_rdd, measure_rdd):
    self.base=base_rdd
    self.measure=measure_rdd

  def quantification(self):
    result1=self.base.map(lambda x:("standalone",x))\
              .filter(pattern)
    result2=self.measure.map(lambda x:("standalone",x))\
              .filter(pattern)
 
    total_result=result1.union(result2).collect()

    if total_result[0][1]==total_result[1][1]:
      if total_result[1][1]=='<?xml version="1.0" standalone="no"?>':
        return 100
    else:
      return 50
