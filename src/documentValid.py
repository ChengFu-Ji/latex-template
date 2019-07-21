class document_valid(model.Attribute):

  def __init__(self, base_rdd, measure_rdd):
    self.base=base_rdd
    self.measure=measure_rdd

  def quantification(self):
    result1 = self.base.map(lambda x: ("valid", x))\
              .filter(pattern).collect()
    result2 = self.measure.map(lambda x: ("valid", x))\
              .filter(pattern).collect()

    if result1 != None and result2 != None:
		if result1 == result2:
          return 100 
        else:
          return 50
    if result2 == None
        return 30
