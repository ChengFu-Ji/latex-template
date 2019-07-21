class document_encoding(model.Attribute):

  def __init__(self, base_rdd, measure_rdd):
    self.base=base_rdd
    self.measure=measure_rdd

  def quantification(self):
    result1=self.base.map(lambda x:("encoding", x))\
            .filter(pattern)
    result2=self.measure.map(lambda x:("encoding", x))\
            .filter(pattern)

    total_result=result1.union(result2).collect()

    if total_result[0][1]==total_result[1][1]:
      return 100
    else:
      return 0
