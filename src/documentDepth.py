class document_depth(model.Attribute):

  def __init__(self, base_rdd, measure_rdd):
    self.base=base_rdd
    self.measure=measure_rdd

  def quantification(self):
	sc = SparkContext(appName = "Guide")
	result1 = sc.textFile(self.base)\
              .map(lambda x: x.split("\n")).count()
	result2 = sc.textFile(self.measure)\
              .map(lambda x: x.split("\n")).count()

	if result1 > result2:
		return (result2/result1)*100
	else:
		return (result1/result2)*100
